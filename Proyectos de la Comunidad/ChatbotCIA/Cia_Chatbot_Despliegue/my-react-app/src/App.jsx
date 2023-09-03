import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [messageHistory, setMessageHistory] = useState([]);
  const [showChat, setShowChat] = useState(false); // State to control the visibility of the chat

  const handleRequest = async () => {
    const response = await fetch('http://localhost:8001/embeddings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    setResult(data.result);
    setMessageHistory([...messageHistory, { text, result: data.result }]);
    setText('');
  };

  const toggleChat = () => {
    setShowChat(!showChat);
  };

  return (
    <div className="app-container">
      {!showChat && (
        <button className="popup-button" onClick={toggleChat}>
          Abrir Chat
        </button>
      )}
  
      {showChat && (
        <div className="chat-container">
          <div className="chat-content">
            {messageHistory.map((message, index) => (
              <div className="chat-message" key={index}>
                <hr />
                <p>Mensaje Ingresado: {message.text}</p>
                <p>Mensaje Recibido: {message.result}</p>
              </div>
            ))}
          </div>
  
          <div className="send-message">
            <input
              className="chat-input"
              type="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Ingresar texto"
            />
            <button onClick={handleRequest}>Enviar uwu</button>
          </div>
  
          <button className="chat-close-button" onClick={toggleChat}>
            Cerrar Chat
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
