import { useState } from "react";
import ItemCard from './ItemCard';
import { NavLink } from 'react-router-dom'

function Login({ user, setUser }) {

  const blankLoginForm = {
    'username': '',
    'password': ''
  }

  const [error, setError] = useState([])
  const [info, setInfo] = useState(blankLoginForm)
  // const [message, setMessage] = useState('')
  
  function handleChange(e) {
    const key = e.target.name
    const value = e.target.value
    setInfo(pre => {
      return { ...pre, [key]: value }
    })
  }

  function HandleLogout() {
    fetch('/logout', {
      method: 'DELETE',
    })
    .then(setUser([]))
  }

  function handleLogin() {
    fetch('/login', {
      method: 'POST', 
      headers: {
      'Content-Type': 'application/json'
      },
      body: JSON.stringify(info)
    })
    .then(r => {
      if (r.ok) {
        r.json()
        .then(data => {
          setUser(data)
          setInfo(blankLoginForm)
        })
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  function deleteReview(id) {
    fetch(`/reviews/${id}`, {
      method: 'DELETE'
    })
    .then(r => {
      if (r.ok) {
        r.json().then(
          fetch('/check_session')
          .then(r => r.json())
          .then(data => setUser(data))
        )
      } else {
        r.json().then(err => setError(err))
      }
    })
  }
  
  return (
    <div Id='login'>
      {!user.username && 
        <div>
          <input 
            className="loginInfo"
            type='text' 
            placeholder="Username" 
            value={info.username}
            name='username' 
            onChange={handleChange}
          />
          <input
            className="loginInfo"
            type="password"
            placeholder="Password"
            name="password"
            value={info.password}
            onChange={handleChange}
          />
          <button onClick={handleLogin}>Login</button>
          {error.error && <h1>{error.error}</h1>}

          <NavLink to='/signup'>Signup</NavLink>

        </div>
      }

      {user.username && 
        <div>
          <h1>Welcome {user.username}</h1>

          {user.carts && 
            <h2>Cart</h2> &&
            user.carts.map(item => {
              return <ItemCard key={item.id} item={item.item} where={item.id}/>
            })
          }

          {user.favorites &&
            <h2>Favorites</h2> &&
            user.favorites.map(item => {
              return <ItemCard key={item.id} item={item.item} where={item.id}/>
            })
          }

          {user.reviews &&
            <h2>Reviews</h2> &&
            user.reviews.map(review => {
              return (
                <div key={review.id}>
                  <h3>Rating: {review.rating}</h3>
                  <p>Review: {review.text}</p>
                  <p>Item: {review.item.name}</p>
                  <button onClick={() => deleteReview(review.id)}>Delete</button>
                </div>
              )
            })
          }

          {user.admin && 
            <NavLink to='/newItem'>Add New Item</NavLink>
          }

          <button onClick={HandleLogout}>Logout</button>
        </div>
      }
    </div>
    
  )
}

export default Login