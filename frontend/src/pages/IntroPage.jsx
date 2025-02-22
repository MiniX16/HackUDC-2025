import { useState, useEffect, useRef } from "react";
import { motion } from "framer-motion";
import UploadImage from "../components/Uploadimage";
import { getProducts } from "../services/api"; // Importamos la función
import "../styles.css"; // Importamos el CSS específico de esta página

const IntroPage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [rowImages, setRowImages] = useState([[], [], []]); // Estado para almacenar imágenes de cada fila
  const rowRefs = [useRef(null), useRef(null), useRef(null)];

  // Obtener imágenes del backend y actualizar cada fila
  useEffect(() => {
    const fetchImages = async () => {
      try {
        const newImages = await getProducts(5); // Obtener imágenes del backend
        if (newImages.length > 0) {
          const repeatedImages = [...newImages, ...newImages, ...newImages, ...newImages]; // Más repeticiones para asegurar la continuidad
          setRowImages([repeatedImages, repeatedImages, repeatedImages]); // Asignar imágenes a cada fila
        }
      } catch (error) {
        console.error("Error al obtener imágenes:", error);
      }
    };

    fetchImages();
  }, []);

  const handleImageClick = (imageSrc) => {
    setSelectedImage(imageSrc);
  };

  const handleScroll = (event, rowIndex) => {
    if (rowRefs[rowIndex].current) {
      event.preventDefault(); // Evita el scroll vertical al usar la rueda
      rowRefs[rowIndex].current.scrollLeft += event.deltaY * 2; // Ajusta la velocidad del desplazamiento
    }
  };

  return (
    <div className="intro-container">
      <h1 className="logo">INDEEPTEX</h1>
      <div className="background-container">
        {rowImages.map((images, rowIndex) => {
          const scrollDirection = rowIndex === 1 ? "left" : "right";
          return (
            <div
              key={rowIndex}
              className={`image-row row-${rowIndex + 1}`}
              style={{ width: "100%", overflowX: "auto", display: "flex" }}
              ref={rowRefs[rowIndex]}
              onWheel={(event) => handleScroll(event, rowIndex)}
            >
              <motion.div
                className="image-track"
                animate={{ x: scrollDirection === "left" ? ["0%", "-100%"] : ["-100%", "0%"] }}
                transition={{ ease: "linear", duration: 20, repeat: Infinity }}
                style={{ display: "flex", minWidth: "200%" }}
              >
                {images.concat(images).map((product, index) => (
                  <img
                    key={product.id || index}
                    src={product.image}
                    alt={product.name}
                    className="moving-image"
                    onClick={() => handleImageClick(product.image)}
                  />
                ))}
              </motion.div>
            </div>
          );
        })}
      </div>
      <div className="content">
        <UploadImage selectedImage={selectedImage} />
      </div>
    </div>
  );
};

export default IntroPage;
