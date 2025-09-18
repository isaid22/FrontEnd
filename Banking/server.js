// server.js
const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// ---- Demo auth API ----
const DEMO_USER = { email: "demo@bank.com", password: "Demo@123" };

app.post("/api/login", (req, res) => {
  const { email, password } = req.body || {};
  if (email === DEMO_USER.email && password === DEMO_USER.password) {
    return res.json({ ok: true, email });
  }
  return res.status(401).json({ ok: false, error: "Invalid credentials" });
});

// ---- Static files ----
app.use(express.static(__dirname));

// ---- SPA fallback for all non-API GETs ----
// Works on Express 5 (no bare "*")
app.get(/^\/(?!api).*/, (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Demo running on http://localhost:${PORT}`));
