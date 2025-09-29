import { useState } from 'react';
import VideoRoom from './components/VideoRoom.jsx';
import Whiteboard from './components/Whiteboard.jsx';
import MathLessonPanel from './components/MathLessonPanel.jsx';
import './styles.css';

function App() {
  const [identity, setIdentity] = useState('');
  const [isConnected, setIsConnected] = useState(false);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Virtual Math Classroom</h1>
        <p>Teach, demonstrate, and collaborate with your students in real time.</p>
      </header>

      <main className="classroom-layout">
        <section className="video-section">
          <VideoRoom
            identity={identity}
            setIdentity={setIdentity}
            isConnected={isConnected}
            setIsConnected={setIsConnected}
          />
        </section>

        <section className="board-section">
          <Whiteboard />
        </section>

        <aside className="lesson-section">
          <MathLessonPanel />
        </aside>
      </main>
    </div>
  );
}

export default App;