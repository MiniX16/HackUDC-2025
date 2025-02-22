import json
import random

# Cargar dataset
with open("data/output.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

def get_random_products(n: int):
    """Devuelve n productos aleatorios del dataset"""
    if n > len(dataset):
        n = len(dataset)
    return random.sample(dataset, n)
