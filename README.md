# Проект по автоматизации тестирования мобильного приложения интернет-магазина техники и электронники [Ситилинк](https://www.citilink.ru/) 


## :world_map: Содержание

- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Список реализованных проверок в автотестах](#white_check_mark-список-реализованных-проверок-в-автотестах)
- [Запуск тестов в Jenkins с параметрами](#rocket-Запуск-тестов-в-Jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#bar_chart-Отчет-о-результатах-тестирования-в-Allure-reports)
- [Статистика запуска тест-планов и отчеты в Allure TestOps](#bar_chart-Статистика-запуска-тест-планов-и-отчеты-в-Allure-TestOps)
- [Уведомление в Telegram о результатах прогона тестов с использованием бота](#email-Уведомление-в-Telegram-о-результатах-прогона-тестов-с-использованием-бота)
- [Видео-отчет прохождения Mobile-автотеста](#movie_camera-Видео-отчет-прохождения-автотеста)


## :dart: Цель проекта

Тестирование основных функций интернет-магазина, позволяющих найти нужный товар, добавить его с корзину или в список Избранных.


## :gear: Технологии и инструменты

<p align="left">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/python.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/jenkins.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/pycharm.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/pytest.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/github.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_mobile_project/blob/main/resources/images/AllureReport%20(1).png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_mobile_project/blob/main/resources/images/AllureTestOps.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_mobile_project/blob/main/resources/images/selene%20(1).png" height="50" width="50">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/browserstack.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_mobile_project/blob/main/resources/images/appium.png" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/android-studio.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_mobile_project/refs/heads/main/resources/images/Telegram.svg" width="50" heigth="50"/>
</p>


## :white_check_mark: Список реализованных проверок в автотестах 

## Mobile-тесты
- Поиск товара
- Добавление товара в корзину
- Добавление товара в раздел "Избранные"


## :rocket: Запуск тестов в Jenkins с параметрами

Сборка, параметризация и запуск проекта производятся с помощью Jenkins. При каждом запросе на тестирование браузера Selenoid запускает новый Docker-контейнер и останавливает его после закрытия браузера. 
Запуск тестов возможен как локально, так и удаленно через Jenkins.
Для локального запуска тестов с дефолтными значениями необходимо выполнить команду:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=bstack 
```

Удаленный запуск автотестов выполняется на сервере Jenkins. 
Для запуска автотестов в Jenkins необходимо:
1. Открыть сборку в Jenkins 
2. Нажать Build with parameters

По умолчанию используется конфиг BrowserStack. Для изменения конфига необходимо перед запуском тестов через pytest указать параметр context pytest --context=bstack / --context=local_emulator / --context=local_real_device в зависимости от того, где планируется запустить тесты.

По умолчанию используется конфиг BrowserStack

Результат запуска сборки можно посмотреть в отчёте Allure Report и в Allure TestOps


## :bar_chart: Отчет о результатах тестирования в Allure-reports

После прохождения тестов автоматически формируется отчет в Allure Report. Allure формирует подробный отчет о результатах прогона тестов. Кастомные фильтры и листенеры делают отчет максимально понятным. Например, в отчет пишутся все селекторы и методы Selene, отчеты формируются по категориям.
После окончания выполнения автотестов по каждому из них в отчете доступны скриншоты, лог консоли браузера и видеозапись выполнения теста.


Общий результат прогона тестов

<p>
<img title="Общий результат прогона" src="resources/photo/общий отчет api.png">
</p>

Список тестов

<p>
<img title="Список API тестов" src="resources/photo/Список API тестов.png">
</p>

Пример результата прохождения теста

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


### Пример результата прохождения теста

<p>
<img title="Пример API" src="resources/photo/результат api.png">
</p>


## :email: Уведомление в Telegram о результатах прогона тестов с использованием бота

Настроено автоматическое оповещение о результатах прохождения тестов в Telegram-бот с полной информацией о прогоне и ссылкой на Allure


### Результат прогона тестов 

<p>
<img title="Telegram" src="resources/photo/Результат прогона API тестов в Telegram.png">
</p>

## :movie_camera: Видео-отчет прохождения автотеста 

Пример видеозаписи выполнения теста в Browserstack.

<p>
<img title="Video" src="resources/video/bstack.gif" alt="video">
</p>

Пример видеозаписи выполнения теста на эмуляторе в Android Studio.

<p>
<img title="Video" src="resources/video/emulator.gif" alt="video">
</p>

Пример видеозаписи выполнения теста на реальном устройстве.

<p>
<img title="Video" src="resources/video/real.gif" alt="video">
</p>
