import { useState } from "react";
import "./UploadImage.css"; // Importamos los estilos CSS

const UploadImage = () => {
  const [image, setImage] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
  };

  return (
    <div className="container">
      <div className="upload-box">
        <h2 className="title">SUBE TU FOTO</h2>
        <label className="upload-area" htmlFor="upload">
          {image ? (
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
    </div>
  );
};

export default UploadImage;
