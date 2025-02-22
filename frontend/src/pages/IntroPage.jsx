import { useState, useRef, useEffect } from "react";
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
        const newImages = await getProducts(20); // Obtener 5 imágenes del backend
        if (newImages.length > 0) {
          setRowImages([newImages, newImages, newImages]); // Asignar imágenes a cada fila
        }
      } catch (error) {
        console.error("Error al obtener imágenes:", error);
      }
    };

    fetchImages();
  }, []);

  // Scroll infinito: Agrega más imágenes al llegar al final de la fila
  useEffect(() => {
    rowRefs.forEach((rowRef, rowIndex) => {
      const row = rowRef.current;
      if (!row) return;

      const handleScroll = async () => {
        if (row.scrollLeft + row.clientWidth >= row.scrollWidth - 100) {
          const newImages = await getProducts(20);
          if (newImages.length > 0) {
            setRowImages((prev) => {
              const updatedImages = [...prev];
              updatedImages[rowIndex] = [...updatedImages[rowIndex], ...newImages]; // Agregar nuevas imágenes
              return updatedImages;
            });
          }
        }
      };

      row.addEventListener("scroll", handleScroll);
      return () => row.removeEventListener("scroll", handleScroll);
    });
  }, [rowRefs]);

  const handleImageClick = (imageSrc) => {
    setSelectedImage(imageSrc);
  };

  return (
    <div className="intro-container">
      <h1 className="logo">INDEEPTEX</h1>
      <div className="background-container">
        {rowImages.map((images, rowIndex) => (
          <div key={rowIndex} className={`image-row row-${rowIndex + 1}`} ref={rowRefs[rowIndex]}>
            {images.map((product, index) => (
              <img
                key={product.id || index}
                src={product.image}
                alt={product.name}
                className="moving-image"
                onClick={() => handleImageClick(product.image)}
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
