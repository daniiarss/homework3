class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance

def create_file(filename):
    with open(filename, 'w'):
        pass

create_file('new_file.txt')

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num2

    def __mul__(self, other):
        return self.num1 * other.num2

    def __truediv__(self, other):
        if other.num2 != 0:
            return self.num1 / other.num2
        else:
            return "Error: Division by zero"

calc1 = Calculator(10, 4)
calc2 = Calculator(4, 2)

print("Addition:", calc1 + calc2)
print("Subtraction:", calc1 - calc2)
print("Multiplication:", calc1 * calc2)
print("Division:", calc1 / calc2)

bank_account = Bank("John", 1000)
print("Current balance:", bank_account._balance)
bank_account.moneyX()
print("Updated balance after deposit:", bank_account._balance)
