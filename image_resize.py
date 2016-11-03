# -*- coding: utf-8 -*-
import argparse
import os
import sys
from PIL import Image

IMAGE_RESIZE_OK = 0
IMAGE_RESIZE_BAD_PARAMS = 1
IMAGE_RESIZE_WRONG_OUTPUT_FORMAT = 2
IMAGE_RESIZE_BAD_INPUT_IMAGE = 3


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', '--i', help='Путь исходного файла')
    # знаю про required=True, но сообщение об ошибке при этом не очень понятное
    parser.add_argument('--width', '--w', help='Ширина конечной картинки',
                        type=int)
    parser.add_argument('--height', '--h', help='Высота конечной картинки',
                        type=int)
    parser.add_argument('--scale', '--s', help='Масштаб конечной картинки',
                        type=float)
    parser.add_argument('--outfile', '--o', help='Путь конечного файла')

    return parser


def resize_image(infile: str, width: int, height: int, scale: float,
                 outfile: str) -> (int, str):
    """
    Изменение размеров изображений по заданным параметрам
    :param infile: путь к входной картинка
    :param width: конечная ширина
    :param height: конечная высота
    :param scale: масштаб, может быть меньше 1
    :param outfile: путь к выходной картинке
    :return: код ошибки, название конечного файла
    """
    if width == 0 or height == 0 or scale == .0:
        return IMAGE_RESIZE_BAD_PARAMS, None
    if scale and (width or height):
        return IMAGE_RESIZE_BAD_PARAMS, None

    try:
        img = Image.open(infile)
    except IOError:
        return IMAGE_RESIZE_BAD_INPUT_IMAGE, None

    try:
        if scale:
            scale = abs(float(scale))
            width = round(img.width * scale)
            height = round(img.height * scale)
        else:
            if width:
                width = abs(int(width))
                height = round(width / (img.width / img.height))
            elif height:
                height = abs(int(height))
                width = round(height * (img.width / img.height))
        tmp = img.resize((width, height), Image.ANTIALIAS)
    except (TypeError, ValueError, ArithmeticError, OverflowError):
        return IMAGE_RESIZE_BAD_PARAMS, None

    name, ext = os.path.splitext(infile)
    if not outfile:
        outfile = '{0}__{1}x{2}{3}'.format(name, tmp.width, tmp.height, ext)
    try:
        tmp.save(outfile)
    except KeyError:  # Невозможно определить формат по имени выходного файла
        return IMAGE_RESIZE_WRONG_OUTPUT_FORMAT, None
    finally:
        tmp.close()

    return IMAGE_RESIZE_OK, outfile


def main():
    enable_win_unicode_console()

    args_parser = get_args_parser()
    args = get_args_parser().parse_args()

    if not args.infile:
        print('Вы не задали путь к исходной картинке')
        args_parser.print_usage()
        exit(1)
    if args.scale and (args.width or args.height):
        print('Нельзя одновременно задавать масштаб и ширину или высоту')
        args_parser.print_usage()
        exit(1)
    elif not args.width and not args.height and not args.scale:
        print('Вы не задали ни ширину, ни высоту, ни масштаб')
        args_parser.print_usage()
        exit(1)

    try:
        error, final_file = resize_image(args.infile, args.width, args.height,
                                         args.scale, args.outfile)
        if error:
            if error == IMAGE_RESIZE_BAD_PARAMS:
                print('Ошибка: неверные параметры')
            elif error == IMAGE_RESIZE_BAD_INPUT_IMAGE:
                print('Ошибка: Исходное изображение некорректно')
            elif error == IMAGE_RESIZE_WRONG_OUTPUT_FORMAT:
                print('Ошибка: Имя конечного файла некорректно')
            exit(1)
        else:
            print('Файл обработан и сохранён как %s' % final_file)
    except OSError as error:
        print('Ошибка: %s в файле: %s' % (error.strerror, error.filename))
        exit(1)


if __name__ == '__main__':
    main()
