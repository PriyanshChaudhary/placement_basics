


class Employee:
    raise_amt = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{}  {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, lang):
        super().__init__( first, last, pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay, emps = None):
        super().__init__(first, last, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emps(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emps(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emps(self):
        for emp in self.emps:
            print('-->', emp.fullname())

dev1 = Employee('pussy', 'slayer', 20000)
dev2 = Developer('pussy', 'himself', 50000, 'python')

mng1 = Manager('tit', 'lover', 20000, [dev1] )
mng2 = Manager('ass', 'eater', 20000, [] )

print(issubclass(Developer,Manager))
