import pytest
from discount_service import calculate_discount


# Тест 1: Звичайний розрахунок
def test_discount_standard_case():
    # Arrange / Act
    result = calculate_discount(100.0, 10.0)  # 10% від 100 = 10. Результат 90

    # Assert
    assert result == 90.0


# Тест 2: Крайній випадок
def test_discount_negative_input():
    # Assert: Перевіряємо, чи викликається ValueError при від'ємній знижці
    with pytest.raises(ValueError) as e:
        calculate_discount(100.0, -5.0)

    # Можна також перевірити повідомлення про помилку
    assert "між 0 і 100" in str(e.value)


# Тест 3: 100% знижка
def test_discount_full_discount():
    result = calculate_discount(500.0, 100.0)
    assert result == 0.0


# Тест 4: Нульова знижка
def test_discount_zero_discount():
    result = calculate_discount(500.0, 0.0)
    assert result == 500.0