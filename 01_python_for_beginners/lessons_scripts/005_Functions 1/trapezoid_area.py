# площадь трапеций s = a + b / 2 * h

def search_area(a, b, h):
    return (a + b) / 2 * h


if __name__ == '__main__':
    number_a = int(input('Введите первую грань: '))
    number_b = int(input('Введите вторую грань: '))
    number_h = int(input('Введите третью грань: '))

    print(search_area(number_a, number_b, number_h))
