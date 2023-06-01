# Автор: Панков Василий
# Дата создания: 29.05.2023

from random import randrange

from typing import List, Tuple, Dict, Iterator


def check_matrix(weight_matrix: List[List[float]]):
    """Проверка, на то что матрица соответствует для данной задачи"""
    assert any(any(row) for row in weight_matrix), "Матрица состоит из нулей, это не является графом"
    for arr in weight_matrix:
        assert len(arr) == len(weight_matrix), "Матрица не является квадратной"
        for el in arr:
            assert el >= 0, "В матрице не должно быть отрицательных чисел"
    for i in range(len(weight_matrix)):
        for j in range(i, len(weight_matrix)):
            if i == j:
                assert weight_matrix[i][j] == 0, "Диагональ должна быть равна 0"
            assert weight_matrix[i][j] == weight_matrix[j][i], "Матрица не симметрична"


def find_parent(parent: List[int], i: int) -> int:
    """Вспомогательная функция для нахождения корня дерева

    :param parent: строка матрицы
    :param i: индекс"""
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])


def union(parent: List[int], rank: List[int], x: int, y: int) -> None:
    """Вспомогательная функция для объединения двух множеств
    :param parent: Список, содержащий родительские вершины для каждой вершины
    :param rank: Список, содержащий ранг (глубину) каждой вершины
    :param x: Начлальная вершина множества x
    :param y: Начлальная вершина множества y
    """

    # Находим корневые вершины (x_root и y_root) для множеств x и y
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    # Если ранг x_root меньше ранга y_root, то x_root становится родительской вершиной для y_root
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:  # Если ранг x_root больше ранга y_root, то
        # y_root становится родительской вершиной для x_root
        parent[y_root] = x_root
    else:  # Если ранги x_root и y_root равны, то выбирается одно из множеств (например, y_root),
        # и оно становится родительской вершиной для другого множества (x_root)
        parent[y_root] = x_root
        rank[x_root] += 1
    # После объединения X_root и y_root указывают на одну и ту же вершину


def crascal_solve(weight_matrix: List[List[float]]) -> List[Tuple[int, int, float]]:
    """Функция, которая решает алгоритмом Краскала
    :param weight_matrix: Матрица весов рёбер

    :return Минимальное остовное дерево в формате списка, элементами которого являются кортежи: (Начало, Конец, Вес)
    """

    # Проверяем матрицу
    check_matrix(weight_matrix)

    n = len(weight_matrix)
    parent = [i for i in range(n)]  # Массив для хранения родительских вершин
    rank = [0] * n  # Массив для хранения ранга каждой вершины

    # Минимальное оставное дерево (начало, конец, длина)
    minimum_spanning_tree: List[Tuple[int, int, float]] = []

    edges: List[Tuple[int, int, float]] = []  # Ребра (начало, конец, ребро)
    for i in range(n):
        for j in range(i + 1, n):
            if weight_matrix[i][j] != 0:
                edges.append((i, j, weight_matrix[i][j]))

    edges.sort(key=lambda a: a[2])

    for edge in edges:
        start, end, weight = edge

        # Проверяем, не создаст ли ребро цикл
        x = find_parent(parent, start)
        y = find_parent(parent, end)

        if x != y:
            minimum_spanning_tree.append((start, end, weight))
            union(parent, rank, x, y)

    return minimum_spanning_tree


def parse_matrix_from_string(string: str) -> List[List[float]]:
    """Генерация матрицы из строки

    :param string: Строка в которой через запятую перечислены элементы матрицы, а через \\n строки
    :return: Матрицу произвольного размера
    :raise ValueError: если значение не является числом
    """
    return [[float(value) for value in row.split(',')] for row in string.split('\n')]


def gen_mermaid_graph(edges: List[Tuple[int, int, float]], minimum_spanning_tree: List[Tuple[int, int, float]]) -> str:
    """Генерация графа в mermaid

    :param edges: Ребра(начало, конец, вес)
    :param minimum_spanning_tree: Минимальное остовное дерево(начало, конец, вес)
    """
    graph = "graph LR\n"
    # Проходим по всем рёбрам
    for i, edge in enumerate(edges):
        start, end, weight = edge
        # Для начала с единицы
        start += 1
        end += 1
        graph += f"{start} --{weight}--- {end}\n"
        if edge in minimum_spanning_tree:
            graph += f"style {start} fill:#f9f\n"
            graph += f"style {end} fill:#f9f\n"
            graph += f"linkStyle {i} stroke-width:2px,fill:none,stroke:#f9f\n"
    return graph


def edges_to_matrix(edges: List[Tuple[int, int, float]], n: int) -> List[List[float]]:
    """Функция для получения матрицы из рёбер

    :param edges: ребра, которые представляют собой кортеж (начало, конец, вес)
    :param n: размер матрицы

    :return Матрица весов рёбер"""

    matrix = [[0.] * n for _ in range(n)]

    for edge in edges:
        start, end, weight = edge
        matrix[start][end] = weight
        matrix[end][start] = weight

    return matrix


def matrix_to_string(matrix: List[List[float]]) -> str:
    """Функция для получения матрицы в строковом виде

    :return Строка в которой через запятую перечислены элементы матрицы, а через \\n строки"""
    return "\n".join([",".join(map(str, row)) for row in matrix])


def crascal_solve_with_steps(weight_matrix: List[List[float]]) -> Iterator[Dict[str, str]]:
    """Данная функция, такая же как crascal_solve, но по шагам. Она является генератором,
    который возвращает с каждым шагом новый граф и какое ребро мы добавили

    :return Возвращает итератор, каждый элемент которого является словарь {"message": str, "graph"/"matrix"/"sum": str}
    """
    # Проверяем матрицу
    check_matrix(weight_matrix)

    n: int = len(weight_matrix)
    parent: List[int] = [i for i in range(n)]  # Массив для хранения родительских вершин
    rank: List[int] = [0] * n  # Массив для хранения ранга каждой вершины

    # Минимальное оставное дерево (начало, конец, длина)
    minimum_spanning_tree: List[Tuple[int, int, float]] = []

    edges: List[Tuple[int, int, float]] = []  # Ребра (начало, конец, вес)
    for i in range(n):
        for j in range(i + 1, n):
            if weight_matrix[i][j] != 0:
                edges.append((i, j, weight_matrix[i][j]))

    edges.sort(key=lambda a: a[2])

    yield {"message": "Начальный граф", "graph": gen_mermaid_graph(edges, minimum_spanning_tree)}

    for edge in edges:
        start, end, weight = edge

        # Проверяем, не создаст ли ребро цикл
        x = find_parent(parent, start)
        y = find_parent(parent, end)

        if x != y:
            minimum_spanning_tree.append((start, end, weight))
            yield {"message": f"Добавлено ребро {start}{end} (Вес {weight})",
                   "graph": gen_mermaid_graph(edges, minimum_spanning_tree)}
            union(parent, rank, x, y)

    yield {"message": "Полученный граф", "graph": gen_mermaid_graph(minimum_spanning_tree, [])}
    yield {"message": "Остовное дерево", "matrix": matrix_to_string(edges_to_matrix(minimum_spanning_tree, n))}
    yield {"message": "Сумма", "sum": sum(map(lambda el: el[2], minimum_spanning_tree))}


def generate_matrix_to_solve() -> str:
    """Функция, которая генерирует матрицу для решения алгоритмом Краскала

    :return Строка в которой через запятую перечислены элементы матрицы, а через \\n строки
    """
    size = randrange(2, 8, 1)
    matrix = [[0.] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j] = randrange(0, 20, 1)
            matrix[j][i] = matrix[i][j]

    return matrix_to_string(matrix)
