import { useState } from "react"
import { useNavigate } from "react-router-dom"

function NewItem() {

  const blankForm = {
    'name': '',
    'image': '',
    'price': 0,
    'category': ''
  }

  const [error, setError] = useState([])
  const [form, setForm] = useState(blankForm)

  const navigate = useNavigate()

  function handleChange(e) {
    const key = e.target.name
    const value = e.target.value
    setForm(pre => {
      return {...pre, [key]: value}
    })
  }

  function handleSubmit(e) {
    e.preventDefault()

    fetch('/items', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form)
    })
    .then(r => {
      if (r.ok) {
        r.json()
        .then(data => navigate(`/${data.category}`))
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  return (
    <form onSubmit={handleSubmit} > 
      <input
        name="name"
        placeholder="Item Name"
        type="text"
        value={form.name}
        onChange={handleChange}
      />
      
      <input
        name="image"
        placeholder="Item Image"
        type="text"
        value={form.image}
        onChange={handleChange}
      />

      <input
        name="price"
        placeholder="Item Price"
        type="number"
        value={form.price}
        onChange={handleChange}
      />

      <input
        name="category"
        placeholder="Item Category"
        type="text"
        value={form.category}
        onChange={handleChange}
      />
      <button>Add Item</button>
      {error.error && <h2>{error.error}</h2>}
    </form>
  )

}

export default NewItem