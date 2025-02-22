import React, { useState, useEffect } from "react";
import { useParams, useLocation } from "react-router-dom";
import { motion } from "framer-motion";
import "../styles/OutfitRecommendation.css";
import { getProducts } from "../services/api";

const OutfitRecommendation = () => {
    const { itemId } = useParams(); // Obtener el ID del producto seleccionado
    const location = useLocation();
    const { product } = location.state || {}; // Recibir la imagen original desde RecomendationPage
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
            <h1 className="title">Outfit Recomendado</h1>
            {product && (
                <div className="selected-product">
                    <motion.img
                        src={product.image}
                        alt={product.name}
                        className="selected-product-image"
                    />
                    <p className="selected-product-name">{product.name}</p>
                    <p className="selected-product-price">{product.price} €</p>
                </div>
            )}
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
