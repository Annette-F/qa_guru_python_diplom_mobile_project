# Проект по автоматизации тестирования мобильного приложения интернет-магазина техники и электронники [Ситилинк](https://www.citilink.ru/) <img src="https://github.com/Annette-F/qa_guru_python_diplom_mobile_project/blob/main/resources/images/%D0%A1%D0%B8%D1%82%D0%B8%D0%BB%D0%B8%D0%BD%D0%BA.png" height="50" width="150">


## :world_map: Содержание

- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Список реализованных проверок в автотестах](#white_check_mark-список-реализованных-проверок-в-автотестах)
- [Запуск тестов в Jenkins с параметрами](#rocket-Запуск-тестов-в-Jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#bar_chart-Отчет-о-результатах-тестирования-в-Allure-reports)
- [Статистика запуска тест-планов и отчеты в Allure TestOps](#bar_chart-Статистика-запуска-тест-планов-и-отчеты-в-Allure-TestOps)
- [Уведомление в Telegram о результатах прогона тестов с использованием бота](#email-Уведомление-в-Telegram-о-результатах-прогона-тестов-с-использованием-бота)
- [Видео-отчет прохождения UI-автотеста на Selenoid](#movie_camera-Видео-отчет-прохождения-UI-автотеста-на-Selenoid)
- [Видео-отчет прохождения Mobile-автотеста](#movie_camera-Видео-отчет-прохождения-Mobile-автотеста)


#### <img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/litres.svg" width="70" heigth="70"/> [Сайт онлайн-сервиса Litres](https://www.litres.ru/)


## :dart: Цель проекта

Тестирование основных функций онлайн-сервиса, позволяющих пользователям пройти успешную авторизацию, найти интересующую книгу, добавить книгу в корзину, 
добавить книгу в список отложенных книг. А также отсутствиии авторизации при неверно указанном пароле.


## :gear: Технологии и инструменты

<p align="left">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/python.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/jenkins.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/pycharm.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/pytest.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/github.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/AllureReport%20(1).png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/AllureTestOps.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/Selenoid%20(1).png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/selene%20(1).png" height="50" width="50">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/browserstack.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/appium.png" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/Telegram.svg" width="50" heigth="50"/>
</p>


## :white_check_mark: Список реализованных проверок в автотестах 

## UI-тесты

- Проверка успешной авторизации пользователя
- Проверка отсутствия авторизации при вводе неверного пароля
- Разлогин пользователя
- Поиск книги через строку поиска по автору
- Поиск книги через каталог по жанру
- Добавление книги в "Отложенные"
- Создание списка книг
- Добавление книги в корзину
- Удаление книги из корзины

## API-тесты

- Добавление книги в корзину
- Поиск печатной книги по названию и автору
- Неуспешный поиск печатной книги по названию
- Добавление книги в "Отложенные"
- Удаление книги из "Отложенных"
- Авторизация с неверно указанным паролем

## Mobile-тесты



## :rocket: Запуск тестов в Jenkins с параметрами

Сборка, параметризация и запуск проекта производятся с помощью Jenkins. При каждом запросе на тестирование браузера Selenoid запускает новый Docker-контейнер и останавливает его после закрытия браузера. Перед запуском можно указать версию браузера (в данном случае запуск тестов проводился на браузере Chrome версии 125.0). Также в параметрах добавлена возможность выбора набора тестов (UI или API), на которые будут запущены. 


## :bar_chart: Отчет о результатах тестирования в Allure-reports

После прохождения тестов автоматически формируется отчет в Allure Report. Allure формирует подробный отчет о результатах прогона тестов. Кастомные фильтры и листенеры делают отчет максимально понятным. Например, в отчет пишутся все селекторы и методы Selene, отчеты формируются по категориям.
После окончания выполнения автотестов по каждому из них в отчете доступны скриншоты, лог консоли браузера и видеозапись выполнения теста.

Общий результат прогона UI-тестов

<p>
<img title="Общий результат прогона" src="resources/photo/общий отчет ui.png">
</p>

Список UI-тестов

<p>
<img title="Список API тестов" src="resources/photo/список UI тестов.png">
</p>

Пример результата прохождения UI-теста

<p>
<img title="Пример API теста" src="resources/photo/результат ui.png">
</p>

Общий результат прогона API-тестов

<p>
<img title="Общий результат прогона" src="resources/photo/общий отчет api.png">
</p>

Список API-тестов

<p>
<img title="Список API тестов" src="resources/photo/Список API тестов.png">
</p>

Пример результата прохождения API-теста

<p>
<img title="Пример API теста" src="resources/photo/отчет api.png">
</p>

## :bar_chart: Статистика запуска тест-планов и отчеты в Allure TestOps

Также настроена интеграция с Allure TestOps., что продоставлят возможность просмотра результата выполнения автотестов, создания ручных тестов, а также через запуск автотестов. В Allure TestOps разработана удобная система предоставления отчетов по результатам запуска тестов. 

### Пример Dashboard с общими результатами тестирования

<p>
<img title="Вфырищфкв" src="resources/photo/дашборд.png">
</p>

### Общий список всех кейсов, имеющихся в системе

<p>
<img title="Список кейсов" src="resources/photo/тест кейсы.png">
</p>

### Пример результата прохождения UI-теста

<p>
<img title="Пример теста" src="resources/photo/результат запуска теста.png">
</p>

### Пример результата прохождения API-теста

<p>
<img title="Пример API" src="resources/photo/результат api.png">
</p>


## :email: Уведомление в Telegram о результатах прогона тестов с использованием бота

Настроено автоматическое оповещение о результатах прохождения тестов в Telegram-бот с полной информацией о прогоне и ссылкой на Allure

### Результат прогона UI-тестов

<p>
<img title="Telegram" src="resources/photo/Результат прогона UI тестов в Telegram.png">
</p>

### Результат прогона API-тестов 

<p>
<img title="Telegram" src="resources/photo/Результат прогона API тестов в Telegram.png">
</p>

## :movie_camera: Видео-отчет прохождения UI-автотеста на Selenoid

Пример видеозаписи выполнения UI-теста.

<p>
<img title="Video" src="resources/video/videoUI.gif" alt="video">
</p>
