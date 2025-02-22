import { useState, useEffect } from "react"; 
import { uploadImage, processImage } from "../services/api"; //  funciones de la API
import { convertToBase64 } from "../utils/convertToBase64"; // Función para convertir la imagen a base64
import "../styles.css";

// Componente para subir una imagen y mostrarla
const UploadImage = ({ selectedImage }) => {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  // Procesar la imagen seleccionada
  useEffect(() => {
    if (selectedImage) {
      handleProcessImage(selectedImage);
    }
  }, [selectedImage]);

  // Manejar el cambio y envio de la imagen al backend
  const handleImageChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setLoading(true);
      const base64 = await convertToBase64(file); // Convertimos la imagen a base64
      setImage(base64);

      const response = await uploadImage(base64); // Enviamos la imagen al backend
      setResponse(response);
      setLoading(false);
    }
  };

  // Procesar la imagen del backend
  const handleProcessImage = async (imageBase64) => {
    setLoading(true);
    const response = await processImage(imageBase64); // Enviamos la imagen base64 al backend
    setResponse(response);
    setLoading(false);
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
