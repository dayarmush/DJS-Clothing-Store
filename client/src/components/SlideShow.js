import { useState, useEffect} from 'react'

function SlideShow({ images }) {
    const [currentSlide, setCurrentSlide] = useState(0);
  
    useEffect(() => {
      const interval = setInterval(() => {
        setCurrentSlide((prevSlide) =>
          prevSlide === images.length - 1 ? 0 : prevSlide + 1
        );
      }, 5000);
  
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

  export default SlideShow