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
app.get("/tic", (req, res) => {
  const filePath = path.join(__dirname, "files", "TIC.PY"); // Path to your file
  res.download(filePath, "TIC.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/tower", (req, res) => {
  const filePath = path.join(__dirname, "files", "TOWER.PY"); // Path to your file
  res.download(filePath, "TOWER.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/jug", (req, res) => {
  const filePath = path.join(__dirname, "files", "JUG.PY"); // Path to your file
  res.download(filePath, "JUG.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/dfs", (req, res) => {
  const filePath = path.join(__dirname, "files", "DFS.PY"); // Path to your file
  res.download(filePath, "DFS.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/bfs", (req, res) => {
  const filePath = path.join(__dirname, "files", "BFS.PY"); // Path to your file
  res.download(filePath, "BFS.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/astar", (req, res) => {
  const filePath = path.join(__dirname, "files", "ASTAR.PY"); // Path to your file
  res.download(filePath, "ASTAR.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/aostar", (req, res) => {
  const filePath = path.join(__dirname, "files", "AOSTAR.PY"); // Path to your file
  res.download(filePath, "AOSTAR.PY", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});
app.get("/unzip", (req, res) => {
  const filePath = path.join(__dirname, "files", "UNZIP.BAT"); // Path to your file
  res.download(filePath, "UNZIP.BAT", (err) => {
    if (err) {
      console.error("Error while sending the file:", err);
      res.status(500).send("Error downloading the file");
    }
  });
});

app.get("/adapter", (req, res) => {
  const filePath = path.join(__dirname, "files", "ADAPTER.ZIP"); // Path to your ZIP file
  res.download(filePath, "ADAPTER.ZIP"); // Send file to the client
});
// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
