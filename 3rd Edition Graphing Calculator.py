class GraphingCalculator:
    def __init__(self):
        self.polynomials = []
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10
        self.resolution = 40

    def add_polynomial(self, coeffs):
        self.polynomials.append(coeffs)

    def remove_polynomial(self, index):
        if 0 <= index < len(self.polynomials):
            self.polynomials.pop(index)
        else:
            print("Invalid index. No polynomial removed.")

    def change_window_corner(self, new_x_min, new_x_max, new_y_min, new_y_max):
        if new_x_min < new_x_max and new_y_min < new_y_max:
            self.x_max = new_x_max
            self.x_min = new_x_min
            self.y_max = new_y_max
            self.y_min = new_y_min
            print("Window corner changed.")
        else:
            print("Invalid input. Minimum value should be less than maximum value for both axes.")

    def evaluate_polynomial(self, coeffs, x):
        result = 0
        for i, coeff in enumerate(coeffs):
            result += coeff * x ** (len(coeffs) - i - 1)
        return result

    def evaluate_function(self, function, x):
        safe_dict = {'x': x}
        try:
            result = eval(function, safe_dict)
            return result
        except Exception as e:
            print("Error evaluating the function:", str(e))
            return None


    def plot_polynomials(self):
        data = [[' ' for _ in range(self.resolution)] for _ in range(self.resolution)]

        for poly in self.polynomials:
            for i in range(self.resolution):
                x = self.x_min + i * (self.x_max - self.x_min) / (self.resolution - 1)
                y = self.evaluate_polynomial(poly, x)
                j = int((y - self.y_min) * (self.resolution - 1) / (self.y_max - self.y_min))
                if 0 <= j < self.resolution:
                    data[self.resolution - 1 - j][i] = '*'

        for row in data:
            print(''.join(row))

    def plot_function(self, function):
        data = [[' ' for _ in range(self.resolution)] for _ in range(self.resolution)]

        for i in range(self.resolution):
            x = self.x_min + i * (self.x_max - self.x_min) / (self.resolution - 1)
            y = self.evaluate_function(function, x)
            j = int((y - self.y_min) * (self.resolution - 1) / (self.y_max - self.y_min))
            if 0 <= j < self.resolution:
                data[self.resolution - 1 - j][i] = '*'

        for row in data:
            print(''.join(row))


def main():
    calculator = GraphingCalculator()
    ## TEST CODE 测试用的
##    calculator.add_polynomial([1, -2, 1])  # Adds the polynomial x^2 - 2x + 1
##    calculator.add_polynomial([-1, 0, 1])  # Adds the polynomial -x^2 + 1
##    calculator.change_window_corner(-2, 2, -2, 2)  # Changes the graph viewing window
##    calculator.plot_polynomials()  # Plots the polynomials
    
    function = input("Enter a function: ")
    calculator.plot_function(function)  # Plots the user-defined function


if __name__ == "__main__":
    main()
