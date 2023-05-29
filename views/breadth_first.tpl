
% rebase('layout.tpl', title="Поиск в ширину")
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        mermaid.initialize({startOnLoad: true});
    });</script>

<div class="px-12">
    <h1 class="text-3xl font-bold mb-4">Алгоритм поиска в ширину</h1>
    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
        <div class="sm:col-span-3">
        <textarea class="w-full h-32 p-2 bg-white rounded shadow h-full"
                  placeholder="Введите матрицу инцидентности ребер, разделяя элементы запятыми и строки переносами строки"></textarea>
        </div>
        <div class="sm:col-span-3">
            <div class="w-full h-32 p-2 bg-white rounded shadow  h-full flex items-center justify-center">
                <div class="mermaid">
                    graph LR
                    Тут -- будет --- A[ваш граф]
                </div>

            </div>
        </div>
    </div>

    <div class="mermaid">
        graph LR
        A ---- B
        A ---- C
        A ---- D
        B ---- E
        C ---- F
        C ---- G
        D ---- E
    </div>

    <p class="text-lg mb-4">Описание алгоритма поиска в ширину:</p>

    <ol class="list-decimal list-inside">
        <li>Запишите все вершины соседние изначальной</li>
        <li>Запишите их, запишите расстояние</li>
        <li>Перейдите к одной из найденных соседних вершин</li>
        <li>Повторите выше перечисленные шаги для текущей вершины</li>
    </ol>

    <p class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">Матрица длин путей из точки A к другим вершинам</p>

    <div class="mermaid">
        graph LR
        A --1--- B
        A --1--- C
        A --1--- D
        A --2--- E
        A --2--- F
        A --2--- G
    </div>
</div>