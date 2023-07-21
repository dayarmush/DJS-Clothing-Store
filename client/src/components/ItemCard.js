import React from 'react';
import { Link } from 'react-router-dom';

function ItemCard({ item, where, what }) {
  const { id, name, image, price, category } = item;

  return (
    <Link to={where ? `/items/${id}/${where}` : `/items/${id}`} className="product">
      <div>
        <h2>{what}</h2>
        <h3>{category}</h3>
        <h2>{name}</h2>
        <img src={image} alt={name} />
        <h3>${price}</h3>
      </div>
    </Link>
  );
}

export default ItemCard;

