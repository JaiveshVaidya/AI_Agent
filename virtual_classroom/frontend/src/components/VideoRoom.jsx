import { useEffect, useRef, useState } from 'react';
import { FaChalkboardTeacher, FaVideo, FaVideoSlash } from 'react-icons/fa';
import { API_BASE_URL } from '../config.js';
import { connect } from 'twilio-video';

const VideoRoom = ({ identity, setIdentity, isConnected, setIsConnected }) => {
  const [room, setRoom] = useState(null);
  const [isCameraOn, setIsCameraOn] = useState(true);
  const localVideoRef = useRef(null);
  const remoteContainerRef = useRef(null);

  useEffect(() => {
    if (!room) return;

    const handleParticipant = participant => {
      participant.tracks.forEach(publication => {
        if (publication.isSubscribed) {
          const track = publication.track;
          remoteContainerRef.current?.appendChild(track.attach());
        }
      });

      participant.on('trackSubscribed', track => {
        remoteContainerRef.current?.appendChild(track.attach());
      });

      participant.on('trackUnsubscribed', track => {
        track.detach().forEach(el => el.remove());
      });
    };

    room.participants.forEach(handleParticipant);
    room.on('participantConnected', handleParticipant);

    room.on('participantDisconnected', participant => {
      participant.tracks.forEach(publication => {
        if (publication.track) {
          publication.track.detach().forEach(el => el.remove());
        }
      });
    });

    return () => {
      room.disconnect();
      room.localParticipant.tracks.forEach(publication => {
        publication.track.stop();
        publication.track.detach().forEach(el => el.remove());
      });
    };
  }, [room]);

  const handleConnect = async event => {
    event.preventDefault();
    if (!identity) return;

    try {
      const response = await fetch(`${API_BASE_URL}/video/token`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ identity }),
      });

      if (!response.ok) {
        throw new Error('Unable to fetch access token');
      }

      const data = await response.json();
      const videoRoom = await connect(data.token, {
        name: data.room,
        audio: true,
        video: { width: 1280, height: 720 },
      });

      setRoom(videoRoom);
      setIsConnected(true);

      const localTrack = Array.from(videoRoom.localParticipant.videoTracks.values())[0]?.track;
      if (localTrack) {
        localVideoRef.current?.appendChild(localTrack.attach());
      }
    } catch (error) {
      console.error('Failed to connect to room', error);
      alert('Failed to join the classroom. Please ensure the backend is running and credentials are correct.');
    }
  };

  const handleDisconnect = () => {
    room?.disconnect();
    setRoom(null);
    setIsConnected(false);
    remoteContainerRef.current.innerHTML = '';
    localVideoRef.current.innerHTML = '';
  };

  const toggleCamera = async () => {
    const videoTrack = room?.localParticipant.videoTracks.values().next().value?.track;
    if (!videoTrack) return;

    if (isCameraOn) {
      videoTrack.disable();
    } else {
      videoTrack.enable();
    }
    setIsCameraOn(prev => !prev);
  };

  return (
    <div className="video-room">
      <h2 className="section-title">
        <span>
          <FaChalkboardTeacher />
        </span>
        Live Classroom
      </h2>

      {!isConnected ? (
        <form className="identity-form" onSubmit={handleConnect}>
          <input
            placeholder="Enter your name"
            value={identity}
            onChange={event => setIdentity(event.target.value)}
          />
          <button type="submit">Join Class</button>
        </form>
      ) : (
        <div className="video-controls">
          <button onClick={toggleCamera}>
            {isCameraOn ? <FaVideo /> : <FaVideoSlash />} {isCameraOn ? 'Disable' : 'Enable'} camera
          </button>
          <button onClick={handleDisconnect} className="leave-button">
            Leave Class
          </button>
        </div>
      )}

      <div className="video-grid">
        <div className="video-tile" ref={localVideoRef}>
          {!isConnected && <span>Your preview will appear here</span>}
        </div>
        <div className="video-tile" ref={remoteContainerRef}>
          {isConnected && !remoteContainerRef.current?.hasChildNodes() && (
            <span>Waiting for students to join…</span>
          )}
        </div>
      </div>
    </div>
  );
};

export default VideoRoom;