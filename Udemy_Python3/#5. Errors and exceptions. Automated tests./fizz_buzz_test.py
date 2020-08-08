import unittest
import fizz_buzz


class FizzBuzzTests(unittest.TestCase):

    # Определяем тестировочные случаи (методы, которые будут исполняться тест-ранером).
    def test_fizz(self):  # Проверяем поведение нашей программы.
        number = 6

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result,
                         'Fizz')  # Проверяем, действительно ли результат полученный от вызова тестируемой функции совпадает с ожидаемым результатом.

    def tets_buzz(self):
        number = 10

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'Buzz')

    def tets_fizzbuzz(self):
        number = 15

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
