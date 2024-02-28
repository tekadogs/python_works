def main():
    x = int(input("What is x? "))
    print("Even") if parity(x) else print("Odd")

def parity(n):
    return n % 2 == 0 

main()

