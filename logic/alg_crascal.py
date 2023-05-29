from typing import List, Tuple, Set, Dict


def check_matrix(weight_matrix: List[List[float]]):
    """Проверка, на то что матрица соответстыет для данной задачи"""
    for arr in weight_matrix:
        assert len(arr) == len(weight_matrix), "Матрица не является квадратной"
        for el in arr:
            assert el >= 0, "В матрице не должно быть отрицательных чисел"


def crascal_solve(weight_matrix: List[List[float]]) -> List[Tuple[int, int, float]]:
    """Функция, которая решает алгоритмом Краскала"""

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
            minimum_spanning_tree.append(edge) # Добавляем ребро в остов
            union_trees.add(edge[0])
            union_trees.add(edge[1])

    return minimum_spanning_tree
