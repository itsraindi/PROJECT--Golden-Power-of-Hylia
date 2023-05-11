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

    def find_derivative(self, poly):
        derivative = []
        n = len(poly)
        for i in range(n - 1):
            derivative.append(poly[i] * (n - i - 1))
        return derivative

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

    def find_intersection(self, poly1, poly2, x0=0, epsilon=1e-6, max_iterations=1000):
        # This function assumes that poly1 and poly2 have the same length
        diff_poly = [poly1[i] - poly2[i] for i
    def find_intersection(self, poly1, poly2, x0=0, epsilon=1e-6, max_iterations=1000):
        # Ensure that poly1 and poly2 have the same length
        len_diff = len(poly1) - len(poly2)
        if len_diff > 0:
            poly2 = [0]*len_diff + poly2
        elif len_diff < 0:
            poly1 = [0]*(-len_diff) + poly1

        diff_poly = [poly1[i] - poly2[i] for i in range(len(poly1))]
        diff_poly_derivative = self.find_derivative(diff_poly)
        
        x = x0
        for _ in range(max_iterations):
            f = self.evaluate_polynomial(diff_poly, x)
            f_prime = self.evaluate_polynomial(diff_poly_derivative, x)
            if f_prime == 0:
                return None
            x_new = x - f / f_prime
            if abs(x_new - x) < epsilon:
                return x_new
            x = x_new
        return None

    def determine_intersections(self):
        if len(self.polynomials) < 2:
            print("At least two polynomials are needed to find intersections.")
            return

        for i in range(len(self.polynomials)):
            for j in range(i + 1, len(self.polynomials)):
                print(f"Finding intersections between polynomial {i+1} and polynomial {j+1}")
                intersection = self.find_intersection(self.polynomials[i], self.polynomials[j])
                if intersection is not None:
                    print(f"The polynomials intersect approximately at x = {intersection:.6f}")
                else:
                    print("Unable to find the intersection with the given initial guess.")
