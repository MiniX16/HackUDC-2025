import React, { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { motion, useScroll, useTransform, useSpring } from "framer-motion";
import "../styles/RecomendationPage.css";
import { getProducts } from "../services/api";

const useParallax = (value, distance) => {
  return useTransform(value, [0, 1], [-distance, distance]);
};

const Image = ({ product }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ container: ref });
  const y = useParallax(scrollYProgress, 100);

  return (
    <motion.div ref={ref} className="img-container" style={{ y }}>
      <motion.img
        src={product.image}
        alt={product.name}
        className="scroll-image"
        layoutId={`modal-${product.id}`}
      />
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
      <StyleSheet />
    </div>
  );
};

function StyleSheet() {
  return (
    <style>{`
        html, body {
            height: 100%;
            overflow: hidden;
            scroll-behavior: smooth;
        }

        .scroll-container {
            height: 100vh;
            overflow-y: auto;
            scroll-snap-type: y mandatory;
        }

        .img-container {
            height: 100vh;
            scroll-snap-align: start;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .img-container img {
            width: 300px;
            height: 400px;
        }

        @media (max-width: 500px) {
            .img-container img {
                width: 150px;
                height: 200px;
            }
        }

        .progress {
            position: fixed;
            left: 0;
            right: 0;
            height: 5px;
            background: #000000;
            bottom: 50px;
            transform-origin: left;
        }
    `}</style>
  );
}

export default RecomendationPage;
