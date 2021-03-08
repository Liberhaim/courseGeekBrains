class Cell:
    amount = 0

    def __init__(self, amount):
        self.amount = amount
        amount += self.amount

    def check(parametr):
        def wrapper(*args):
            for obj in args:
                if not isinstance(obj, Cell):
                    raise ValueError(f'Обект {type(obj)} не является клетка ')
            return parametr(*args)

        return wrapper

    @check
    def __add__(self, other):
        return self.amount + int(other.amount)

    @check
    def __sub__(self, other):
        if self.amount - int(other.amount) == 0:
            return 'данный метод не может быть реализован т.к. произойдет анигиляция'
        else:
            return self.amount - int(other.amount)

    @check
    def __mul__(self, other):
        return self.amount * int(other.amount)

    @check
    def __truediv__(self, other):
        return self.amount / int(other.amount)

    def __str__(self):
        return str(self.amount)

    def make_order(self, order):
        string = ""
        for i in range(self.amount // order):
            string += f'{"*" * order}\n'
        return string + f'{"*" * (self.amount % order)}'


cell_1 = Cell(4)
cell_2 = Cell(16)
cell1 = cell_1 + cell_2
cell2 = cell_2 - cell_1
cell3 = cell_1 * cell_2
cell4 = cell_2 / cell_1

print(f'Результат: {cell1}, {cell2}, {cell3}, {cell3}')
print(cell_2.make_order(5))
