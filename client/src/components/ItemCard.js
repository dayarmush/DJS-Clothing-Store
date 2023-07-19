function ItemCard({item}) {
  const {name, image, price, reviews, category} = item


  return (
    <div>
      <h2>{category}</h2>
      <h1>{name}</h1>
      <img src={image} alt={name}/>
      <h2>{price}</h2>
      {/* {reviews.map(rev => <h3>{rev}</h3>)} */}
    </div>
  )
}

export default ItemCard

// import React, { useEffect, useState } from "react";

// const ProductList = () => {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     fetch('https://fakestoreapi.com/products')
//       .then(res => res.json())
//       .then(json => setProducts(json))
//       .catch(error => console.error('Error:', error));

//     document.cookie = "key=value; SameSite=Strict";
//   }, []); 

//   if (products.length === 0) {
//     return <div>Loading...</div>;
//   }

//   return (
//     <div id="product-container">
//       {products.map((product) => (
//         <div key={product.id} className="product">
//           <h2>{product.title}</h2>
//           <img src={product.image} alt={product.title} />
//           <p>{product.description}</p>
//         </div>
//       ))}
//     </div>
//   );
// };

// export default ProductList;
