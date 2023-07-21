import React, { useState, useEffect } from 'react';
import ItemCard from './ItemCard';
// import './women.css';

function Slideshow() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const images = [
    'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/newscms/2017_09/1198835/sp17_nwmn_on_location_dumbo_01_219_f1c.jpg',
    'https://clothesmentor.com/cdn/shop/files/ClothesMentor_SpringFashion_ShopOnline2.jpg?v=1676580892&width=1500',
    'https://advancelocal-adapter-image-uploads.s3.amazonaws.com/image.al.com/home/bama-media/width2048/img/spotnews/photo/prompaloozajpg-d94fffb07d117162.jpg',
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
      <div id="product-container">
        {items.map((item) => {
          if (item.category === "Women's") {
            return (
              <ItemCard
                className="product"
                key={item.id}
                item={item}
                where=""
              />
            );
          }
          return null;
        })}
      </div>
    </>
  );
  }

export default WomenItems;

