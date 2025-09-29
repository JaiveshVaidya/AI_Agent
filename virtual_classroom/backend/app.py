from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

load_dotenv()

app = FastAPI(title="Virtual Classroom Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")
TWILIO_API_SECRET = os.getenv("TWILIO_API_SECRET")
TWILIO_ROOM_NAME = os.getenv("TWILIO_ROOM_NAME", "math_classroom")


class TokenRequest(BaseModel):
    identity: str


class TokenResponse(BaseModel):
    token: str
    room: str


def _build_access_token(identity: str) -> AccessToken:
    if not all([TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET]):
        raise RuntimeError("Twilio credentials are not set. Check your environment variables.")

    token = AccessToken(
        TWILIO_ACCOUNT_SID,
        TWILIO_API_KEY,
        TWILIO_API_SECRET,
        identity=identity,
    )
    video_grant = VideoGrant(room=TWILIO_ROOM_NAME)
    token.add_grant(video_grant)
    return token


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/video/token", response_model=TokenResponse)
def generate_video_token(request: TokenRequest):
    try:
        access_token = _build_access_token(request.identity)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    jwt_token = access_token.to_jwt().decode("utf-8")
    return TokenResponse(token=jwt_token, room=TWILIO_ROOM_NAME)