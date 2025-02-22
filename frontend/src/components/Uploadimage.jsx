import { useState, useEffect } from "react";
import { uploadImage } from "../services/api";
import { convertToBase64 } from "../utils/convertToBase64";
import { useNavigate } from "react-router-dom";
import "../styles.css";

const UploadImage = ({ selectedImage }) => {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [price, setPrice] = useState(""); // Permitir entrada de número
  const navigate = useNavigate();

  useEffect(() => {
    if (selectedImage) {
      setImage(selectedImage);
    }
  }, [selectedImage]);

  const handleImageChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setLoading(true);
      const base64 = await convertToBase64(file);
      setImage(base64);
      console.log(base64);

      const response = await uploadImage(base64);
      setResponse(response);
      setLoading(false);
    }
  };


  const handleUploadAndNavigate = async () => {
    if (!image) {
      alert("Selecciona una imagen antes de continuar.");
      return;
    }
  
    try {
      setLoading(true);
  
      const formattedPrice = price ? parseFloat(price) : 0; // ✅ Convierte price a número o null
    
  
      const response = await uploadImage(image, formattedPrice);
      setResponse(response);
      setLoading(false);
  
      navigate("/recomendation", {state: {response}}); // Redirigir solo si no hay errores
    } catch (error) {
      console.error("Error al subir la imagen:", error);
      setLoading(false);
    }
  };
  
  

  return (
    <div className="upload-container">
      <div className="upload-box">
        <h2 className="title">SUBE TU FOTO</h2>
        <label className="upload-area" htmlFor="upload">
          {loading ? (
            <p>Cargando...</p>
          ) : image ? (
            <img src={image} alt="Preview" className="preview-image" />
          ) : (
            <div className="icon-container">
              <svg
                className="upload-icon"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M12 4v16m8-8H4"
                ></path>
              </svg>
              <span>Haz clic para subir</span>
            </div>
          )}
          <input
            id="upload"
            type="file"
            accept="image/*"
            className="file-input"
            onChange={handleImageChange}
          />
        </label>

        {/* Nuevo Input para escribir el precio */}
        <div className="price-input">
          <label htmlFor="price">Ingrese el precio:</label>
          <input
            id="price"
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            
            min="0"
            
          />
        </div>

       
        {/* Un solo botón para subir la imagen y redirigir */}
        <button className="confirm-button" onClick={handleUploadAndNavigate}>
          Subir Imagen y Continuar
        </button>
              </div>

              {/* Mostrar la imagen procesada desde el backend */}
      {response?.image && (
        <div className="result-container">
          <h3>Imagen procesada:</h3>
          <img src={response.image} alt="Processed" className="preview-image" />
        </div>
      )}
    </div>
  );
};

export default UploadImage;
