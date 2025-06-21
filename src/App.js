import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";

function App() {
  const [currentString, setCurrentString] = useState("Goodbye");

  useEffect(() => {
    fetch('/hi').then(res => res.json()).then(data => { 
      console.log(data);
      setCurrentString(data.message);
    });
  }, []);
  
  return (
    <h1>{ currentString }</h1>
  );
}

export default App;
