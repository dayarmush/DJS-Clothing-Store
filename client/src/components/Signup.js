import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Signup({ setUser }) {

  const blankSignupForm = {
    'username': '',
    'password': ''
  }

  const [error, setError] = useState([])
  const [form, setForm] = useState(blankSignupForm)

  const navigate = useNavigate()

  function handleSubmit(e) {
    e.preventDefault()

    fetch('/signup', {
      method: 'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify(form)
    })
    .then(r => {
      if (r.ok) {
        r.json()
        .then(data => {
          setUser(data)
          setForm(blankSignupForm)
          navigate('/login')
        })
      } else {
        r.json().then(err => setError(err))
      }
    })
  }

  function handleChange(e) {
    const key = e.target.name
    const value = e.target.value
    setForm(pre => {
      return {...pre, [key]: value}
    })
  }

  return (
    <div className='login'>
      <form onSubmit={handleSubmit}>
        <input
          className="loginInfo"
          placeholder="Username"
          type="text"
          name="username"
          value={form.username}
          onChange={handleChange}
        />

        <input
          className="loginInfo"
          placeholder="Password"
          type="password"
          value={form.password}
          name="password"
          onChange={handleChange}
        />

        <button className="loginInfo">Signup</button>
      </form>

      {error.error &&
        <h2>{error.error}</h2>
      }
    </div>
  )
}

export default Signup
