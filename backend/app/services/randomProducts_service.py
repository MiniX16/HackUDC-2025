import json
import time
import random
from apis.inditex_api import search_products_by_text
from utils.get_img import get_product_image

CLOTHES = ["shirt", "pant", "jacket"]

async def get_random_products(n: int):
    result = []
    for _ in range(n):
        result.append(
            random.choice(search_products_by_text(random.choice(CLOTHES)))
        )
        result[-1]["img"] = await get_product_image(result[-1]["link"])
    print(result)
    return json.dumps(result, indent=4)
