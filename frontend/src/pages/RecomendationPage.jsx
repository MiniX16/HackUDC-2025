import React, { useState, useRef, useEffect } from "react";
import { motion, useScroll, useTransform, useSpring } from "framer-motion";
import "../styles/RecomendationPage.css";
import { processImage } from "../services/api";
import { useNavigate , useLocation } from "react-router-dom";

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
      <a href={product.link} target="_blank" rel="noopener noreferrer">
        <motion.img
          src={product.image}
          alt={product.name}
          className="scroll-image"
          layoutId={`modal-${product.id}`}
        />
      </a>
      <div className="overlay">
        <a href={product.link} target="_blank" rel="noopener noreferrer" className="product-link">
          <p>{product.name}</p>
        </a>
        <p>{product.price} €</p>
        <p>{product.brand}</p>
        <button className="outfit-button" onClick={() => navigate("/outfit-recommendation/", {state: {product}})}>Crear Outfit</button>
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
  const navigate = useNavigate();

  const location = useLocation();
  const { response } = location.state || {};


  useEffect(() => {
    if (response ) {
      setRowImages(response);
    }
  }, [response]);

  return (
    <div id="example" className="scroll-container" ref={containerRef}>
      <h1 className="logo" onClick={() => navigate('/')}>INDEEPTEX</h1>
      {/* Botón de cierre en la esquina superior derecha */}
      <button className="close-button" onClick={() => navigate('/')}>X</button>
      {rowImages.map((product) => (
        <Image key={product.id} product={product} />
      ))}
      <motion.div className="progress" style={{ scaleX }} />
      
    </div>
  );
};


export default RecomendationPage;
