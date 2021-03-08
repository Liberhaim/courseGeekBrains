"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self):
        print('>>> Склад оргтехники: ')


class OfficeEquipment(Storage):
    def param(self, paper_size, type_ink, value):
        self.paper_size = paper_size
        self.type_ink = type_ink  # тип чернил
        self.type_value = value
        print(f'Виды оргтехники: \n Принтер {self.type_ink}, Cканер ({self.paper_size}), ксерокс ({self.type_value})')


class Printer(OfficeEquipment):
    def param_printer(self, type_printer):
        self.type_printer = type_printer
        return print(f'Тип принтера: {self.type_printer}')


class Copier(OfficeEquipment):
    def param_copier(self, format):
        self.format = format
        print(f'Формат ксерокса: {self.format}')


class Scanner(OfficeEquipment):
    def param_scanner(self, name):
        self.name = name
        print(f'Производитель сканера: {self.name}')


office = OfficeEquipment()
office.param("a4", "water", 13)
pr = Printer()
pr.param_printer("Laser")
copier = Copier()
copier.param_copier("А0")
sc = Scanner()
sc.param_scanner("LG")
