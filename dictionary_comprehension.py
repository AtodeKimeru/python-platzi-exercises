from numpy import sqrt


def run():
    dic = {i: round(sqrt(i), 3) for i in range(1, 1001)}
    print(dic)


if __name__ == '__main__':
    run()