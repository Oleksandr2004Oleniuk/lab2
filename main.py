import math

class Calculator:
    def __init__(self, decimal_places=2):
        self.result = None
        self.decimal_places = decimal_places

    def get_operator_input(self):
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if operator not in ('+', '-', '*', '/', '^', '√', '%'):
            raise ValueError("Недійсний оператор.")
        return operator

    def get_number_input(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print("Помилка: Введіть дійсне число.")

    def calculate(self, num1, operator, num2):
        try:
            if operator == '+':
                self.result = num1 + num2
            elif operator == '-':
                self.result = num1 - num2
            elif operator == '*':
                self.result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Помилка: Ділення на нуль неможливе.")
                    self.result = None
                else:
                    self.result = num1 / num2
            elif operator == '^':
                self.result = num1 ** num2
            elif operator == '√':
                if num1 < 0:
                    print("Помилка: Неможливо взяти корінь з від'ємного числа.")
                    self.result = None
                else:
                    self.result = math.sqrt(num1)
            elif operator == '%':
                self.result = num1 % num2
            else:
                raise ValueError("Недійсний оператор.")
        except Exception as e:
            print(f"Помилка: {str(e)}")

    def display_result(self):
        if self.result is not None:
            print(f"Результат: {self.result:.{self.decimal_places}f}")  # Виведення з вказаною кількістю знаків після коми
        else:
            print("Помилка: Неможливо вивести результат.")

    def perform_calculations(self):
        while True:
            num1 = self.get_number_input("Введіть перше число: ")
            operator = self.get_operator_input()
            num2 = self.get_number_input("Введіть друге число: ")

            self.calculate(num1, operator, num2)
            self.display_result()

            repeat = input("Бажаєте виконати ще одне обчислення? (Так/Ні): ").lower()
            if repeat != "так":
                break

if __name__ == "__main__":
    decimal_places = int(input("Введіть кількість знаків після коми: "))
    calc = Calculator(decimal_places)
    calc.perform_calculations()