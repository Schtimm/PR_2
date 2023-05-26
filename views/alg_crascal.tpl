% rebase('layout.tpl', title="Метод Краскала")

<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        mermaid.initialize({startOnLoad: true});
    });</script>

<div class="px-12">
    <h1 class="text-3xl font-bold mb-4">Алгоритм Краскала</h1>
    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
        <div class="sm:col-span-3">
        <textarea class="w-full h-32 p-2 bg-white rounded shadow h-full"
                  placeholder="Введите матрицу весов ребер, разделяя элементы запятыми и строки переносами строки"></textarea>
        </div>
        <div class="sm:col-span-3">
            <div class="w-full h-32 p-2 bg-white rounded shadow  h-full flex items-center justify-center">
                <div class="mermaid">
                    graph LR
                    A -- 5 --- B
                </div>

            </div>
        </div>
    </div>

    <div class="mermaid">
        graph LR
        A -- 5 --- B
        A -- 7 --- C
        B -- 2 --- C
        B -- 9 --- D
        C -- 1 --- D
        C -- 8 --- E
        D -- 4 --- E
    </div>

    <p class="text-lg mb-4">Описание алгоритма Краскала:</p>

    <ol class="list-decimal list-inside">
        <li>Сортируйте все ребра графа в порядке возрастания их весов.</li>
        <li>Проходите по отсортированным ребрам и добавляйте их в остовное дерево, если они не создают цикл.</li>
        <li>Повторяйте шаг 2 до тех пор, пока не будут добавлены все вершины в остовное дерево.</li>
    </ol>

    <p class="text-lg mt-4">Кратчайшее остовное дерево:</p>

    <div class="mermaid">
        graph LR
        C -- 1 --- D
        B -- 2 --- C
        D -- 4 --- E
        A -- 5 --- B
    </div>
</div>