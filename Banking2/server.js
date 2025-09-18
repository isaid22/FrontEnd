// server.js
const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// ---- Demo users ----
const USERS = [
  { email: "demo@bank.com", password: "Demo@123" },     // original demo
  { email: "alice@bank.com", password: "Alice@123" },   // new user 1
  { email: "bob@bank.com",   password: "Bob@123" },     // new user 2
];

// ---- API ----
app.post("/api/login", (req, res) => {
  const { email, password } = req.body || {};
  const user = USERS.find(u => u.email === email && u.password === password);
  if (user) {
    return res.json({ ok: true, email: user.email });
  }
  return res.status(401).json({ ok: false, error: "Invalid credentials" });
});

// ---- Static files ----
app.use(express.static(__dirname));

// ---- Fallback for SPA (non-API routes) ----
app.get(/^\/(?!api).*/, (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Demo running on http://localhost:${PORT}`));

