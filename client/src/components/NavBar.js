import { NavLink } from "react-router-dom";


function NavBar() {

  return (
    <div className="navbar">
      <ul>
        <li><NavLink to='/'>Home</NavLink></li>
        <li><NavLink to='/mens'>Men's</NavLink></li>
        <li><NavLink to='/Womens'>Women's</NavLink></li>
        <li><NavLink to='/Kids'>Kid's</NavLink></li>
        <li><NavLink to='/login'>👤</NavLink></li>
      </ul>
    </div>
  )
}

export default NavBar
