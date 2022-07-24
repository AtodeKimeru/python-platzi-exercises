def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Debes ingresar un número'
    num = int(num)
    assert num > 0, 'El número ingresado debe ser entero positivo'
    print(divisors(num))
    print('terminó mi programa')


if __name__=='__main__':
    run()