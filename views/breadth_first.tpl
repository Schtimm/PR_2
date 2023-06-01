
% rebase('layout.tpl', title="Поиск в ширину")
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        mermaid.initialize({startOnLoad: true});
    });</script>

<div class="px-12">
    <h1 class="text-3xl font-bold mb-4">Алгоритм поиска в ширину</h1>
    <div class="mt-10 grid grid-cols-1 gap-x-5 gap-y-8 sm:grid-cols-6">
        <div class="sm:col-span-3">
        <textarea class="w-full h-32 p-2 bg-white rounded shadow"
                  placeholder="Введите матрицу инцидентности ребер, разделяя элементы запятыми и строки переносами строки"></textarea>
        </div>
        <div class="sm:col-span-3">
            <div class="w-full h-32 p-2 bg-white rounded shadow flex items-center justify-center">
                <div class="mermaid">
                    graph LR
                    Тут -- будет --- A[ваш граф]
                </div>                
            </div>
        </div>
    </div> 
    <div align="right">
        <button class="px-4 py-2 bg-blue-500 text-white rounded shadow">Сгенерировать задачу</button>
        <button class="px-4 py-2 bg-blue-500 text-white rounded shadow">Решить</button>
    </div>
    </div>
    <div align="center">
        <div>
            <h2 class="text-2xl font-bold mb-4">Пример</h2>
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
            <ol class="list-decimal list-inside mb-8">
                <li>Найдите все вершины соседние изначальной</li>
                <li>Запишите найденные вершины, запишите расстояние от изначальной вершины до найденных</li>
                <li>Перейдите к одной из найденных соседних вершин</li>
                <li>Повторите выше перечисленные шаги для текущей вершины</li>
            </ol>
        <div/>
        <p class="text-lg mb-4">Пошаговое выполнение алгоритма:</p>
        <div class="grid max-w-3xl grid-cols-1 gap-0 sm:grid-cols-2">
            <div class="bg-white rounded-lg p-6">
                <div class="w-80 h-144 bg-gray-50 rounded shadow mb-4">
                    <div class="mermaid">
                        graph LR
                        A ---- B
                        A ---- C
                        A ---- D
                        B ---- E
                        C ---- F
                        C ---- G
                        D ---- E
                        style A fill:#f9f
                    </div>
                </div>
            <p class="text-lg">Шаг 1.</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-80 h-144 bg-gray-50 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A ---- B
                    A ---- C
                    A ---- D
                    B ---- E
                    C ---- F
                    C ---- G
                    D ---- E
                    style A fill:#f9f
                    linkStyle 0 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 1 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 2.</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-80 h-144 bg-gray-50 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A ---- B
                    A ---- C
                    A ---- D
                    B ---- E
                    C ---- F
                    C ---- G
                    D ---- E
                    style A fill:#f9f
                    style B fill:#f9f
                    style C fill:#f9f
                    style D fill:#f9f
                    linkStyle 0 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 1 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 3 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 5 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 6 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 3.</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-80 h-144 bg-gray-50 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A ---- B
                    A ---- C
                    A ---- D
                    B ---- E
                    C ---- F
                    C ---- G
                    D ---- E
                    style A fill:#f9f
                    style A fill:#f9f
                    style B fill:#f9f
                    style C fill:#f9f
                    style D fill:#f9f
                    style E fill:#f9f
                    style F fill:#f9f
                    style G fill:#f9f
                    linkStyle 0 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 1 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 3 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 5 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 6 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 4.</p>
        </div>

    </div>
        <p>Матрица кратчайших путей из точки А к другим вершинам</p>
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
</div>