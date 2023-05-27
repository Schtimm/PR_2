% rebase('layout.tpl', title="Домашняя страница")


<header class="py-16 bg-blue-500 text-white">
    <div class="container mx-auto px-4">
        <h1 class="text-4xl font-semibold mb-4">Добро пожаловать на страницу Графовых Алгоритмов</h1>
        <p class="text-lg">Исследуйте мир графовых алгоритмов и решайте задачи, связанные с графами.</p>
    </div>
</header>

<!-- Секция с особенностями -->
<section id="features" class="py-20">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl font-semibold text-gray-800 mb-12">Особенности</h2>

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
                <form>
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
    </div>
</section>
