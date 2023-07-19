import Login from './components/Login'
import NavBar from './components/NavBar';
import { useState, useEffect } from 'react';
import ItemCard from './components/ItemCard';
import HomePage from './components/HomeScreen'
import { Routes, Route, Navigate } from 'react-router-dom';


function App() {

  const [items, setItems] = useState([])

  useEffect(() => {
    fetch('/items')
    .then(r => r.json())
    .then(data => setItems(data))
  }, [])

  return (
    <div>
      <NavBar/>
      <div>
        <Routes>
          <Route path="/mens" element={'mens'}/>

          <Route path="/womens" element={'Womens'}/>

          <Route path="/kids" element={'Kids'}/>

          <Route path='/login' element={<Login/>}/>

          <Route exact path='/' element={<HomePage/>}/>

          <Route path='*' element={<Navigate to='/' />}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
