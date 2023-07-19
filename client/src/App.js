import { useState, useEffect } from 'react';
import ItemCard from './components/ItemCard';
import { Routes, Route, Navigate } from 'react-router-dom';


function App() {

  const [items, setItems] = useState([])

  useEffect(() => {
    fetch('/items')
    .then(r => r.json())
    .then(data => setItems(data))
  }, [])

  


  return (
    <>
     {items.map(item => {
    return <ItemCard item={item}/>
  })}
    </>
   
  );
}

export default App;
