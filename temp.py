import sys

def c_to_f(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    c = float(sys.argv[1])
    print(f"Fahrenheit: {c_to_f(c):.2f}")