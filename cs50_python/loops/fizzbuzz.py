def main():
    while True:
        n = int(input("What's n? "))
        if n >= 0:
            break
        else:
            n = n
    fizzbuzz(n)

def fizzbuzz(x):
    for _ in range(x):
        print(x, end=" ")
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print("")
        x -= 1
main()