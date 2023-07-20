import Login from './components/Login'
import NavBar from './components/NavBar';
import { useState, useEffect } from 'react';
import ItemCard from './components/ItemCard';
import HomePage from './components/HomeScreen'
import { Routes, Route, Navigate } from 'react-router-dom';
import Signup from './components/Signup';
import NewItem from './components/NewItem';
import ItemDetail from './components/ItemDetail';


function App() {

  const [user, setUser] = useState([])
  const [items, setItems] = useState([])

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
          <Route path="/mens" element={'mens'}/>

          <Route path="/womens" element={'Womens'}/>

          <Route path="/kids" element={'Kids'}/>

          <Route path='/login' element={<Login user={user} setUser={setUser}/>}/>

          <Route path='/signup/*' element={<Signup setUser={setUser}/>}/>

          <Route path='/newItem/*' element={<NewItem/>}/>

          <Route path='items/:id/:where' element={'where'} />

          <Route path='items/:id/' element={<ItemDetail user={user}/>}/>

          <Route exact path='/' element={<HomePage/>}/>

          <Route path='*' element={<Navigate to='/' />}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
