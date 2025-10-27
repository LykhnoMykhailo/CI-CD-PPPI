def calculate_discount(original_price: float, discount_percent: float) -> float:
    min = 0
    max = 100
    half = 2
    if not (min <= discount_percent <= max):
        # Використовуємо ValueError для недійсних вхідних даних
        raise ValueError("Відсоток знижки має бути між 0 і 100.")

    discount_amount = original_price * (discount_percent / max)
    return round(original_price - discount_amount, half)
