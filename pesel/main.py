
class Pesel:
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        control_sum = 0
        for index, j in enumerate(self.pesel):
            if (index == 10):
                break
            digit = int(j)
            control_sum += digit * self.weights[index]

        modulo = control_sum % 10
        if modulo == 0:
            if modulo != int(self.pesel[10]):
                return False

            return True

        sum_control = 10 - modulo
        if (sum_control != int(self.pesel[10])):
            return False
        return True

    def check_sex(self):
        if int(self.pesel[9]) % 2 == 0:
            return "K"
        else:
            return "M"

    def show_data(self):
        print(f"Płeć: {self.check_sex()}")
        if (pesel.is_valid()):
            print("Pesel jest poprawny")
        else:
            print("Pesel jest niepoprawny")


pesel = Pesel(input("Podaj pesel: "))


pesel.show_data()
