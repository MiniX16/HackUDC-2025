import React, { useState, useEffect } from "react";
import {  useLocation } from "react-router-dom";
import { motion } from "framer-motion";
import "../styles/OutfitRecommendation.css";
import { processImage } from "../services/api";

const OutfitRecommendation = () => {
    const location = useLocation();
    const { product } = location.state || {}; // Recibir la imagen original desde RecomendationPage
    const [recommendedItems, setRecommendedItems] = useState([]);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const products = await processImage(product.color, product.categories) // Obtener 10 productos recomendados
                console.log(products)
                setRecommendedItems(products);
            } catch (error) {
                console.error("Error obteniendo recomendaciones:", error);
            }
        };
        
        fetchRecommendations();
    }, []);

    return (
        <div className="outfit-recommendation-container">
            <h1 className="title">Outfit Recomendado</h1>
            
            <div className="product-grid">
                {recommendedItems.map((product, index) => (
                    <div key={product.id || index} className="product-card">
                        <motion.img
                            src={product.image}
                            alt={product.name}
                            className="product-image"
                            layoutId={`recommend-${index}`}
                        />
                        <div className="product-info">
                            <p className="product-name">{product.name}</p>
                            <p className="product-price">{product.price} €</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default OutfitRecommendation;
