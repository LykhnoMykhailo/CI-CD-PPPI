public class App {
    
    /**
     * Основна точка входу для запуску програми (якщо потрібно).
     * @param args Аргументи командного рядка.
     */
    public static void main(String[] args) {
        // Тут може бути логіка запуску, наприклад:
        App calculator = new App();
        int result = calculator.add(5, 7);
        System.out.println("Результат додавання 5 + 7: " + result);
    }

    /**
     * Додає два цілих числа. Це метод, який ми будемо тестувати.
     * @param a Перше число.
     * @param b Друге число.
     * @return Сума a і b.
     */
    public int add(int a, int b) {
        return a + b; // Простий функціонал
    }
}