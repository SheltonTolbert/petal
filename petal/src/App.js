import React from "react";
import "./App.css";
import Navbar from "./components/navbar/Navbar";
import Sidedrawer from "./components/sidedrawer/Sidedrawer";
import Flowsection from "./components/flowsection/Flowsection";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Sidedrawer />
      <Flowsection />
    </div>
  );
}

export default App;
