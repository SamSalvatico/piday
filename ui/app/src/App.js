import logo from "./logo.svg";
import "./App.css";
import { TextField } from "@material-ui/core";
import { React, useState } from "react";
import { DataGrid } from "@material-ui/data-grid";
import axios from "axios";

function App() {
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");
  const [results, setResults] = useState(null);

  const makeQuery = (query) => {
    let query_p = encodeURI(query);
    axios
      .get("http://35.152.84.157:5000/query_get?query=" + query_p + "&lang=it")
      .then((res) => {
        console.log(res.data);
        setResults(res.data);
      });
  };

  return (
    <div className="App">
      <div
        style={{
          display: "flex",
          alignContent: "center",
          width: "100%",
          justifyContent: "center",
        }}
      >
        <TextField
          style={{ display: "flex", width: "100%", margin: "24px" }}
          id="outlined-basic"
          onKeyPress={(ev) => {
            console.log(`Pressed keyCode ${ev.key}`);
            if (ev.key === "Enter") {
              setLoading(true);
              makeQuery(query);
              setLoading(false);
              ev.preventDefault();
            }
          }}
          label="Search"
          value={query}
          onChange={(el) => {
            console.log(el.target.value);
            setQuery(el.target.value);
          }}
          variant="outlined"
        />
      </div>
      <div style={{ height: 400, width: "100%" }}>
        {results !== null ? (
          results["data"].map((el) => <h1>{JSON.stringify(el)}</h1>)
        ) : (
          <div></div>
        )}
      </div>
    </div>
  );
}

export default App;
