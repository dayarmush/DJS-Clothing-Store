import { useParams } from "react-router-dom"
import { useState, useEffect } from 'react'

function RemoveDetails({ user }) {

  const params = useParams()

  const [item, setItem] = useState([])
  const [error, setError] = useState([])
  const [message, setMessage] = useState('')
console.log(params.where)
  useEffect(() => {
    fetch(`/items/${params.id}`)
    .then(r => {
      if (r.ok) {
        r.json().then(data => setItem(data))
      } else {
        r.json().then(err => setError(err))
      }
    })
  }, [])

  function removeCart() {
    fetch(`/carts/${params.where}`, {
      method: 'DELETE'
    })
    .then(r => {
      if (r.ok) {
        r.json().then(setMessage('Item Removed From Cart'))
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  function removeFave() {
    fetch(`/favorites/${params.where}`, {
      method: 'DELETE'
    })
    .then(r => {
      if (r.ok) {
        r.json().then(setMessage('Item Removed From Faves'))
      } else {
        r.json().then(err => setError(err))
      }
    })
  }


  return (
      <div>
      <h2>{item.name}</h2>
      <img src={item.image}/>
      <h5>${item.price}</h5>
      {item.reviews &&
          item.reviews.map(review => {
            return (
              <div key={review.id}>
                <h2>Rating: {review.rating}</h2>
                <p>Review: {review.text}</p>
                <p>User: {review.user.username}</p>
              </div>
            )
          })
      }

      <h3>{error.error ? error.error : message}</h3>
      <button onClick={removeCart}>Remove From Cart</button>
      <button onClick={removeFave}>Remove From Favorites</button>
  </div>
  )
}

export default RemoveDetails