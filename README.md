<h1 id="Encrypte">Encrypte</h1>
<blockquote>
<p>Encrypte - программа для шифрования и дешифрования текста</p>
</blockquote>
<h1 id="-">Как запустить:</h1>
<details><summary><h3 id="-python-"><strong>Первый этап: установка python и нужных библиотек</strong></h3>
<h5 id="-python3-pygame-">Если у вас уже установлен python3 и вы можете самостоятельно установить библиотеки tkinter и string — пропустите этот этап</h5></summary>
<p><strong>1. Скачайте python3 с официального <a href="https://www.python.org/downloads/">сайта</a> и установите его.</strong> 
<p><strong>2. Во время установки <em>обязательно</em> поставьте галочку "Add Python 3.x to PATH".</strong></p> <p><img src="https://python-scripts.com/wp-content/uploads/2018/06/win-install-dialog.40e3ded144b0.png" alt="add path screenshot"></p>
<p><strong>3. Запустите консоль Windows любым удобным для вас способом (например набрав в поиске приложений cmd)</strong></p>
<p><strong>4. Установите нужные библиотеки используя команды</strong></p>
<blockquote>
<p>pip install T</p>
</blockquote>
</details>
<h3 id="-"><strong>Второй этап: запуск программы</strong></h3>
<p><strong>1. Скачайте проект с github любым удобным для вас способом (gitclone или по ссылке https://github.com/polinavenberg/Encrypte.git</a>.</strong></p>
<p><strong>2. В консоли перейдите в папку с игрой при помощи команды cd.</strong></p>
<p><strong>3. Запустите игру при помощи команды</strong></p>
<blockquote>
<p>python Encrypte.py</p>
</blockquote>
<p>для запуска в консоли, или</p>
<blockquote>
<p>python graphicEncrypte.py</p>
</blockquote>
<p>для запуска графического интерфейса</p>
<p><strong>4. Теперь вы можете приступить к шифрованию! </strong></p>
<h1 id="-"><strong>Интерфейс программы и доступные виды шифрования</strong></h1>
<p>В программе доступно 5 видов шифрования:</p>
<ul>
<li><details><summary>Шифр Цезаря</summary>
Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F">ссылка</a>
  <p>На вход подается файл с текстом, название файла, куда будет сохранен результат, и сдвиг.</p>
  <p>Также есть возможность расшифровать текст методом частотного анализа. Для этого на вход программе нужно загрузить только файл с зашифрованным текстом.</p>
<img src="https://b.radikal.ru/b04/2104/d6/ae100101e233.png" alt="скрин"></li>
  </details>
<li><details><summary>Шифр Виженера</summary>
Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0">ссылка</a>
  
<p>На вход подается файл с текстом, название файла, куда будет сохранен результат, и ключевое слово любой длины.</p>
<p><img src="https://d.radikal.ru/d40/2104/92/f1ee787c6404.png" alt="скрин"></p></li>
  </details>
<li><details><summary>Шифр Вернама</summary>
 Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B5%D1%80%D0%BD%D0%B0%D0%BC%D0%B0">ссылка</a>
<p>Работает почти как шифр Виженера, но ключ должен быть такой же по длине, как и шифруемый текст.</p>
  <p><img src="https://b.radikal.ru/b13/2104/56/fceb015371dc.png" alt="скрин"></p></li>
</details>
<li><details><summary>Азбука Морзе</summary>
Как работает: <a href="https://ru.wikipedia.org/wiki/%D0%90%D0%B7%D0%B1%D1%83%D0%BA%D0%B0_%D0%9C%D0%BE%D1%80%D0%B7%D0%B5">ссылка</a>
  <p>На вход подается файл с текстом и название файла, куда будет сохранен результат.</p>
<img src="https://b.radikal.ru/b34/2104/82/017e36feea33.png" alt="скрин"></li>
  </details>

<li><details><summary>Шифрование в картинку</summary>
<p>Зашифровывает текст в пиксели картинки так, что это практически незаметно для человеческого глаза. На вход подается файл с текстом, файл с картинкой в формате bmp и название файла, куда будет сохранен результат.</p>
  <p><img src="https://d.radikal.ru/d00/2104/f2/d8267dfd84da.png" alt="скрин"></p></li>
</details>
</ul>
<h2 id="-">Несколько примеров работы шифратора:</h2>
<p><strong>Шифр Цезаря</strong></p>
<p><img src="https://b.radikal.ru/b31/2104/c1/ea8c43301612.png" alt=""></p>
<p><strong>Шифрование в картинку</strong>
<img src="https://b.radikal.ru/b20/2104/43/871722b4cf51.png" alt=""></p>
<p><img src="https://b.radikal.ru/b42/2104/d4/9c82b80593db.png" alt=""></p>
