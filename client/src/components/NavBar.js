import { NavLink } from "react-router-dom";

function NavBar() {

  return (
    <div>
      <NavLink to='/'>Home</NavLink>
      <NavLink to='/mens'>Men's</NavLink>
      <NavLink to='/Womens'>Women's</NavLink>
      <NavLink to='/kids'>Kid's</NavLink>
      <NavLink to='/login'>👤</NavLink>
    </div>
  )
}

export default NavBar