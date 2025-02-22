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
      body: JSON.stringify({ 
        image: base64Image,
        price: price || null // Enviar el precio
      }),
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

export const getProducts = async (i) => {
  try {
    const response = await fetch(`${API_URL}api/random-products/?n=${i}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) throw new Error("Error al obtener los productos");

    const data = await response.json();

    // Convertimos las imágenes base64 a URLs válidas para <img src="...">
    return data.map(product => ({
      id: product.id,
      name: product.name,
      price: product.price.value.current,
      link: product.link,
      brand: product.brand,
      categories: product.categories,
      color: product.color,
      image: `data:image/jpeg;base64,${product.image_base64}`}));
  } catch (error) {
    console.error("Error en getProducts:", error);
    return [];
  }
};
