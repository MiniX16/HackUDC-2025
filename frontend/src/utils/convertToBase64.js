export const convertToBase64 = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file); // Convierte la imagen a base64
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });
};
