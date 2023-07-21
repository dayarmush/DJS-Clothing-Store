import React, { useState, useEffect } from 'react';
import ItemCard from './ItemCard';
import SlideShow from './SlideShow';

function WomenItems() {
  const [items, setItems] = useState([]);

  const images = [
    'https://clothesmentor.com/cdn/shop/files/ClothesMentor_SpringFashion_ShopOnline2.jpg?v=1676580892&width=1500',
    'https://www.hawtcelebs.com/wp-content/uploads/2021/08/kaia-gerber-for-vogue-magazine-september-2021-1.jpg'
  ];

  useEffect(() => {
    fetch('/items/womens')
      .then((response) => response.json())
      .then((data) => setItems(data))
      .catch((error) => {
        console.error('Error fetching items:', error);
      });
  }, []);

  return (
    <>
      <SlideShow images={images}/>
      <div id="product-container">
        {items.map((item) => {
            return (
              <ItemCard
                className="product"
                key={item.id}
                item={item}
              />
            );
        })}
      </div>
    </>
  );
  }

export default WomenItems;

