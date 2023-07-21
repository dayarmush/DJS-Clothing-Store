import React, { useState, useEffect } from 'react'
import ItemCard from './ItemCard';
import SlideShow from './SlideShow';

function MenItems() {
  const [items, setItems] = useState([]);

  const images = [
    'https://assets.vogue.com/photos/61e9c42f201fe8db0bc39899/4:3/w_900,h_675,c_limit/00_promo.jpg',
    'https://i.insider.com/54fdc12decad042920ceb0c8?width=800&format=jpeg',
    'https://media.istockphoto.com/id/1293366109/photo/this-one-match-perfect-with-me.jpg?s=612x612&w=0&k=20&c=wJ6yYbRrDfdmoViuQkX39s2z_0lCiNQYgEtLU--0EbY=',
  ];

  useEffect(() => {
    fetch('/items/mens')
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
          }
        )}
      </div>
    </>
  );
}

export default MenItems;