import React, { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion"; // Importamos Framer Motion
import "../styles/RecomendationPage.css"; // Importamos el CSS específico
import foto1 from "../assets/foto1.jpg";
import foto2 from "../assets/foto2.jpg";
import foto3 from "../assets/foto3.jpg";

const initialImages = [
  { src: foto1, name: "Camisa de lino", color: "Beige", url: "#" },
  { src: foto2, name: "Pantalón chino", color: "Negro", url: "#" },
  { src: foto3, name: "Chaqueta de cuero", color: "Marrón", url: "#" },
];

const RecomendationPage = () => {
  const [rowImages, setRowImages] = useState([initialImages, initialImages, initialImages]);
  const [selectedImage, setSelectedImage] = useState(null); // Estado para el modal
  const rowRefs = [useRef(null), useRef(null), useRef(null)];

  // Función para manejar el scroll infinito
  useEffect(() => {
    rowRefs.forEach((rowRef, rowIndex) => {
      const row = rowRef.current;
      if (!row) return;

      const handleScroll = () => {
        if (row.scrollLeft + row.clientWidth >= row.scrollWidth - 100) {
          setRowImages((prev) => {
            const updatedImages = [...prev];
            updatedImages[rowIndex] = [...updatedImages[rowIndex], ...initialImages];
            return updatedImages;
          });
        }
      };

      row.addEventListener("scroll", handleScroll);
      return () => row.removeEventListener("scroll", handleScroll);
    });
  }, [rowRefs]);

  return (
    <div className="recomendation-container">
      <h1 className="logo">INDITEX</h1>

      <div className="rows-container">
        {rowImages.map((images, rowIndex) => (
          <div key={rowIndex} className="image-row" ref={rowRefs[rowIndex]}>
            {images.map((image, index) => (
              <motion.img
                key={index}
                src={image.src}
                alt={image.name}
                className="scroll-image"
                layoutId={`modal-${index}`} // Asignamos un layoutId único
                onClick={() => setSelectedImage(image)} // Abre el modal al hacer clic
              />
            ))}
          </div>
        ))}
      </div>

      {/* Modal con animación */}
      <AnimatePresence>
        {selectedImage && (
          <motion.div
            className="modal-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedImage(null)} // Cerrar modal al hacer clic afuera
          >
            <motion.div
              className="modal-content"
              initial={{ y: 50, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              exit={{ y: 50, opacity: 0 }}
              onClick={(e) => e.stopPropagation()} // Evita que se cierre si se hace clic dentro
            >
              <motion.img
                src={selectedImage.src}
                alt={selectedImage.name}
                className="modal-image"
                layoutId={`modal-${selectedImage.name}`} // Misma animación de layout
              />
              <div className="modal-info">
                <h2>{selectedImage.name}</h2>
                <p>Color: {selectedImage.color}</p>
                <a href={selectedImage.url} target="_blank" rel="noopener noreferrer">
                  Ver en tienda
                </a>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default RecomendationPage;
