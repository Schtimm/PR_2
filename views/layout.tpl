<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{title}}</title>
  <script src="/static/scripts/tailwindcss.js"></script>
   <link rel="stylesheet" type="text/css" href="/static/styles/style.css"/>
</head>

<body class="bg-gray-100">
  <nav class="bg-blue-500 py-4">
    <div class="container mx-auto flex items-center justify-between px-4">
      <a href="/" class="text-white text-lg font-semibold">Главная</a>
      <div>
        <a href="#" class="text-white px-4">Алгоритм поиска в ширину</a>
        <a href="#" class="text-white px-4">Алгоритм поиска в глубину</a>
        <a href="/crascal" class="text-white px-4">Алгоритм Краскала</a>
        <a href="/authors" class="text-white px-4">Об авторах</a>
      </div>
    </div>
  </nav>
  {{!base}}

  <footer class="bg-blue-500 py-4 mt-12">
    <div class="container mx-auto text-center">
      <p class="text-white">Все права защищены &copy; 2023</p>
    </div>
  </footer>

</body>

</html>
