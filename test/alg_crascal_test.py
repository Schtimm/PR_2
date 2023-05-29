import unittest

from logic.alg_crascal import check_matrix, crascal_solve


class TestGraphAlgorithms(unittest.TestCase):

    def test_check_matrix_valid(self):
        # Правильные матрицы
        matrices = [[],

                    [[10]],

                    [[0, 1, 2],
                     [1, 0, 3],
                     [2, 3, 0]],

                    [[1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5]
                     ]
                    ]
        for el in matrices:
            self.assertIsNone(check_matrix(el))

    def test_check_matrix_invalid(self):
        # Неправильная матрици
        invalid_matrices = [
            [[0, 1],
             [1, 0, 3],
             [2, 3, 0]],
            [[1, 2, 3]],
            [[1], [1]],
            [[]],
            [
                [1, 0, 3],
                [0, 1],
                [2, 3, 0]],
            [[-1, -2], [-1, -2]] # Пути не могут быть меньше 0
        ]
        for matrix in invalid_matrices:
            self.assertRaises(AssertionError, check_matrix, matrix)

    def test_crascal_solve(self):
        # Список тестовых матриц
        matrices = [
            # Тестовая матрица 1
            [[0, 1, 2, 0],
             [1, 0, 3, 0],
             [2, 3, 0, 4],
             [0, 0, 4, 0]],

            # Тестовая матрица 2
            [[0, 1, 3, 0],
             [1, 0, 0, 2],
             [3, 0, 0, 4],
             [0, 2, 4, 0]],

            # Пустая матрица
            [],

            # Матрица с одной вершиной
            [[0]],

            # Матрица с дублирующимися ребрами
            [[0, 1, 2],
             [1, 0, 1],
             [2, 1, 0]]
        ]

        # Список ожидаемых результатов
        expected_results = [
            # Ожидаемый результат для Тестовой матрицы 1
            [(0, 1, 1), (0, 2, 2), (2, 3, 4)],

            # Ожидаемый результат для Тестовой матрицы 2
            [(0, 1, 1), (1, 3, 2), (0, 2, 3)],

            # Ожидаемый результат для Пустой матрицы
            [],

            # Ожидаемый результат для Матрицы с одной вершиной
            [],

            # Ожидаемый результат для Матрицы с дублирующимися ребрами
            [(0, 1, 1), (1, 2, 1)]
        ]

        # Проверка результатов для каждой матрицы
        for matrix, expected_result in zip(matrices, expected_results):
            self.assertEqual(crascal_solve(matrix), expected_result)

    def test_crascal_solve_invalid_matrix(self):
        # Неправильная матрица (не квадратная)
        invalid_matrix = [[0, 1, 2],
                          [1, 0, 3]]
        self.assertRaises(AssertionError, crascal_solve, invalid_matrix)


if __name__ == '__main__':
    unittest.main()
