import React, { useState, useEffect } from 'react';
import ItemCard from './ItemCard';

function Slideshow() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const images = [
    'https://media1.popsugar-assets.com/files/thumbor/Vl8siWdewF18bkglNsc_fMJ7oGA/0x0:2875x1342/fit-in/1048x489/filters:format_auto-!!-:strip_icc-!!-/2021/11/12/659/n/1922564/c99eb59e618e7ef94c8511.80465920_.jpg',
    'https://www.usatoday.com/gcdn/presto/2022/07/22/USAT/66195ac0-9e1f-4e4b-8c7f-5234d7dcf909-back-to-school-outfit-Hanna-Andersson.png',
    'https://akns-images.eonline.com/eol_images/Entire_Site/202275/rs_1024x759-220805095514-1024-ecomm-Back_to_School_Sales-gj.jpg?fit=around%7C1024:759&output-quality=90&crop=1024:759;center,top',
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prevSlide) =>
        prevSlide === images.length - 1 ? 0 : prevSlide + 1
      );
    }, 4000);

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

function KidItems() {
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
          <h1>Kids Department</h1>
          <Slideshow />
          <div id="product-container">
            {items.map((item) => {
              if (item.category === 'kids') {
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

export default KidItems;