class MyMath:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass

    def addition(self, a, b):
        s = a + b
        if s % 1 == 0:
            return int(s)
        else:
            return s

    def multiplication(self, a, b):
        m = a * b
        if m % 1 == 0:
            return int(m)
        else:
            return m

    def division(self, a, b):
        if b != 0:
            d = a / b
            if a % b == 0:
                return int(d)
            else:
                return d
        else:
            d = 'На 0 делить нельзя!'
            return d

    def subtraction(self, a, b):
        s = a - b
        if s % 1 == 0:
            return int(s)
        else:
            return s

    def pow(self, a, b):
        p = a ** b
        if p % 1 == 0:
            return int(p)
        else:
            return p

    def sqrt(self, a):
        if a >= 0:
            sq = a ** 0.5
            if sq % 1 == 0:
                return int(sq)
            else:
                return sq
        else:
            sq = 'Невозможно извлечь корень'
            return sq


math = MyMath

while True:
    a = float(input('Введите первое число\n'))
    b = float(input('Введите второе число\n'))
    c = input('+, *, /, -, pow, sqrt\n')
    if c == '+':
        print(math.addition(math, a, b))
    elif c == '*':
        print(math.multiplication(math, a, b))
    elif c == '/':
        print(math.division(math, a, b))
    elif c == '-':
        print(math.subtraction(math, a, b))
    elif c == 'pow':
        print(math.pow(math, a, b))
    elif c == 'sqrt':
        print(math.sqrt(math, a))
    else:
        print('Такого действия нет')