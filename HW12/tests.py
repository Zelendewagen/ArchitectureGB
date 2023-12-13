# Разработать Unit Test для разработанного для проекта кода.
import unittest


class TestRobot(unittest.TestCase):
    def test_start_and_stop_cleaning(self):
        robot = Robot()

        robot.start_cleaning()
        self.assertTrue(
            robot.is_cleaning)  # Проверка, что флаг уборки изменен на True после вызова метода start_cleaning()
        robot.stop_cleaning()
        self.assertFalse(
            robot.is_cleaning)  # Проверка, что флаг уборки изменен на False после вызова метода stop_cleaning()

    def test_change_power(self):
        robot = Robot()

        self.assertEqual(robot.power, 50)  # Проверка активной мощности
        robot.set_power(50)  # Установка мощности 50%
        self.assertEqual(robot.power, 50)  # Проверка изменений мощности

    def test_move(self):
        robot = Robot()

        last_position = robot.getPosition
        robot.move("forward")
        self.assertEqual(robot.getPosition(), last_position)  # Проверка позиции робота после движения

        last_position = robot.getPosition
        robot.move("back")
        self.assertEqual(robot.getPosition(), last_position)  # Проверка позиции робота после движения

        last_position = robot.getPosition
        robot.move("right")
        self.assertEqual(robot.getPosition(), last_position)  # Проверка позиции робота после движения

        last_position = robot.getPosition
        robot.move("left")
        self.assertEqual(robot.getPosition(), last_position)  # Проверка позиции робота после движения

    def test_cleanup_after_cleaning(self):
        robot = Robot()

        robot.start_cleaning()
        # Здесь можем добавить логику для симуляции уборки (например, использовать фейковое время или методы mock объектов)
        robot.stop_cleaning()
        self.assertFalse(robot.is_cleaning)
        robot.cleanup()  # Очистка после завершения уборки
        self.assertTrue(robot.is_clear)  # Проверка чистоты робота
