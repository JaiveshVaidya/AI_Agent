import { useEffect, useRef, useState } from 'react';
import { FaTrash, FaDownload } from 'react-icons/fa';

const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 500;

const Whiteboard = () => {
  const canvasRef = useRef(null);
  const contextRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [brushColor, setBrushColor] = useState('#38bdf8');
  const [brushRadius, setBrushRadius] = useState(4);

  useEffect(() => {
    const canvasElement = canvasRef.current;
    if (!canvasElement) return;

    canvasElement.width = CANVAS_WIDTH * 2;
    canvasElement.height = CANVAS_HEIGHT * 2;
    canvasElement.style.width = `${CANVAS_WIDTH}px`;
    canvasElement.style.height = `${CANVAS_HEIGHT}px`;

    const context = canvasElement.getContext('2d');
    context.scale(2, 2);
    context.lineCap = 'round';
    context.strokeStyle = brushColor;
    context.lineWidth = brushRadius;
    contextRef.current = context;
  }, []);

  useEffect(() => {
    if (contextRef.current) {
      contextRef.current.strokeStyle = brushColor;
      contextRef.current.lineWidth = brushRadius;
    }
  }, [brushColor, brushRadius]);

  const getCoordinates = event => {
    const canvasElement = canvasRef.current;
    if (!canvasElement) return { x: 0, y: 0 };

    const rect = canvasElement.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    return { x, y };
  };

  const startDrawing = event => {
    const { x, y } = getCoordinates(event);
    contextRef.current?.beginPath();
    contextRef.current?.moveTo(x, y);
    setIsDrawing(true);
  };

  const drawStroke = event => {
    if (!isDrawing) return;
    event.preventDefault();
    const { x, y } = getCoordinates(event);
    contextRef.current?.lineTo(x, y);
    contextRef.current?.stroke();
  };

  const stopDrawing = () => {
    if (!isDrawing) return;
    contextRef.current?.closePath();
    setIsDrawing(false);
  };

  const handleClear = () => {
    contextRef.current?.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  };

  const handleExport = () => {
    const canvasElement = canvasRef.current;
    if (!canvasElement) return;

    const dataUrl = canvasElement.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = dataUrl;
    link.download = 'math-whiteboard.png';
    link.click();
  };

  return (
    <div className="whiteboard-wrapper">
      <h2 className="section-title">Interactive Math Board</h2>

      <div className="whiteboard-toolbar">
        <div className="toolbar-group">
          <label>
            Color
            <input
              type="color"
              value={brushColor}
              onChange={event => setBrushColor(event.target.value)}
              style={{ marginLeft: '0.5rem' }}
            />
          </label>
          <label>
            Brush Size
            <input
              type="range"
              min="1"
              max="12"
              value={brushRadius}
              onChange={event => setBrushRadius(Number(event.target.value))}
              style={{ marginLeft: '0.5rem' }}
            />
          </label>
        </div>

        <div className="toolbar-group">
          <button onClick={handleClear} title="Clear board">
            <FaTrash />
          </button>
          <button onClick={handleExport} title="Export as PNG">
            <FaDownload />
          </button>
        </div>
      </div>

      <div className="whiteboard-canvas">
        <canvas
          ref={canvasRef}
          onMouseDown={startDrawing}
          onMouseMove={drawStroke}
          onMouseUp={stopDrawing}
          onMouseLeave={stopDrawing}
        />
      </div>
    </div>
  );
};

export default Whiteboard;