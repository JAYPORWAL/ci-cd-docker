// src/App.js
import React, { useState } from "react";
import "./app.css";

function App() {
  const [user, setUser] = useState({ username: "", password: "" });

  const handleLogin = (e) => {
    e.preventDefault();
    alert(`Welcome ${user.username}`);
  };

  return (
    <div className="login-container">
      <h2>React Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          onChange={(e) => setUser({ ...user, username: e.target.value })}
        />
        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setUser({ ...user, password: e.target.value })}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default App;
