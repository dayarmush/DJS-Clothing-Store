import Login from "./Login";
import NavBar from "./NavBar";
import { useState, useEffect } from "react";
import ItemCard from "./ItemCard";
import HomePage from "./homeScreen";
// import kidStuff from "./Kids";
import { Routes, Route, Navigate } from "react-router-dom";

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("/items")
      .then((r) => r.json())
      .then((data) => setItems(data));
  }, []);

  return (
    <div>
      <NavBar />
      <div>
        <Routes>
          <Route path="/mens" element={"mens"} />

          <Route path="/womens" element={"Womens"} />

          <Route path="/kids" element={"kidStuff"} />

          <Route path="/login" element={<Login />} />

          <Route exact path="/" element={<HomePage />} />

          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
