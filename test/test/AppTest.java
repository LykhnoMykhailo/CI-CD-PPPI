import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

// Імпортувати клас App не потрібно, якщо вони знаходяться у різних "кореневих" папках (src і test), 
// але в одному проєкті VS Code сам їх знайде.
public class AppTest {

    @Test
    void additionTest() {
        // 1. Створення екземпляра класу, який ми тестуємо (System Under Test - SUT)
        App calculator = new App();
        
        // 2. Визначення очікуваного результату
        int expected = 12;
        
        // 3. Виклик методу та отримання фактичного результату
        int actual = calculator.add(5, 7);
        
        // 4. Перевірка: чи відповідає фактичний результат очікуваному
        assertEquals(expected, actual, "Метод add() має повертати 12 для 5 і 7");
    }

    @Test
    void additionOfNegativesTest() {
        App calculator = new App();
        assertEquals(-5, calculator.add(-2, -3), "Має правильно обробляти від'ємні числа");
    }
}