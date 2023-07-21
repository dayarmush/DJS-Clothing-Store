import { useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'

function ItemDetail({ user, setUser }) {

  const params = useParams()
  const [item, setItem] = useState([])
  const [error, setError] = useState([])
  const [message, setMessage] = useState('')
  const [hasForm, setHasForm] = useState(false)
  const [form, setForm] = useState({
    "text": '',
    "rating": '',
  })

  useEffect(() => {
    fetch(`/items/${params.id}`)
    .then(r => {
      if (r.ok) {
        r.json().then(data => setItem(data))
      } else {
        r.json().then(err => setError(err))
      }
    })
  }, [params.id])

  function addCart() {
    if (!user) return <h3>Please sign in</h3>
    fetch('/carts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "user_id": user.id,
        "item_id": params.id
      })
    })
    .then(r => {
      if (r.ok) {
        r.json().then(data => {
          setMessage('Added to Cart');
          setUser(pre => {
            const newCarts = [...pre.carts, data]
            return {...pre, carts: newCarts}
          })
        })
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  function addFave() {
    if (!user) return <h3>Please sign in</h3>
    fetch('/favorites', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "user_id": user.id,
        "item_id": params.id
      })
    })
    .then(r => {
      if (r.ok) {
        r.json().then(data => {
          setMessage('Added to Favorites')
          setUser(pre => {
            const newFave = [...pre.favorites, data]
            return {...pre, favorites: newFave}
          })
        })
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  function review() {
    if (!user) return <h3>Please sign in</h3>
    setHasForm(pre => !pre)
  }

  function handleChange(e) {
    const key = e.target.name
    const value = e.target.value
    setForm(pre => {
      return {...pre, [key]: value}
    })
  }

  function handleSubmit(e) {
    e.preventDefault()

    fetch('/reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "text": form.text,
        "rating": form.rating,
        "user_id": user.id,
        "item_id": params.id
      })
    })
    .then(r => {
      if (r.ok) {
        r.json().then(data => {
          setHasForm(pre => !pre)
          setMessage('Review Added')
          setUser(pre => {
            const newReview = [...pre.reviews, data]
            return {...pre, reviews: newReview}
          })
        })
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  return (
    <div Id='login'>
      <h2>{item.name}</h2>
      <img src={item.image} alt={item.name}/>
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
      <button onClick={addCart}>Add to Cart</button>
      <button onClick={addFave}>Add to Favorites</button>
      <button onClick={review}>Review</button>

      {hasForm && 
        <form onSubmit={handleSubmit}>
          <input
            placeholder='Rating'
            type='number'
            name='rating'
            min='1'
            max='5'
            style={{ width: '15%' }} // Set the width to 100%
            value={form.rating}
            onChange={handleChange}
          />

          <input
            placeholder='Review'
            type='text'
            name='text'
            value={form.text}
            onChange={handleChange}
          />
          <button>Submit</button>
        </form>
      }
    </div>
  )
}

export default ItemDetail