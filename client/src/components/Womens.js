import React, { useState, useEffect } from 'react';
import './women.css';


function Slideshow() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const images = [
    'https://assets.vogue.com/photos/61e9c42f201fe8db0bc39899/4:3/w_900,h_675,c_limit/00_promo.jpg',
    'https://i.insider.com/54fdc12decad042920ceb0c8?width=800&format=jpeg',
    'https://media.istockphoto.com/id/1293366109/photo/this-one-match-perfect-with-me.jpg?s=612x612&w=0&k=20&c=wJ6yYbRrDfdmoViuQkX39s2z_0lCiNQYgEtLU--0EbY=',
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prevSlide) =>
        prevSlide === images.length - 1 ? 0 : prevSlide + 1
      );
    }, 3000);

    return () => {
      clearInterval(interval);
    };
  }, [images.length]);

  return (
    <div className="slideshow-container">
      <img src={images[currentSlide]} alt={`Slide ${currentSlide + 1}`} />
      <div className="dot-container">
        {images.map((_, index) => (
          <span
            key={index}
            className={currentSlide === index ? 'active' : ''}
            onClick={() => setCurrentSlide(index)}
          ></span>
        ))}
      </div>
    </div>
  );
}

function WomenItems() {
    const [items, setItems] = useState([]);
  
    useEffect(() => {
      fetch('/items')
        .then((response) => response.json())
        .then((data) => setItems(data))
        .catch((error) => {
          console.error('Error fetching items:', error);
        });
    }, []);
  
  return (
    <>
    <h1>Women's Department</h1>
    <Slideshow />
      <div>
        {items.map((item) => {
          if (item.category === "Women's") {
            return (
              <div key={item.id}>
                <img src={item.image} alt={item.name} />
                <p>{item.name}</p>
                <p>{"$"}{item.price}</p>
              </div>
            );
          }
          return null;
        })}
      </div>
      </>
    );
  }

export default WomenItems;