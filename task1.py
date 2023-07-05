# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# C:\Users\Honor\Desktop\Обучение тестировщик\Погружение в Python\5 Итераторы и генераторы\Семинар 5. Погружение в Python. Итераторы и генераторы.pdf


def abs_link(abs: str) -> tuple:
    list_abs_link = link.split('\\')
    *a, b = list_abs_link
    list_last_elem = b.split('.')
    path = "\\".join(a)
    name = b
    expansion = list_last_elem[-1]
    return path, name, expansion

if __name__ == '__main__':
    link = input("Введите абсолютный путь до файла: ")
    print(abs_link(link))

