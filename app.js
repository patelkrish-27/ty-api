const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Endpoint to download a file
app.get("/rsa", (req, res) => {
  const filePath = path.join(__dirname, "files", "RSA.PY"); // Path to your file
  res.download(filePath, "RSA.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/caesar", (req, res) => {
  const filePath = path.join(__dirname, "files", "CAESAR.PY"); // Path to your file
  res.download(filePath, "CAESAR.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/railfence", (req, res) => {
  const filePath = path.join(__dirname, "files", "RAILFENCE.PY"); // Path to your file
  res.download(filePath, "RAILFENCE.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/hellman", (req, res) => {
  const filePath = path.join(__dirname, "files", "HELLMAN.py"); // Path to your file
  res.download(filePath, "HELLMAN.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
