% rebase('layout.tpl', title="Метод Краскала")

<script src="/static/scripts/mermaid.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        mermaid.initialize({startOnLoad: true});
    });</script>

<script>

    const alphabet = [...'abcdefghijklmnopqrstuvwxyz'];

    /// Форматирование строки матрицы
    function formatMatrix(value) {
        return value.replace(' ', '') // Удаление всех пробелов, которые вводит пользователь
    }

    /// Проверка матрицы на корректность
    function isCorrectMatrix(value) {
        let matrix = parseMatrix(value)
        console.log(matrix)
        for (const arr of matrix) {
            if (arr.length !== matrix.length || isNaN(arr.slice(-1)[0])) {
                document.getElementById("alert").style.display = "block"
                document.getElementById("alert_message").textContent = "Матрица должна быть квадратной"
                return false;
            }
        }

        document.getElementById("alert").style.display = "none"
        return true;
    }

    function parseMatrix(input) {
        const rows = input.split('\n');
        const matrix = [];

        for (let i = 0; i < rows.length; i++) {
            const rowValues = rows[i].split(',');

            // Преобразование строковых значений в числа
            const parsedRow = rowValues.map((value) => parseFloat(value));

            matrix.push(parsedRow);
        }
        return matrix;
    }

    /// Отображение графа
    async function drawGraph(value) {
        let matrix = parseMatrix(value)
        var graph = "graph LR\n"
        for (let i = 0; i < matrix.length; i++) {
            const row = matrix[i];
            for (let j = 0; j < row.length; j++) {
                const weight = row[j];
                if (weight > 0) {
                    graph += `${i} -- ${weight} --- ${j}\n`
                }
            }
        }

        let output = document.getElementById("graph_parent");


        const {svg} = await mermaid.render("graph_view", graph);
        output.innerHTML = `<div id="graph_view" class="mermaid">${svg}</div>`;
    }

</script>

<div class="px-12">
    <h2 class="text-3xl font-semibold text-gray-800 my-12">Алгоритм Краскала</h2>
    <div style="display: none" id="alert" role="alert">
        <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
            К вниманию
        </div>
        <div class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
            <p id="alert_message">Введённая матрица некорректная</p>
        </div>
    </div>
    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
        <div class="sm:col-span-3">
        <textarea oninput="this.value = formatMatrix(this.value); "
                  onchange="if (isCorrectMatrix(this.value)) drawGraph(this.value);"
                  class="w-full h-32 p-2 bg-white rounded shadow h-full"
                  placeholder="Введите матрицу весов ребер, разделяя элементы запятыми и строки переносами строки"></textarea>
        </div>
        <div class="sm:col-span-3">
            <div id="graph_parent" class="w-full h-32 p-2 bg-white rounded shadow  h-full flex items-center justify-center">
                <div id="graph_view" class="mermaid">
                    graph LR
                    Тут -- будет --- A[ваш граф]
                </div>

            </div>
        </div>
        <div class="sm:col-span-6 flex justify-end">
            <div class="flex gap-x-4">
                <button class="px-4 py-2 bg-blue-500 text-white rounded shadow">Сгенерировать задачу</button>
                <button class="px-4 py-2 bg-blue-500 text-white rounded shadow">Решить</button>
            </div>
        </div>
    </div>


</div>

<div class="max-w-3xl mx-auto">
    <h2 class="text-2xl font-semibold text-gray-800 my-12 text-center">Пример</h2>

    <div class="w-full h-64 bg-gray-100 rounded shadow flex items-center justify-center mb-8">
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
    </div>

    <p class="text-lg mb-4">Описание алгоритма Краскала:</p>

    <ol class="list-decimal list-inside mb-8">
        <li>Сортируйте все ребра графа в порядке возрастания их весов.</li>
        <li>Проходите по отсортированным ребрам и добавляйте их в остовное дерево, если они не создают цикл.</li>
        <li>Повторяйте шаг 2 до тех пор, пока не будут добавлены все вершины в остовное дерево.</li>
    </ol>

    <h2 class="text-2xl font-semibold text-gray-800 my-12 text-center">Шаги выполнения алгоритма Краскала:</h2>

    <div class="grid grid-cols-1 gap-8 sm:grid-cols-2">
        <div class="bg-white rounded-lg p-6">
            <div class="w-full h-48 bg-gray-100 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A -- 5 --- B
                    A -- 7 --- C
                    B -- 2 --- C
                    B -- 9 --- D
                    C -- 1 --- D
                    C -- 8 --- E
                    D -- 4 --- E
                    style C fill:#f9f
                    style D fill:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 1: Добавлено ребро C-D (вес 1).</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-full h-48 bg-gray-100 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A -- 5 --- B
                    A -- 7 --- C
                    B -- 2 --- C
                    B -- 9 --- D
                    C -- 1 --- D
                    C -- 8 --- E
                    D -- 4 --- E
                    style B fill:#f9f
                    style C fill:#f9f
                    style D fill:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 2: Добавлено ребро B-C (вес 2).</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-full h-48 bg-gray-100 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A -- 5 --- B
                    A -- 7 --- C
                    B -- 2 --- C
                    B -- 9 --- D
                    C -- 1 --- D
                    C -- 8 --- E
                    D -- 4 --- E
                    style B fill:#f9f
                    style C fill:#f9f
                    style D fill:#f9f
                    style E fill:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 6 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 3: Добавлено ребро D-E (вес 4).</p>
        </div>

        <div class="bg-white rounded-lg p-6">
            <div class="w-full h-48 bg-gray-100 rounded shadow mb-4">
                <div class="mermaid">
                    graph LR
                    A -- 5 --- B
                    A -- 7 --- C
                    B -- 2 --- C
                    B -- 9 --- D
                    C -- 1 --- D
                    C -- 8 --- E
                    D -- 4 --- E
                    style B fill:#f9f
                    style C fill:#f9f
                    style D fill:#f9f
                    style E fill:#f9f
                    style A fill:#f9f
                    linkStyle 4 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 2 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 6 stroke-width:2px,fill:none,stroke:#f9f
                    linkStyle 0 stroke-width:2px,fill:none,stroke:#f9f
                </div>
            </div>
            <p class="text-lg">Шаг 4: Добавлено ребро A-B (вес 5).</p>
        </div>
    </div>

    <p class="text-lg mt-8">Кратчайшее остовное дерево:</p>

    <div class="w-full h-64 bg-gray-100 rounded shadow mb-8 flex items-center justify-center">
        <div class="mermaid">
            graph LR
            C -- 1 --- D
            B -- 2 --- C
            D -- 4 --- E
            A -- 5 --- B
        </div>
    </div>
</div>