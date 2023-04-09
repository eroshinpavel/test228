import math
import unittest


def distribute_orders(num_orders):
    if not isinstance(num_orders, int) or num_orders < 0:
        raise TypeError("num_orders должен быть положительным целым числом")
    if num_orders == 0:
        return []
    elif num_orders <= 40:
        return [num_orders]
    else:
        num_trucks = math.ceil(num_orders / 40)
        orders_per_truck = num_orders // num_trucks
        extra_orders = num_orders % num_trucks
        return [orders_per_truck + 1 if i < extra_orders else orders_per_truck for i in range(num_trucks)]




class TestOrderDistribution(unittest.TestCase):

    def test_zero_orders(self):
        self.assertEqual(distribute_orders(0), [])

    def test_single_truck(self):
        self.assertEqual(distribute_orders(5), [5])
        self.assertEqual(distribute_orders(40), [40])

    def test_multiple_trucks(self):
        self.assertEqual(distribute_orders(41), [21, 20])
        self.assertEqual(distribute_orders(80), [40, 40])
        self.assertEqual(distribute_orders(85), [29, 28, 28])

    def test_large_number_of_orders(self):
        self.assertEqual(distribute_orders(1000), [40] * 25)

    def test_noninteger_input(self):
        with self.assertRaises(TypeError):
            distribute_orders(5.5)


if __name__ == "__main__":
    print('Добро пожаловать в сортировщик груза для грузовика! Выберите функцию:')
    a = int(input('1 - работа с функцией распределения груза, 2 - проведение юниттестов функции '))
    if a == 1:
        while True:
            num_orders = int(input('Введите количество груза '))
            print(distribute_orders(num_orders))
            if input('Хотите еще? 1 - да, 2 - нет ') == '2':
                break
    elif a == 2:
        unittest.main(exit=False)