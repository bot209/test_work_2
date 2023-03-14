- Тестовое задание №2
# Для запуска тестов необходимо:
#### 1. Установить Python - https://www.python.org/downloads/, при установке обязательно ставим галочку "Add Python to PATH"
#### 2. Установить Git - https://git-scm.com/downloads, для работы с git репозиториями на своем устройстве
#### 3. Установить браузеры Chrome/Firefox
#### 4. Клонировать репозиторий "test_work_2" на свое устройство
        
       git clone https://github.com/bot209/test_work_2.git

#### 5. Установить пакеты из файла requirements.txt
        
       pip install -r requirements.txt
        
#### 6. Запустить тесты:

Для браузера Chrome:
        
       pytest -s -v --browser_name=chrome test_element_page.py

Для браузера FireFox:
        
       pytest -s -v --browser_name=firefox test_element_page.py
        
