import numpy as np
import matplotlib.pyplot as plt

def input_polynomial():
    print("Enter polynomial coefficients separated by spaces")
    print("Example for 2x^3 - 4x^2 + 3x - 5, enter: 2 -4 3 -5")
    coeffs_str = input("Coefficients (highest degree first): ")
    coeffs = list(map(float, coeffs_str.strip().split()))
    return np.poly1d(coeffs)

def main():
    n = int(input("How many polynomials do you want to plot? "))
    polynomials = []
    for i in range(n):
        print(f"\nPolynomial {i+1}:")
        p = input_polynomial()
        polynomials.append(p)

    x = np.linspace(-10, 10, 400)

    plt.figure(figsize=(8,6))
    for idx, poly in enumerate(polynomials, start=1):
        y = poly(x)
        plt.plot(x, y, label=f'Poly {idx}: {poly}')

    plt.title("Polynomial Graphs")
    plt.xlabel("x")
    plt.ylabel("p(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
