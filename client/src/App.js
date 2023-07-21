import Login from './components/Login'
import NavBar from './components/NavBar';
import { useState, useEffect } from 'react';
import HomePage from "./components/HomePage";
import { Routes, Route, Navigate } from 'react-router-dom';
import Signup from './components/Signup';
import NewItem from './components/NewItem';
import ItemDetail from './components/ItemDetail';
import RemoveDetails from './components/RemoveDetails';
import KidItems from "./components/Kids";
import MenItems from "./components/Mens";
import WomenItems from "./components/Womens";
import './components/NavBar.css'
import './components/HomePage.css';

function App() {

  const [user, setUser] = useState([])

  useEffect(() => {
    fetch('/check_session')
    .then(r => r.json())
    .then(data => setUser(data))
  }, [])

  return (
    <div>
      <NavBar/>
      <div>
        <Routes>
          <Route path="/mens" element={<MenItems />} />

          <Route path="/Womens" element={<WomenItems />} />

          <Route path="/Kids" element={<KidItems />} />

          <Route path='/login' element={<Login user={user} setUser={setUser}/>}/>

          <Route path='/signup/*' element={<Signup setUser={setUser}/>}/>

          <Route path='/newItem/*' element={<NewItem/>}/>

          <Route path='items/:id/:where' element={<RemoveDetails setUser={setUser}/>} />

          <Route path='items/:id/' element={<ItemDetail user={user} setUser={setUser}/>}/>

          <Route exact path='/' element={<HomePage/>}/>

          <Route path='*' element={<Navigate to='/' />}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
