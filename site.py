#!/bin/bash

PROJECT_NAME="my_first_website"

echo "========================================="
echo " 🌐 ГЕНЕРАТОР ВЕБ-САЙТА С ДИЗАЙНОМ"
echo "========================================="
echo "Создаем проект в папке ~/$PROJECT_NAME..."

# 1. Создаем структуру папок
mkdir -p "$HOME/$PROJECT_NAME/css"
mkdir -p "$HOME/$PROJECT_NAME/images"
cd "$HOME/$PROJECT_NAME"

# 2. Генерируем HTML-код страницы
cat << EOF > index.html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой Linux Проект</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <header>
        <h1>Приветик из терминала! 👋</h1>
        <p>Этот сайт был полностью сгенерирован с помощью Bash-скрипта.</p>
    </header>

    <main class="container">
        <section class="card">
            <h2>Как это работает?</h2>
            <p>Мы написали скрипт, который автоматически создал эту страницу, настроил папки и прописал стили CSS. Никакой рутины!</p>
        </section>

        <section class="card">
            <h2>Что дальше?</h2>
            <p>Теперь можно учиться настраивать сервер, поднимать базы данных и, конечно же, разворачивать свой собственный крутой VPN.</p>
        </section>
    </main>

    <footer>
        <p>Создано на Linux-сервере в $PROJECT_NAME &copy; $(date +%Y)</p>
    </footer>

</body>
</html>
EOF

# 3. Генерируем CSS-код для стиля страницы
cat << 'EOF' > css/style.css
/* Общие настройки для всей страницы */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f7f6;
    color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* Красивая шапка сайта */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    padding: 40px 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

header h1 {
    margin: 0;
    font-size: 2.5rem;
}

header p {
    margin: 10px 0 0 0;
    opacity: 0.9;
}

/* Контейнер для блоков по центру */
.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    display: flex;
    gap: 20px;
    flex-grow: 1;
}

/* Стильные карточки с контентом */
.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    flex: 1;
    transition: transform 0.2s;
}

.card:hover {
    transform: translateY(-5px);
}

.card h2 {
    color: #764ba2;
    margin-top: 0;
}

/* Подвал (футер) */
footer {
    background-color: #2d3748;
    color: #a0aec0;
    text-align: center;
    padding: 15px;
    font-size: 0.9rem;
    margin-top: auto;
}
EOF

echo "-----------------------------------------"
echo "🎉 Готово! Проверь папку ~/$PROJECT_NAME"
echo "========================================="
