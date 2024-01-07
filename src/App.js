// App.js

import React, { useState } from 'react';
import "./App.css";

const App = () => {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleQuery = async () => {
    try {
      setLoading(true);
      const now = new Date();
      const startDateTime = now.toISOString();
      const endDateTime = now.toISOString();
  
      const response = await fetch('http://127.0.0.1:8000/filtered-logs/');
  
      if (!response.ok) {
        throw new Error('Failed to fetch logs');
      }
  
      const data = await response.json();
      console.log('Data from server:', data);
  
      setLogs(data.filtered_logs); // Corrected this line
      console.log('Logs in state:', logs);
  
    } catch (error) {
      console.error('Error fetching logs:', error);
    } finally {
      setLoading(false);
    }
  };
  

  return (
    <div className="container">
      <h1>FastAPI Log Viewer</h1>

      <div>
        <button onClick={handleQuery} disabled={loading}>
          {loading ? 'Loading...' : 'Query FastAPI for Logs'}
        </button>
      </div>

      <div>
        <h2>Logs:</h2>
        {logs.length > 0 ? (
          <ul>
            {logs.map((log, index) => (
              <li key={index}>{log}</li>
            ))}
          </ul>
        ) : (
          <p>No logs to display.</p>
        )}
      </div>
    </div>
  );
};

export default App;
