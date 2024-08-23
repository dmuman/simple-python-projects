# -*- coding: utf-8 -*-
import os
import random
# import string


# визначаємо директорію через абсолютний шлях
scriptDir = os.path.dirname(os.path.abspath(__file__))  # директорія скрипта


# 1. Створення папки
def createFolder(folderName: str = "New Folder") -> str:
    """
    Створює папку із заданою назвою.
    Додає до назви номер, у зростаючому порядку,
    починаючи з 1, якщо папка з заданим іменем вже існує.
    Повертає назву створеної папки (це потрібно у випадку, 
    якщо папка з таким іменем вже існує, щоб нові файли не створювались 
    у старій папці).
    Повертає текст помилки, якщо вона є.

    Вимагає:
    forderName - не пустий стрінг.
    За замовчуванням назва "New Folder".

    Запевняє:
    Створено нову папу з заданою назвою.
    Повернено назву створеної папки.
    Повертає текст помилки, якщо вона є.
    """
    originalName = folderName
    global folderNum        # глобальна змінна для підрахування кількості папок з однаковою назвою
    folderNum = 1

    # розташування нової папки буде в одній директорії зі скриптом
    folderPath = os.path.join(scriptDir, folderName)

    # якщо така папка вже існує
    while os.path.exists(folderPath):
        folderName = f'{originalName} ({folderNum})'
        folderPath = os.path.join(scriptDir, folderName)
        # додаємо до нової папки номер
        folderNum += 1

    # створюємо папку, якщо немає помилок
    try:
        os.mkdir(folderPath)
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'

    return folderName


# 2. Створити 3 нові текстові файли в новій папці
def createFiles(folderName: str, numFiles: int = 3) -> str | None:
    """
    Створює задану кількість файлів у заданій папці.
    За замовчуванням - кількість файлів = 3.
    Якщо папки із заданим іменем не існує - створюється нова папка
    за допомогою функції `createFolder()`.
    Повертає текст помилки, якщо вона є.

    Вимагає:
    forderName - не пустий стрінг, назва цільової папки.
    numFiles - додатнє ціле число. 
    За замовчуванням = 3.

    Запевняє:
    Створено задану кількість пустих файлів у заданій папці.
    Повертає текст помилки, якщо вона є.
    """
    # шлях до цільової папки
    folderPath = os.path.join(scriptDir, folderName)
    try:
        if folderName not in os.listdir(scriptDir): # перевіряємо, чи існує папка
            createFolder(folderName)                # створюємо, якщо ні

        for i in range(1, numFiles + 1):            # створюємо задану кількість файлів
            filePath = os.path.join(folderPath, f'file ({i}).txt')
            open(filePath, 'w').close()             # робимо файли пустими
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'


# 3. Організувати зміну розширення цих файлів, через запит
def changeExtension(folderName: str) -> str | None:
    """
    Змінює розширення всіх файлів (пофайлово)
    у заданій папці за допомогою запиту нового 
    розширення у консолі.
    Якщо папка пуста - повертає  відповідне повідомлення.
    Повертає текст помилки, якщо вона є.

    Вимагає:
    folderName - не пустий стрінг, назва цільової папки.

    Запевняє:
    Розширення усіх файлів у папці змінено на ті,
    що користувач ввів в консоль.
    Повертає текст про те, що цільова папка пуста, 
    якщо вона пуста.
    Повертає текст помилки, якщо вона є.  
    """
    # шлях до цільової папки
    folderPath = os.path.join(scriptDir, folderName)
    try:
        if len(os.listdir(folderPath)) == 0:    # перевіряємо, чи папка пуста
            print(f"Папка {folderName} пуста")  # повертаємо відповідне повідомлення, якщо так
            return f"Папка {folderName} пуста"
        else:   # якщо ж не пуста
            for file in os.listdir(folderPath):
                filePath = os.path.join(folderPath, file)       # шлях до файлу
                fileName, oldExtension = os.path.splitext(file) # ділимо шлях на його назву та розширення

                if os.path.isfile(filePath):            # перевіряємо, чи файл є дійсно файлом
                    newExtension = input(f"Введіть новий тип даних для файлу {file}: ") # запитуємо про нове розширення
                    if newExtension and not newExtension.startswith('.'):   # якщо розширення було введено та без крапки
                        newExtension = f'.{newExtension}'   # додаємо крапку

                    # створюємо нове ім'я та шлях
                    newFileName = f'{fileName}{newExtension}'
                    newFilePath = os.path.join(folderPath, newFileName)

                    # змінюємо шлях
                    os.rename(filePath, newFilePath)
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'


# 4. Організувати заповнення цих файлів будь-якими даними через введення з консолі
def fillFiles(folderName: str) -> str | None:
    """
    Заповнює усі файли (пофайлово) у заданій папці 
    даними, які було введено користувачем у консоль.
    Якщо папка пуста - повертає  відповідне повідомлення.
    Повертає текст помилки, якщо вона є.

    Вимагає:
    folderName - не пустий стрінг, назва цільової папки.

    Запевняє:
    Усі файли у папці наповнено даними, які 
    користувач ввів у консоль.
    Повертає текст про те, що цільова папка пуста, 
    якщо вона пуста.
    Повертає текст помилки, якщо вона є. 
    """
    # шлях до цільової папки
    folderPath = os.path.join(scriptDir, folderName)
    try:
        
        if len(os.listdir(folderPath)) == 0:    # перевіряємо, чи папка пуста
            
            print(f"Папка {folderName} пуста")  # повертаємо відповідне повідомлення, якщо так
            return f"Папка {folderName} пуста"
        else:   # якщо ж не пуста
            for file in os.listdir(folderPath):
                filePath = os.path.join(folderPath, file)   # шлях до файлу
                with open(filePath, 'a') as f:      # відкриваємо файл для наповнення
                    toWrite = input(f'Введіть дані, якими треба заповнити файл {file}: ')   # запитуємо про дані, якими треба наповнити файл
                    f.write(f'{toWrite}\n')         # записуємо дані у файл
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'


# 5. Перевірити розміри файлів. Якщо розмір менше 5000 символів, збільшити розмір файлу до 5000 символів, випадковими текстовими даними
def adjustSize(folderName: str) -> str | None:
    """
    Заповнює пусте місце у всіх файлах (пофайлово) 
    у заданій папці випадковими текстовими даними, 
    якщо файл містить менш, ніж 5000 символів.
    Пусте місце дорівнює 5000 - кількості символів у файлі.
    Якщо папка пуста - повертає  відповідне повідомлення.
    Повертає текст помилки, якщо вона є.

    Вимагає:
    folderName - не пустий стрінг, назва цільової папки.

    Запевняє:
    Усі пусті місця у всіх файлах у папці 
    наповнено випадковими текстовими даними, 
    якщо файл містить менш, ніж 5000 символів.
    Повертає текст про те, що цільова папка пуста, 
    якщо вона пуста.
    Повертає текст помилки, якщо вона є. 
    """
    # змінні для символів
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    letters = lower + upper
    # можна використати `letters = string.ascii_letters`,
    # але тоді треба імпортувати бібліотеку `string`

    # шлях до цільової папки
    folderPath = os.path.join(scriptDir, folderName)
    try:
        if len(os.listdir(folderPath)) == 0:    # перевіряємо, чи папка пуста
            print(f"Папка {folderName} пуста")  # повертаємо відповідне повідомлення, якщо так
            return f"Папка {folderName} пуста"
        else:   # якщо ж не пуста
            for file in os.listdir(folderPath):
                filePath = os.path.join(folderPath, file)           # шлях до файлу
                with open(filePath, 'r+', encoding='utf-8') as f:   # відкриваємо файл як 'r+', щоб читати і дописувати
                    data = f.read()             # читаємо файл
                    if len(data) < 5000:        # перевіряємо довжину
                        missingData = 5000 - len(data)
                        # додаємо випадкові текстові дані, якщо довжина менш, ніж 5000
                        f.write(''.join(random.choices(letters, k=missingData)))
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'


# 6. Вивести кількість символів "a" у всіх файлах
def countA(folderName: str) -> int | str:
    """
    Рахує кількість літер "а" у всіх файлах.
    Повертає значення для кожного файлу,
    а також загальну кількість у всіх файлах.
    Якщо папка пуста - повертає  відповідне повідомлення.
    Повертає текст помилки, якщо вона є.

    Вимагає:
    folderName - не пустий стрінг, назва цільової папки.

    Запевняє:
    Пише у консоль кількість літер "а" у кожному файлі,
    а також повертає загальну кількість у всіх файлах.
    totalA - додатнє ціле число.
    Повертає текст про те, що цільова папка пуста, 
    якщо вона пуста.
    Повертає текст помилки, якщо вона є. 
    """
    # загальна кількість літер "а"
    totalA = 0

    # шлях до цільової папки
    folderPath = os.path.join(scriptDir, folderName)
    try:
        if len(os.listdir(folderPath)) == 0:    # перевіряємо, чи папка пуста
            print(f"Папка {folderName} пуста")  # повертаємо відповідне повідомлення, якщо так
            return f"Папка {folderName} пуста"
        else:   # якщо ж не пуста
            for file in os.listdir(folderPath):
                filePath = os.path.join(folderPath, file)   # шлях до файлу
                with open(filePath, 'r') as f:  # відкриваємо файл для читання
                    data = f.read()
                    numA = data.count('a')      # рахуємо кількість літер "а" функцією `count()`
                    print(f'Кількість літер "а" у файлі {file}: {numA}')    # виводимо у консоль кількість у файлі
                    totalA += numA              # збільшуємо загальну кількість
            
            print(f'Загальна кількість літер "а" у всіх файлах: {totalA}')  # повертаємо загальну кількість
            return totalA
    
    # повертаємо помилку
    except Exception as e:
        print(f'Виникла помилка: {e}')
        return f'Виникла помилка: {e}'

# 7. В процесі виконання виконувати необхідні контролі
if __name__ == "__main__":
    folderName = input("Введіть назву папки: ") # запитуємо назву папки
    createdFolder = createFolder(folderName)    # створюємо змінну для назви, щоб перевіряти, чи така папка вже існує
    createFiles(createdFolder)                  # створюємо файли
    changeExtension(createdFolder)              # змінюємо розширення
    fillFiles(createdFolder)                    # наповнюмо файли даними
    adjustSize(createdFolder)                   # наповнюмо файли випадковими даними, якщо довжина файлу < 5000 символів
    countA(createdFolder)                       # рахуємо кількість літер "а"