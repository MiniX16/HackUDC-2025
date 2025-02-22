import axios from "axios";

const API_URL = "http://localhost:8000/";


// Enviar imagen en base64 al backend
export const uploadImage = async (base64Image, price) => {
  try {
    const response = await fetch(`${API_URL}api/upload-image/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        price: price , // Enviar el precio
        image_base64: base64Image,
      }),
    });

    
    if (!response.ok) {
      const errorDetails = await response.json(); // Leer mensaje del backend
      console.error("Error en uploadImage:", errorDetails);
      throw new Error(`Error ${response.status}: ${errorDetails.detail}`);
    }
    
    const data = await response.json();


    return data
      .filter(product => {
        try {
          const imageUrl = `data:image/jpeg;base64,${product.image_base64}`;
          // Intentar crear un objeto URL para verificar si es válido
          new URL(imageUrl);
          return true;
        } catch (e) {
          console.error(`Error al convertir la imagen del producto ${product.id}:`, e);
          return false;
        }
      })
      .map(product => ({
        id: product.id,
        name: product.name,
        price: product.price,
        currency: product.currency,
        description: product.description,
        link: product.link,
        brand: product.brand,
        categories: product.categories,
        color: product.color,
        image: `data:image/jpeg;base64,${product.image_base64}`
      }));
  } catch (error) {
    console.error("Error en uploadImage:", error);
    return [];
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

    // Filtrar productos con imágenes válidas y convertir las imágenes base64 a URLs válidas para <img src="...">
    return data
      .filter(product => {
        try {
          const imageUrl = `data:image/jpeg;base64,${product.image_base64}`;
          // Intentar crear un objeto URL para verificar si es válido
          new URL(imageUrl);
          return true;
        } catch (e) {
          console.error(`Error al convertir la imagen del producto ${product.id}:`, e);
          return false;
        }
      })
      .map(product => ({
        id: product.id,
        name: product.name,
        price: product.price,
        currency: product.currency,
        description: product.description,
        link: product.link,
        brand: product.brand,
        categories: product.categories,
        color: product.color,
        image: `data:image/jpeg;base64,${product.image_base64}`
      }));
  } catch (error) {
    console.error("Error en getProducts:", error);
    return [];
  }
};
