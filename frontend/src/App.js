import React, { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [summary, setSummary] = useState("");

  const handleSubmit = async () => {

    if (!file || !email) {
      setMessage("Please upload a file and enter email.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("email", email);

    try {

      setMessage("Processing...");
      setSummary("");

      const response = await axios.post(
        "https://sales-insight-automator-api-o6s0.onrender.com/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      setMessage(response.data.message);
      setSummary(response.data.summary);

    } catch (error) {

      console.error(error);

      if (error.response) {
        setMessage(error.response.data.error || "Server error");
      } else {
        setMessage("Backend not reachable");
      }

    }
  };

  return (

    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h2>Sales Insight Automator</h2>

      <input
        type="file"
        accept=".csv,.xlsx"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <input
        type="email"
        placeholder="Enter recipient email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        Generate Summary
      </button>

      <br /><br />

      <p><strong>{message}</strong></p>

      {summary && (
        <div
          style={{
            background: "#f4f4f4",
            padding: "15px",
            borderRadius: "6px",
            marginTop: "10px",
            maxWidth: "700px"
          }}
        >
          <h3>AI Generated Summary</h3>
          <p>{summary}</p>
        </div>
      )}

    </div>

  );

}

export default App;