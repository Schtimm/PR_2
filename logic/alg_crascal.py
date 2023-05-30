# Автор: Панков Василий
# Дата создания: 29.05.2023

from typing import List, Tuple, Set, Dict, Iterator


def check_matrix(weight_matrix: List[List[float]]):
    """Проверка, на то что матрица соответстыет для данной задачи"""
    for arr in weight_matrix:
        assert len(arr) == len(weight_matrix), "Матрица не является квадратной"
        for el in arr:
            assert el >= 0, "В матрице не должно быть отрицательных чисел"


def crascal_solve(weight_matrix: List[List[float]]) -> List[Tuple[int, int, float]]:
    """Функция, которая решает алгоритмом Краскала
    :param weight_matrix: Матрица весов рёбер

    :return Минимальное остовное дерево в формате списка, элементами которого являются кортежи: (Начало, Конец, Вес)
    """

    check_matrix(weight_matrix)

    # Минимальное оставное дерево (начало, конец, длина)
    minimum_spanning_tree: List[Tuple[int, int, float]] = []
    # Ребра (начало, конец, ребро)
    edges: List[Tuple[int, int, float]] = []

    # Множество соединенных вершин
    union_trees: Set[int] = set()
    # словарь списка изолированных групп вершин
    groups: Dict[int, List[int]] = {}
    for i in range(len(weight_matrix)):
        for j in range(len(weight_matrix)):
            if weight_matrix[i][j] != 0:
                edges.append((i, j, weight_matrix[i][j]))

    edges.sort(key=lambda a: a[2])
    for edge in edges:
        # Проверка на образование циклов
        if edge[0] not in union_trees or edge[1] not in union_trees:
            # Если обеих вершин нет в множестве то добавляем в группу
            if edge[0] not in union_trees and edge[1] not in union_trees:
                groups[edge[0]] = [edge[0], edge[1]]
                groups[edge[1]] = [edge[0], edge[1]]
            else:
                # Если первой вершины нет  группах, то добавляем его  существующей и создаём его собственную группу
                if edge[0] not in groups.keys():
                    groups[edge[1]].append(edge[0])
                    groups[edge[0]] = [edge[1]]
                else:
                    groups[edge[0]].append(edge[1])
                    groups[edge[1]] = [edge[0]]
            minimum_spanning_tree.append(edge)  # Добавляем ребро в остов
            union_trees.add(edge[0])
            union_trees.add(edge[1])

    return minimum_spanning_tree

def parse_matrix_from_string(string: str) -> List[List[float]]:
    """Генерация матрицы из строки

    :param string: Строка в которой через запятую перечислены элементы матрицы, а через \\n строки
    :return: Матрицу произвольного размере
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
        graph += f"{edge[0]} --{edge[2]}--- {edge[1]}\n"
        if edge in minimum_spanning_tree:
            graph += f"style {edge[0]} fill:#f9f\n"
            graph += f"style {edge[1]} fill:#f9f\n"
            graph += f"linkStyle {i} stroke-width:2px,fill:none,stroke:#f9f\n"
    return graph


def crascal_solve_with_steps(weight_matrix: List[List[float]]) -> Iterator[Dict[str, str]]:
    """Данная функция, такая же как crascal_solve, но по шагам. Она является генератором,
    который возвращает с каждым шагом новый граф и какое ребро мы добавили

    :return Возвращает итератор, каждый элемент которого является словарь {"message": str, "graph": str}
    """
    check_matrix(weight_matrix)

    # Минимальное оставное дерево (начало, конец, длина)
    minimum_spanning_tree: List[Tuple[int, int, float]] = []
    # Ребра (начало, конец, ребро)
    edges: List[Tuple[int, int, float]] = []

    # Множество соединенных вершин
    union_trees: Set[int] = set()
    # словарь списка изолированных групп вершин
    groups: Dict[int, List[int]] = {}
    for i in range(len(weight_matrix)):
        for j in range(len(weight_matrix)):
            if weight_matrix[i][j] != 0:
                edges.append((i, j, weight_matrix[i][j]))

    edges.sort(key=lambda a: a[2])
    yield {"message": "Начальный граф", "graph": gen_mermaid_graph(edges, minimum_spanning_tree)}

    for edge in edges:
        # Проверка на образование циклов
        if edge[0] not in union_trees or edge[1] not in union_trees:
            # Если обеих вершин нет в множестве то добавляем в группу
            if edge[0] not in union_trees and edge[1] not in union_trees:
                groups[edge[0]] = [edge[0], edge[1]]
                groups[edge[1]] = [edge[0], edge[1]]
            else:
                # Если первой вершины нет  группах, то добавляем его  существующей и создаём его собственную группу
                if edge[0] not in groups.keys():
                    groups[edge[1]].append(edge[0])
                    groups[edge[0]] = [edge[1]]
                else:
                    groups[edge[0]].append(edge[1])
                    groups[edge[1]] = [edge[0]]
            minimum_spanning_tree.append(edge)  # Добавляем ребро в остов
            yield {"message": f"Добавлено ребро {edge[0]}{edge[1]}",
                   "graph": gen_mermaid_graph(edges, minimum_spanning_tree)}
            union_trees.add(edge[0])
            union_trees.add(edge[1])

    yield {"message": "Полученный граф", "graph": gen_mermaid_graph(minimum_spanning_tree, [])}

