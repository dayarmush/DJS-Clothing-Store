import React, { useState, useEffect } from 'react';
import ItemCard from './ItemCard';
import SlideShow from './SlideShow';

function HomePage() {
  const [items, setItems] = useState([]);

  const images = [
    'https://hornorharrison.com/cdn/shop/files/Home_Banner_Option1_5ed6dd12-9a96-4bcd-8c4d-b15c1c7f8a94.jpg?v=1679054325&width=3840',
    'https://image.made-in-china.com/2f0j00NVlrvIHEfKcJ/Women-Clothing-No-Sexy-Sports-Set-Couple-Men-prime-S-Hoodie-and-Jogger-Set-Hoodies.jpg',
    'https://res.cloudinary.com/jerrick/image/upload/d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,q_auto,w_1024/6229c8f5feade9001f02d97d.png',
  ];

  useEffect(() => {
    fetch('/items')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setItems(data))
      .catch((error) => {
        console.error('Error fetching items:', error);
      });
  }, []);

  return (
    <>
      <h1>Welcome To DJ'S Clothing Store</h1>
        <SlideShow images={images}/>
      <div id="product-container">
        {items.map((item) => (
          <ItemCard className="product" key={item.id} item={item}/>
        ))}
      </div>
    </>
  );
}

export default HomePage;
