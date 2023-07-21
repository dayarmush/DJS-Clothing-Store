// import { Link } from 'react-router-dom'
// import {useState} from 'react'


// function ItemCard({ item, where }) {

//   const {id, name, image, price, reviews, category} = item

//   return (
//     <Link to={where ? `/items/${id}/${where}` : `/items/${id}`} id="product-container">
//       <div className="product">
//         <>
//         <h2>{category}</h2>
//         <h1>{name}</h1>
//         <img src={image} alt={name}/>
//         <h2>${price}</h2>
//           {/* {reviews.map(rev => <h3>{rev}</h3>)} */}
//           </>
//       </div>
//     </Link>
    
//   )
// }

// export default ItemCard

import React from 'react';
import { Link } from 'react-router-dom';

function ItemCard({ item, where }) {
  const { id, name, image, price, category } = item;

  return (
    <Link to={where ? `/items/${id}/${where}` : `/items/${id}`} className="product">
      <div>
        <h3>{category}</h3>
        <h2>{name}</h2>
        <img src={image} alt={name} />
        <h3>${price}</h3>
      </div>
    </Link>
  );
}

export default ItemCard;

