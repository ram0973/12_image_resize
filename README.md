# Решение задачи [№12](https://devman.org/challenges/12/) с сайта [devman.org](https://devman.org)

## Условие задачи:

Написать скрипт, который принимает на вход изображение и кладёт 
изображение с новым размером, куда скажет пользователь или рядом с исходным. 
У него есть обязательный аргумент – путь до исходной картинки. 
И несколько необязательных: 
width - ширина результирующей картинки, 
height - её высота, 
scale - во сколько раз увеличить изображение (может быть меньше 1), 
output - куда класть результирующий файл.

Логика работы такая:

Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. 
И наоборот, если указана и ширина и высота – создать именно такое изображение. 
Вывести в консоль предупреждение, если пропорции не совпадают с исходным изображением.
Если указан масштаб, то ширина и высота указаны быть не могут. 
Иначе никакого ресайза не происходит и скрипт ломается с понятной ошибкой.
Если не указан путь до финального файла, то результат кладётся рядом с 
исходным файлом. Если исходный файл называется pic.jpg (100x200),
 то после вызова python image_resize.py --scale 2 pic.jpg должен 
 появиться файл pic__200x400.jpg.

Для работы с изображениями можно использовать Pillow, а для работы с 
аргументами скрипта – модуль argparse (он входит в стандартную библиотеку 
и его не нужно устанавливать).

Скрипт должен работать хотя бы с jpg и png.

## Системные требования

```
Python 3.5.2+
Внешний модуль win-unicode-console
Внешний модуль pillow
```

## Установка

Windows

```    
git clone https://github.com/ram0973/12_image_resize.git
cd 12_image_resize
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/12_image_resize.git
cd 12_image_resize
pip3 install -r requirements.txt
```
    
## Описание работы

Пользователь вводит обязательный аргумент - путь до исходной картинки и 
четыре необязательных. Скрипт изменяет размеры картинки и сохраняет, как 
указано в условии задачи. Работает как минимум с jpg, png, tif, bmp, tga. 
В gif сохраняет, но получившийся gif не может обработать.

## Запуск

Windows

```
python image_resize.py --i путь_до_исходной_картинки
```
 
Linux

``` 
python3 image_resize.py --i путь_до_исходной_картинки 
```

Пример необязательных параметров:
``` 
python3 image_resize.py --i original_image.jpg --w 200 --h 100 --s 0.5 --o image_scaled.jpg
```

 
## Лицензия

[MIT](http://opensource.org/licenses/MIT)