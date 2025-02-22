import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { motion } from "framer-motion";
import "../styles/OutfitRecommendation.css";
import { getProducts } from "../services/api";

const OutfitRecommendation = () => {
    const { itemId } = useParams(); // Obtener el ID del producto seleccionado
    const [recommendedItems, setRecommendedItems] = useState([]);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const products = await getProducts(10); // Obtener 10 productos recomendados
                setRecommendedItems(products);
            } catch (error) {
                console.error("Error obteniendo recomendaciones:", error);
            }
        };
        
        fetchRecommendations();
    }, [itemId]);

    return (
        <div className="outfit-recommendation-container">
            <h1>Outfit Recomendado</h1>
            <div className="rows-container">
                <div className="image-row">
                    {recommendedItems.map((product, index) => (
                        <motion.img
                            key={product.id || index}
                            src={product.image}
                            alt={product.name}
                            className="scroll-image"
                            layoutId={`recommend-${index}`}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default OutfitRecommendation;
