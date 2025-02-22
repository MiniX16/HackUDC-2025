import React, { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion"; // Importamos Framer Motion
import "../styles/RecomendationPage.css"; // Importamos el CSS específico
import { getProducts } from "../services/api"; // Importamos la función de la API
/*
import foto1 from "../assets/foto1.jpg";
import foto2 from "../assets/foto2.jpg";
import foto3 from "../assets/foto3.jpg";

const initialImages = [
  { src: foto1, name: "Camisa de lino", color: "Beige", url: "#" },
  { src: foto2, name: "Pantalón chino", color: "Negro", url: "#" },
  { src: foto3, name: "Chaqueta de cuero", color: "Marrón", url: "#" },
];
*/

const RecomendationPage = () => {
    const [rowImages, setRowImages] = useState([[], [], []]); // Inicialmente vacío
    const [selectedImage, setSelectedImage] = useState(null);
    const rowRefs = [useRef(null), useRef(null), useRef(null)];
  
    // Obtener productos sugeridos al cargar la página
    useEffect(() => {
      const fetchProducts = async () => {
        try {
          const suggestedProducts = await getProducts(20); // Llama a la API para obtener 20 productos
          if (suggestedProducts.length > 0) {
            setRowImages([suggestedProducts, suggestedProducts, suggestedProducts]); // Rellena las filas
          }
        } catch (error) {
          console.error("Error obteniendo productos:", error);
        }
      };
  
      fetchProducts();
    }, []);
  
    // Scroll infinito para cargar más productos cuando se llegue al final de la fila
    useEffect(() => {
      rowRefs.forEach((rowRef, rowIndex) => {
        const row = rowRef.current;
        if (!row) return;
  
        const handleScroll = async () => {
          if (row.scrollLeft + row.clientWidth >= row.scrollWidth - 100) {
            const newProducts = await getProducts(10); // Obtiene 10 productos adicionales
            if (newProducts.length > 0) {
              setRowImages((prev) => {
                const updatedImages = [...prev];
                updatedImages[rowIndex] = [...updatedImages[rowIndex], ...newProducts];
                return updatedImages;
              });
            }
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
              {images.map((product, index) => (
                <motion.img
                  key={product.id || index}
                  src={product.image}
                  alt={product.name}
                  className="scroll-image"
                  layoutId={`modal-${index}`}
                  onClick={() => setSelectedImage(product)}
                />
              ))}
            </div>
          ))}
        </div>
  
        <AnimatePresence>
          {selectedImage && (
            <motion.div
              className="modal-overlay"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setSelectedImage(null)}
            >
              <motion.div
                className="modal-content"
                initial={{ y: 50, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                exit={{ y: 50, opacity: 0 }}
                onClick={(e) => e.stopPropagation()}
              >
                <motion.img
                  src={selectedImage.image}
                  alt={selectedImage.name}
                  className="modal-image"
                  layoutId={`modal-${selectedImage.name}`}
                />
                <div className="modal-info">
                  <h2>{selectedImage.name}</h2>
                  <p>Color: {selectedImage.color}</p>
                  <a href={selectedImage.link} target="_blank" rel="noopener noreferrer">
                    Ver en tienda
                  </a>
                  <button className="recommend-button" onClick={() => navigate(`/outfit-recommendation`)}>
                    RECOMIÉNDAME UN OUTFIT CON ESTO
                  </button>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    );
  };
  
  export default RecomendationPage;
