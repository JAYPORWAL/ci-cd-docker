import React, { useState } from "react";
import "./app.css";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isSignup, setIsSignup] = useState(false);
  const [formData, setFormData] = useState({ email: "", password: "" });

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsLoggedIn(true); // simulate login
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const toggleForm = () => {
    setIsSignup(!isSignup);
  };

  if (isLoggedIn) {
    return (
      <div className="welcome-page">
        <h1>🎉 Welcome to the React CI/CD App 🎉</h1>
        <p className="quote">
          “Code is like humor. When you have to explain it, it’s bad.”
        </p>
      </div>
    );
  }

  return (
    <div className="app">
      <div className="login-container">
        <h2>{isSignup ? "Sign Up" : "Login"}</h2>
        <form onSubmit={handleSubmit} className="login-form">
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <button type="submit">{isSignup ? "Sign Up" : "Login"}</button>
        </form>
        <p className="toggle-text">
          {isSignup ? "Already have an account?" : "Don't have an account?"}{" "}
          <span onClick={toggleForm} className="toggle-link">
            {isSignup ? "Login" : "Sign Up"}
          </span>
        </p>
      </div>
    </div>
  );
}

export default App;
