def apply_increase(price_product: float) -> float:
    """Aplica un aumento del 5% a un precio.

    Args:
        price_product (float): El precio al cual se le aplicara el aumento.

    Returns:
        float: El precio mas el aumento del 5%.
    """
    if isinstance(price_product, float):

        increase = 5

        result = price_product + (price_product * increase) / 100

        return result
    
