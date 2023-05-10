class GraphingCalculator:
    def __init__(self):
        self.polynomials = []
        self.poly = []
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10

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
        try:
            new_x_min = float(input("Enter your minimum value for x-axis: "))
            new_x_max = float(input("Enter your maximum value for x-axis: "))
            new_y_min = float(input("Enter your minimum value for y-axis: "))
            new_y_max = float(input("Enter your maximum value for y-axis: "))
            
            if new_x_min < new_x_max and new_y_min < new_y_max:
                self.x_max = new_x_max
                self.x_min = new_x_min
                self.y_max = new_y_max
                self.y_min = new_y_min
                print("Window corner changed.")
            else:
                print("Invalid input. Minimum value should be less than maximum value for both axes.")
        except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def newton_raphson(self, poly, poly_derivative, x0, epsilon=1e-6, max_iterations=1000):
        x = x0
        for i in range(max_iterations):
            x_new = x - self.evaluate_polynomial(poly, x) / self.evaluate_polynomial(poly_derivative, x)
            if abs(x_new - x) < epsilon:
                return x_new 
        return None
   
    def evaluate_polynomial(self, poly, x):
        result = 0
        for i, coeff in enumerate(poly):
            result += coeff * x ** (len(poly) - i - 1)
        return result
   
    def find_derivative(self, poly):
        derivative = []
        for i, coeff in enumerate(poly[:-1]):
            derivative.append(coeff * (len(poly) - i - 1))
        return derivative
                                  
    def determine_zeros(self):
        index = int(input("Enter the index of the polynomial to find zeros for: "))
        if 0 <= index < len(self.polynomials):
            poly = self.polynomials[index]
            poly_derivative = self.find_derivative(poly)
            x0 = float(input("Enter the initial guess for the zero: "))
            zero = self.newton_raphson(poly, poly_derivative, x0)
            if zero is not None:
                print(f"A zero of the polynomial is approximately {zero:.6f}.")
            else:
                print("Unable to find the zero with the given initial guess.")
        else:
            print("Invalid index. No zeros calculated.")
                       
    def determine_intersections(self):
        if len(self.polynomials) < 2:
            print("At least two polynomials are needed to find intersection.")
            return

        for i in range(len(self.polynomials)):
            for j in range(i+1, len(self.polynomials)):
                print(f"Finding intersections between polynomial {i+1} and polynomial {j+1}")
                intersection = self.find_intersection(self.polynomials[i], self.polynomials[j])
                if intersection is not None:
                    print(f"The polynomials intersect approximately at x = {intersection:.6f}")
                else:
                    print("Unable to find the intersection with the given initial guess.")
                       
    def find_intersection(self, poly1, poly2, x0=0, epsilon=1e-6, max_iterations=1000):
        diff_poly = [c1 - c2 for c1, c2 in zip_longest(poly1, poly2, fillvalue=0)]
        diff_poly_derivative = self.find_derivative(diff_poly)
                     
        x = x0
        for _ in range(max_iterations):
            x_new = x - self.evaluate_polynomial(diff_poly, x) / self.evaluate_polynomial(diff_poly_derivative, x)
            if abs(x_new -x) < epsilon:
                return x_new
        return None
               
    def display_screen(self):
        print("\nCurrent Polynomials: ")
        for i, equation in enumerate(self.poly):
            print(f"{i+1}: {equation}")
                     
        print(f"\nCurrent Window: X-axis [{self.x_min},{self.x_max}], Y-axis [{self.y_min}, {self.y_max}]\n")
      
    def menu(self):
        while True:
            print("\nOptions:")
            print("(1) Add Polynomial")
            print("(2) Remove Polynomial")
            print("(3) Change Window Corner")
            print("(4) Determine Zeros")
            print("(5) Determine Intersections")
            print("(6) EXIT")
            num = input ("Enter your option number: ")
            try:
                 num = int(num)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

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
