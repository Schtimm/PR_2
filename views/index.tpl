% rebase('layout.tpl', title="Домашняя страница")


<header class="py-16 bg-blue-500 text-white">
    <div class="container mx-auto px-4">
        <h1 class="text-4xl font-semibold mb-4">Добро пожаловать на страницу Решения графов </h1>
        <p class="text-lg">Исследуйте мир графовых алгоритмов и решайте задачи, связанные с графами.</p>
    </div>
</header>

<!-- Секция с особенностями -->
<section id="features" class="py-20">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl font-semibold text-gray-800 mb-12">Варианты решений</h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
            <!-- Особенность 1 -->
            <div class="bg-white rounded-lg p-8 shadow">
                <h3 class="text-xl font-semibold mb-4">Поиск в ширину</h3>
                <p class="text-gray-700 mb-6">Изучите алгоритм поиска в ширину и его применение для обхода графовых
                    структур.</p>
                <a href="#" class="text-blue-500 font-semibold">Узнать больше</a>
            </div>

            <!-- Особенность 2 -->
            <div class="bg-white rounded-lg p-8 shadow">
                <h3 class="text-xl font-semibold mb-4">Поиск в глубину</h3>
                <p class="text-gray-700 mb-6">Откройте алгоритм поиска в глубину и его использование для обхода графов и
                    поиска путей.</p>
                <a href="#" class="text-blue-500 font-semibold">Узнать больше</a>
            </div>

            <!-- Особенность 3 -->
            <div class="bg-white rounded-lg p-8 shadow">
                <h3 class="text-xl font-semibold mb-4">Алгоритм Краскала</h3>
                <p class="text-gray-700 mb-6">Исследуйте алгоритм Краскала и его применение для нахождения минимального
                    остовного дерева.</p>
                <a href="/crascal" class="text-blue-500 font-semibold">Узнать больше</a>
            </div>
        </div>
    </div>
</section>

<!-- Секция "О нас" -->
<section id="about" class="py-20 bg-gray-200">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl font-semibold text-gray-800 mb-12">О нас</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
                <img src="/static/images/team.jpg" alt="Наша команда" class="rounded-lg mb-6">
            </div>
            <div>
                <h3 class="text-2xl font-semibold mb-4">Наша команда</h3>
                <p class="text-gray-700 mb-6">Мы - команда опытных разработчиков, увлеченных графовыми алгоритмами и их
                    применением в реальных задачах.</p>
                <p class="text-gray-700 mb-6">Мы стремимся сделать обучение и практику графовых алгоритмов доступными
                    для всех.</p>
                <a href="/authors" class="text-blue-500 font-semibold">Узнать больше о нашей команде</a>
            </div>
        </div>
    </div>
</section>

<!-- Секция "Контакты" -->
<section id="contact" class="py-20">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl font-semibold text-gray-800 mb-12">Контакты</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
                <p class="text-gray-700 mb-6">Если у вас возникли вопросы или вам нужна помощь, не стесняйтесь связаться
                    с нами.</p>
                <ul class="text-gray-700 mb-6">
                    <li>Email: pank@pank.su</li>
                    <li>Телефон: +7 962 7011087</li>
                </ul>
            </div>
            <div>
                <form id="message_form" action="/send_message" method="post">
                    <div class="mb-4">
                        <label for="name" class="text-gray-700">Ваше имя:</label>
                        <input type="text" id="name" name="name"
                               class="w-full rounded-lg p-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div class="mb-4">
                        <label for="email" class="text-gray-700">Ваш Email:</label>
                        <input type="email" id="email" name="email"
                               class="w-full rounded-lg p-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div class="mb-4">
                        <label for="message" class="text-gray-700">Сообщение:</label>
                        <textarea id="message" name="message"
                                  class="w-full rounded-lg p-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
                    </div>
                    <button type="submit" class="bg-blue-500 text-white py-2 px-4 rounded-lg">Отправить</button>
                </form>
            </div>
        </div>
        % if len(message) != 0:
        % if is_error:
        <div class="mt-10" role="alert">
            <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
                Ошибка
            </div>
            <div class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                <p>{{message}}</p>
            </div>
        </div>
        % else:
        <div class="mt-10 bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md" role="alert">
        <div class="flex">
            <div class="py-1"><svg class="fill-current h-6 w-6 text-teal-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
                <div>
                <p class="font-bold">Поздравляем</p>
                <p class="text-sm">{{message}}</p>
                </div>
            </div>
        </div>
        % end
        % end
    </div>
</section>
