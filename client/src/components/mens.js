import React, { useState, useEffect } from 'react';

const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('https://fakestoreapi.com/products')
      .then((res) => res.json())
      .then((json) => {
        const filteredProducts = json.filter(
          (product) => product.category === "men's clothing"
        );
        setProducts(filteredProducts);
      })
      .catch((error) => console.error('Error:', error));

    document.cookie = 'key=value; SameSite=Strict';
  }, []);

  return (
    <div>
      <section>
        <div>
          <div>
            {products.map((product) => (
              <Product product={product} key={product.id} />
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
