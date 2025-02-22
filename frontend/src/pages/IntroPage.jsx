import { useState, useRef } from "react";
import { motion, useScroll, useMotionValue, useMotionValueEvent, animate } from "framer-motion";
import UploadImage from "../components/UploadImage";
import "../styles.css";

// Importamos imágenes desde la carpeta assets
import foto1 from "../assets/foto1.jpg";
import foto2 from "../assets/foto2.jpg";
import foto3 from "../assets/foto3.jpg";

// Arreglo de imágenes repetidas para el fondo
const images = [foto1, foto2, foto3, foto1, foto2, foto3, foto1, foto2, foto3];

const IntroPage = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const rowRefs = useRef([]);

  function useScrollOverflowMask(scrollXProgress) {
    const maskImage = useMotionValue(
      `linear-gradient(90deg, #000, #000 0%, #000 80%, #0000)`
    );

    useMotionValueEvent(scrollXProgress, "change", (value) => {
      if (value === 0) {
        animate(maskImage, `linear-gradient(90deg, #000, #000 0%, #000 80%, #0000)`);
      } else if (value === 1) {
        animate(maskImage, `linear-gradient(90deg, #0000, #000 20%, #000 100%, #000)`);
      } else {
        animate(maskImage, `linear-gradient(90deg, #0000, #000 20%, #000 80%, #0000)`);
      }
    });

    return maskImage;
  }

  return (
    <div className="intro-container">
      {/* Logo superpuesto estilo Zara */}
      <h1 className="logo">INDITEX</h1>

      {/* Fondo animado con filas de imágenes */}
      <div className="background-container">
        {[...Array(3)].map((_, rowIndex) => {
          const { scrollXProgress } = useScroll({ container: rowRefs.current[rowIndex] });
          const maskImage = useScrollOverflowMask(scrollXProgress);

          return (
            <motion.div
              key={rowIndex}
              ref={(el) => (rowRefs.current[rowIndex] = el)}
              className={`image-row row-${rowIndex + 1}`}
              style={{ maskImage }}
              drag="x"
              dragConstraints={{ left: -500, right: 0 }}
              whileTap={{ cursor: "grabbing" }}
              onDragStart={(e) => {
                e.currentTarget.style.animationPlayState = "paused"; // Pausar animación al arrastrar
              }}
              onDragEnd={(e) => {
                e.currentTarget.style.animationPlayState = "running"; // Reanudar animación al soltar
              }}
            >
              {images.map((src, index) => (
                <motion.img
                  key={index}
                  src={src}
                  alt={`Prenda ${index + 1}`}
                  className="moving-image"
                  onClick={() => setSelectedImage(src)}
                />
              ))}
            </motion.div>
          );
        })}
      </div>

      {/* Formulario de subida de imágenes */}
      <div className="content">
        <UploadImage selectedImage={selectedImage} />
      </div>
    </div>
  );
};

export default IntroPage;
