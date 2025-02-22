import axios from "axios";

const API_URL = "http://localhost:8000/";


// Enviar imagen en base64 al backend
export const uploadImage = async (base64Image) => {
  try {
    const response = await fetch(`${API_URL}upload-image/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ image: base64Image }),
    });

    if (!response.ok) throw new Error("Error al subir la imagen");

    const data = await response.json();
    return data; // Retorna la respuesta del backend
  } catch (error) {
    console.error("Error en uploadImage:", error);
    return null;
  }
};

// Procesar una imagen ya existente en base64
export const processImage = async () => {
  try {
    const response = await fetch(`${API_URL}recommendations/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      
    });

    if (!response.ok) throw new Error("Error al procesar la imagen");

    const data = await response.json();
    return data; // Retorna la imagen procesada en base64
  } catch (error) {
    console.error("Error en processImage:", error);
    return null;
  }
};
