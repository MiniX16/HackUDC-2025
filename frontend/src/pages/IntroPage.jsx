import React, { useState, useRef, useEffect } from "react";
import UploadImage from "../components/Uploadimage";
import { processImage } from "../services/api";
import "../styles.css";
import foto1 from "../assets/foto1.jpg";
import foto2 from "../assets/foto2.jpg";
import foto3 from "../assets/foto3.jpg";

const images = [foto1, foto2, foto3, foto1, foto2, foto3, foto1, foto2, foto3];

const IntroPage = () => {
  const [selectedImage, setSelectedImage] = useState(null); // Estado para la imagen seleccionada
  const [isManualScroll, setIsManualScroll] = useState([false, false, false]); // Estado para cada fila
  const rowRefs = [useRef(null), useRef(null), useRef(null)]; // Referencias para cada fila

  // Manejar el scroll manual de cada fila
  const handleScroll = (rowIndex) => {
    setIsManualScroll((prev) => {
      const newState = [...prev];
      newState[rowIndex] = true;
      return newState;
    });

    // Limpia el estado después de un breve tiempo para reanudar la animación.
    setTimeout(() => {
      setIsManualScroll((prev) => {
        const newState = [...prev];
        newState[rowIndex] = false;
        return newState;
      });
    }, 1000); // Ajusta el tiempo según sea necesario.
  };

  // Manejar clic en una imagen del fondo
  const handleImageClick = async (imageSrc) => {
    setSelectedImage(imageSrc);
    try {
      const response = await processImage(imageSrc);
      if (response?.image) {
        setSelectedImage(response.image);
      }
    } catch (error) {
      console.error("Error procesando la imagen:", error);
    }
  };

  // Efecto para crear scroll infinito
  useEffect(() => {
    rowRefs.forEach((rowRef, rowIndex) => {
      const row = rowRef.current;
      if (row) {
        const handleScroll = () => {
          if (row.scrollLeft + row.clientWidth >= row.scrollWidth - 100) {
            row.scrollLeft = 0;
          }
        };
        row.addEventListener("scroll", handleScroll);
        return () => row.removeEventListener("scroll", handleScroll);
      }
    });
  }, [rowRefs]);

  return (
    <div className="intro-container">
      <h1 className="logo">INDITEX</h1>
      <div className="background-container">
        {[...Array(3)].map((_, rowIndex) => (
          <div
            key={rowIndex}
            className={`image-row row-${rowIndex + 1}`}
            ref={rowRefs[rowIndex]}
            onScroll={() => handleScroll(rowIndex)}
            style={{
              animationPlayState: isManualScroll[rowIndex] ? "paused" : "running",
            }}
          >
            {images.concat(images).map((src, index) => (
              <img
                key={index}
                src={src}
                alt={`Prenda ${index + 1}`}
                className="moving-image"
                onClick={() => handleImageClick(src)}
              />
            ))}
          </div>
        ))}
      </div>
      <div className="content">
        <UploadImage selectedImage={selectedImage} />
      </div>
    </div>
  );
};

export default IntroPage;