import React, { useState, useRef, useEffect } from "react";
import { motion, useScroll, useTransform, useSpring } from "framer-motion";
import "../styles/RecomendationPage.css";
import { getProducts } from "../services/api";
import { useNavigate } from "react-router-dom";

const useParallax = (value, distance) => {
  return useTransform(value, [0, 1], [-distance, distance]);
};

const Image = ({ product }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ container: ref });
  const y = useParallax(scrollYProgress, 100);
  const navigate = useNavigate();

  return (
    <motion.div ref={ref} className="img-container" style={{ y }}>
      <motion.img
        src={product.image}
        alt={product.name}
        className="scroll-image"
        layoutId={`modal-${product.id}`}
      />
      <div className="overlay">
        <a href={product.link} target="_blank" rel="noopener noreferrer" className="product-link">
          <p>{product.name}</p>
        </a>
        <p>{product.price} €</p>
        <p>{product.brand}</p>
        <button className="outfit-button" onClick={() => navigate("/outfit-recommendation/:${selectedImage.id}")}>Crear Outfit</button>
      </div>
    </motion.div>
  );
};

const RecomendationPage = () => {
  const [rowImages, setRowImages] = useState([]);
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({ container: containerRef });
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001,
  });

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const suggestedProducts = await getProducts(20);
        setRowImages(suggestedProducts);
      } catch (error) {
        console.error("Error obteniendo productos:", error);
      }
    };
    fetchProducts();
  }, []);

  return (
    <div id="example" className="scroll-container" ref={containerRef}>
      {rowImages.map((product) => (
        <Image key={product.id} product={product} />
      ))}
      <motion.div className="progress" style={{ scaleX }} />
      
    </div>
  );
};


export default RecomendationPage;
