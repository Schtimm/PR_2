# Автор: Панков Василий
# Дата создания: 27.05.2023

import unittest

from logic.alg_crascal import check_matrix, crascal_solve, generate_matrix_to_solve, parse_matrix_from_string, \
    gen_mermaid_graph, edges_to_matrix, matrix_to_string


class TestAlgCrascal(unittest.TestCase):
    """Тестирование алогритма Краскала"""
    invalid_matrices = [
        [],
        # Матрица неквадратная первый случай
        [
            [1, 0, 3],
            [0, 1],
            [2, 3, 0]
                        ],

        # Матрица не квадратная второй случай
        [[1, 2, 3]],

        # Нет симметрии
        [
            [0, 0, 3],
            [0, 0, 1],
            [2, 3, 0],
        ],

        # Отрицательные числа
        [[0, -2],
         [-2, 0]],

        # нули
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ],

        # Диагональ не равна 0
        [[1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2],
         [1, 2, 3, 3, 3],
         [1, 2, 3, 4, 4],
         [1, 2, 3, 4, 5]
         ]
    ]

    def test_check_matrix_valid(self):
        """Тестирование проверки матриц для решения алгоритмом Краскала, корректные матрицы"""
        matrices = [
                    [
                        [0, 7, 11, 6, 5, 8],
                        [7, 0, 1, 8, 19, 7],
                        [11, 1, 0, 9, 0, 4],
                        [6, 8, 9, 0, 12, 16],
                        [5, 19, 0, 12, 0, 17],
                        [8, 7, 4, 16, 17, 0]
                    ],

                    [[0, 1, 1, 1, 1],
                     [1, 0, 2, 2, 2],
                     [1, 2, 0, 3, 3],
                     [1, 2, 3, 0, 4],
                     [1, 2, 3, 4, 0]
                     ],
                    # Проверки функции генератора и парсера
                    parse_matrix_from_string(generate_matrix_to_solve())
                    ]
        for el in matrices:
            self.assertIsNone(check_matrix(el))

    def test_check_matrix_invalid(self):
        """Тестирование проверки матриц для решения алгоритмом Краскала, некорректные матрицы"""

        for matrix in self.invalid_matrices:
            self.assertRaises(AssertionError, check_matrix, matrix)

    def test_crascal_solve(self):
        """Тестирование решения алгоритмом Краскала"""
        matrices = [
            # Тестовая матрица 1 (нет возможной разъеденении двух множеств)
            [[0, 1, 2, 0],
             [1, 0, 3, 0],
             [2, 3, 0, 4],
             [0, 0, 4, 0]],
            # Тестовая матрица 2 (большая матрица, есть возможное разъеденение двух множеств)
            [
                [0, 7, 11, 6, 5, 8],
                [7, 0, 1, 8, 19, 7],
                [11, 1, 0, 9, 0, 4],
                [6, 8, 9, 0, 12, 16],
                [5, 19, 0, 12, 0, 17],
                [8, 7, 4, 16, 17, 0]
            ],

            # Тестовая матрица 3 (дополнительный тест)
            [[0, 1, 3, 0],
             [1, 0, 0, 2],
             [3, 0, 0, 4],
             [0, 2, 4, 0]],


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
            [(1, 2, 1), (2, 5, 4), (0, 4, 5), (0, 3, 6), (0, 1, 7)],

            # Ожидаемый результат для Тестовой матрицы 3
            [(0, 1, 1), (1, 3, 2), (0, 2, 3)],

            # Ожидаемый результат для Матрицы с дублирующимися ребрами
            [(0, 1, 1), (1, 2, 1)]
        ]

        # Проверка результатов для каждой матрицы
        for matrix, expected_result in zip(matrices, expected_results):
            self.assertEqual(crascal_solve(matrix), expected_result)

    def test_crascal_solve_invalid_matrix(self):
        """Тест с неправильными матрицами"""
        for matrix in self.invalid_matrices:
            self.assertRaises(AssertionError, crascal_solve, matrix)



class TestHelpfulFunctions(unittest.TestCase):
    """Тестирование вспомогательных функций"""

    def test_gen_mermaid_graph(self):
        """Тестирование генерации графов mermaid"""
        test_cases = [
            {
                'edges': [(0, 1, 3.5), (1, 2, 2.2), (2, 3, 4.7), (0, 3, 1.8)],
                'minimum_spanning_tree': [(0, 1, 3.5), (1, 2, 2.2)],
                'expected_output': """graph LR
1 --3.5--- 2
style 1 fill:#f9f
style 2 fill:#f9f
linkStyle 0 stroke-width:2px,fill:none,stroke:#f9f
2 --2.2--- 3
style 2 fill:#f9f
style 3 fill:#f9f
linkStyle 1 stroke-width:2px,fill:none,stroke:#f9f
3 --4.7--- 4
1 --1.8--- 4
"""
            },
            {
                'edges': [(0, 1, 2.5)],
                'minimum_spanning_tree': [],
                'expected_output': "graph LR\n1 --2.5--- 2\n"
            },
        ]

        for test in test_cases:
            result = gen_mermaid_graph(test['edges'], test['minimum_spanning_tree'])
            self.assertEqual(result, test['expected_output'])

    def test_edges_to_matrix(self):
        """Тестирование преобразования рёбер в матрицу"""
        test_cases = [
            {
                'edges': [(0, 1, 3.5), (1, 2, 2.2), (2, 3, 4.7), (0, 3, 1.8)],
                'n': 4,
                'expected_output': [[0.0, 3.5, 0.0, 1.8],
                                    [3.5, 0.0, 2.2, 0.0],
                                    [0.0, 2.2, 0.0, 4.7],
                                    [1.8, 0.0, 4.7, 0.0]]
            },
            {
                'edges': [],
                'n': 3,
                'expected_output': [[0.0, 0.0, 0.0],
                                    [0.0, 0.0, 0.0],
                                    [0.0, 0.0, 0.0]]
            },

        ]

        for test in test_cases:
            result = edges_to_matrix(test['edges'], test['n'])
            self.assertEqual(result, test['expected_output'])

    def test_matrix_to_string(self):
        """Тестирование преобразования матрицы в строку"""
        test_cases = [
            {
                'matrix': [[0.0, 3.5, 0.0, 1.8],
                           [3.5, 0.0, 2.2, 0.0],
                           [0.0, 2.2, 0.0, 4.7],
                           [1.8, 0.0, 4.7, 0.0]],
                'expected_output': "0.0,3.5,0.0,1.8\n3.5,0.0,2.2,0.0\n0.0,2.2,0.0,4.7\n1.8,0.0,4.7,0.0"
            },
            {
                'matrix': [[1.5]],
                'expected_output': "1.5"
            },
        ]

        for test in test_cases:
            result = matrix_to_string(test['matrix'])
            self.assertEqual(result, test['expected_output'])

    def test_parse_matrix_from_string(self):
        """Тестирование функции парсинга из строки в матрицу"""
        test_cases = [
            {
                'string': "1.0,2.0\n3.0,4.0\n5.0,6.0",
                'expected_output': [[1.0, 2.0],
                                    [3.0, 4.0],
                                    [5.0, 6.0]]
            },
            {
                'string': "0",
                'expected_output': [[0.0]]
            },
        ]

        for test in test_cases:
            result = parse_matrix_from_string(test['string'])
            self.assertEqual(result, test['expected_output'])

    def test_parse_matrix_from_string_invalid(self):
        """Тестирование функции парсинга из строки в матрицу"""
        invalid_values = [
            # пустой
            "",
            # c буквами
            "1.0,abc,2.3\n4.5,6.7,8.9",
            # \n на конце
            "1.0,2.0\n3.0,4.0\n5.0,6.0\n",
            # пустые
            "1.0,,,2.0\n3.0,4.0\n5.0,6.0"
                          ]

        for value in invalid_values:
            self.assertRaises(ValueError, parse_matrix_from_string, value)


if __name__ == '__main__':
    unittest.main()
