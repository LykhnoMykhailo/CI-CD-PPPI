def calculate_discount(original_price: float, discount_percent: float) -> float:
    if not (0 <= discount_percent <= 100):
        # Використовуємо ValueError для недійсних вхідних даних
        raise ValueError("Відсоток знижки має бути між 0 і 100.")

    discount_amount = original_price * (discount_percent / 100.0)
    return round(original_price - discount_amount, 2)