// src/App.js
import React, { useState } from "react";
import "./App.css";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isSignup, setIsSignup] = useState(false);
  const [username, setUsername] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // fake auth success
    setIsAuthenticated(true);
  };

  return (
    <div className="app-container">
      {!isAuthenticated ? (
        <div className="form-container">
          <h2>{isSignup ? "Sign Up" : "Sign In"}</h2>
          <form onSubmit={handleSubmit}>
            {isSignup && (
              <input
                type="text"
                placeholder="Full Name"
                required
                onChange={(e) => setUsername(e.target.value)}
              />
            )}
            <input type="email" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <button type="submit">{isSignup ? "Sign Up" : "Sign In"}</button>
          </form>
          <p onClick={() => setIsSignup(!isSignup)} className="toggle-link">
            {isSignup
              ? "Already have an account? Sign In"
              : "Don't have an account? Sign Up"}
          </p>
        </div>
      ) : (
        <div className="welcome-container">
          <h1>Welcome {username || "User"}! 🎉</h1>
          <p>"Success usually comes to those who are too busy to be looking for it." – Henry David Thoreau</p>
        </div>
      )}
    </div>
  );
}

export default App;
