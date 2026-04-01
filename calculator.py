def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("=== Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        expr = input("Enter expression (e.g. 5 + 3): ").strip()
        if expr.lower() == "quit":
            break

        parts = expr.split()
        if len(parts) != 3:
            print("Invalid format. Use: number operator number\n")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Invalid numbers.\n")
            continue

        ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
        if op not in ops:
            print(f"Unknown operator '{op}'\n")
            continue

        try:
            result = ops[op](a, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
