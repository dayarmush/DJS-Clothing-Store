import React from "react";
import ReactDOM from "react-dom";

const { useEffect, useState } = React;

const HomePage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('https://fakestoreapi.com/products')
      .then(res => res.json())
      .then(json => setProducts(json))
      .catch(error => console.error('Error:', error));

    document.cookie = "key=value; SameSite=Strict";
  }, []); 

  if (products.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div id="product-container">
      {products.map((product) => (
        <div key={product.id} className="product">
          <h2>{product.title}</h2>
          <img src={product.image} alt={product.title} />
          <p>{product.description}</p>
        </div>
      ))}
    </div>
  );
};


export default HomePage
