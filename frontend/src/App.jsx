// src/App.jsx
import { useState } from 'react';
import Login from './components/login';
import Dashboard from './components/Dashboard';

function App() {
  const [profile, setProfile] = useState(null);

  return (
    <div className="max-w-xl mx-auto mt-10">
      {!profile ? (
        <Login onLogin={setProfile} />
      ) : (
        <Dashboard profile={profile} />
      )}
    </div>
  );
}

export default App;
