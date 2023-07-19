import { useEffect, useState } from "react";

function Login() {

  const blankLoginForm = {
    'username': '',
    'password': ''
  }

  const [user, setUser] = useState([])
  const [error, setError] = useState([])
  const [info, setInfo] = useState(blankLoginForm)
  
  function handleChange(e) {
    const key = e.target.name
    const value = e.target.value
    setInfo(pre => {
      return { ...pre, [key]: value }
    })
  }

  function handleClick() {
    fetch('/login', {
      method: 'POST', 
      headers: {
      'Content-Type': 'application/json'
      },
      body: JSON.stringify(info)
    })
    .then(r => r.json())
    .then(data => {
      setUser(data)
      setInfo(blankLoginForm)
    })
    .catch(r => setError(r.body))
  }
  
  return ( 
    <div>
      <input 
        type='text' 
        placeholder="Username" 
        value={info.username}
        name='username' 
        onChange={handleChange}
      />

      <input
        type="password"
        placeholder="Password"
        name="password"
        value={info.password}
        onChange={handleChange}
      />

      <button onClick={handleClick}>Login</button>

    </div>
  )
}

export default Login