// Це мінімальний тестовий файл для виконання CI-пайплайну.
const assert = require('assert');
// ➡️ Імпортуємо код, який ми щойно створили в index.js
const AppCore = require('./index'); 

// Група тестів для основної логіки
describe('Application Core Logic', function() {
  // Тест 1: Перевірка базового додавання
  it('should verify basic addition result (1 + 3 = 4)', function() {
    // ➡️ Тестуємо функцію add() з нашого модуля AppCore
    assert.strictEqual(AppCore.add(1, 3), 4);
  });

  // Тест 2: Перевірка стану (має завжди повертати true)
  it('should confirm application status is active', function() {
    // ➡️ Тестуємо функцію getStatus() з нашого модуля AppCore
    assert.strictEqual(AppCore.getStatus(), true, "The application status should be true.");
  });

  // Тест 3: Перевірка додавання негативних чисел
  it('should handle adding negative numbers (-10 + 5 = -5)', function() {
    assert.strictEqual(AppCore.add(-10, 5), -5);
  });
});