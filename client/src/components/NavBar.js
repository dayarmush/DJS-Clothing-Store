import { NavLink } from "react-router-dom";
import './NavBar.css'

function NavBar() {

  return (
    <div className="navbar">
      <ul>
      <li><NavLink to='/'>Home</NavLink></li>
      <li><NavLink to='/mens'>Men's</NavLink></li>
      <li><NavLink to='/Womens'>Women's</NavLink></li>
      <li><NavLink to='/kids'>Kid's</NavLink></li>
      <li><NavLink to='/login'>👤</NavLink></li>
        </ul>
    </div>
  )
}

export default NavBar
