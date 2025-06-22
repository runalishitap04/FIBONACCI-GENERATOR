def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

def main():
    print("FIBONACCI SERIES GENERATOR")
    try:
        n = int(input("Enter the number of terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_fibonacci(n)
            print("Fibonacci series:")
            print(series)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
