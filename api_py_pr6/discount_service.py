def calculate_discount(original_price: float, discount_percentage: float) -> float:
    MIN_PERCENT = 0
    MAX_PERCENT = 100
    DECIMAL_PLACES = 2

    if not (MIN_PERCENT <= discount_percentage <= MAX_PERCENT):
        raise ValueError("Відсоток знижки має бути між 0 і 100.")

    discount_amount = original_price * (discount_percentage / MAX_PERCENT)

    return round(original_price - discount_amount, DECIMAL_PLACES)