class GraphingCalculator:
    def __init__(self):
        self.polynomials = []
        self.graph = g
        self.poly = p

    def add_polynomial(self, coeffs):
        self.polynomials.append(coeffs)
        symbol = chr(ord('A') + len(self.polynomials) - 1)
        equation = "{}: ".format(symbol)
        for i, coeff in enumerate(coeffs):
            if i > 0:
                equation += " + " if coeff >= 0 else " - "
            equation += "{:.2f}x^{}".format(abs(coeff), len(coeffs) - i - 1)
        self.poly.append(equation)

    def remove_polynomial(self, index):
        if 0 <= index < len(self.polynomials):
            self.polynomials.pop(index)
            self.poly.pop(index)
        else:
            print("Invalid index. No polynomial removed.")

    def change_window_corner(self):
        print("Change Window Corner functionality not implemented yet.")

    def determine_zeros(self):
        print("Determine Zeros functionality not implemented yet.")

    def determine_intersections(self):
        print("Determine Intersections functionality not implemented yet.")

    def display_screen(self):
        displayScreen(self.graph, self.poly)

    def menu(self):
        while True:
            print("\nOptions:")
            print("(1) Add Polynomial")
            print("(2) Remove Polynomial")
            print("(3) Change Window Corner")
            print("(4) Determine Zeros")
            print("(5) Determine Intersections between")
            print("(6) EXIT")
            num = checkAndConvert(input("Enter your option number: "))

            if num == 1:
                coeffs = input("Enter the coefficients of the polynomial separated by spaces: ")
                coeffs_list = [float(x) for x in coeffs.split()]
                self.add_polynomial(coeffs_list)
                print("Polynomial added.")
            elif num == 2:
                index = int(input("Enter the index of the polynomial to remove: "))
                self.remove_polynomial(index - 1)
                print("Polynomial removed.")
            elif num == 3:
                self.change_window_corner()
            elif num == 4:
                self.determine_zeros()
            elif num == 5:
                self.determine_intersections()
            elif num == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")

            self.display_screen()

def main():
    calculator = GraphingCalculator()
    calculator.menu()

if __name__ == "__main__":
    main()
