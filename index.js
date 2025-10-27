/**
 * Простий модуль для демонстрації CI/CD.
 * Містить основну логіку, яку ми перевіряємо у test.js.
 */
class AppCore {
    /**
     * Повертає статус програми.
     * @returns {boolean} true, якщо додаток активний.
     */
    static getStatus() {
        return true; 
    }

    /**
     * Виконує додавання.
     * @param {number} a 
     * @param {number} b 
     * @returns {number} Сума a та b.
     */
    static add(a, b) {
        return a + b;
    }
}

module.exports = AppCore;