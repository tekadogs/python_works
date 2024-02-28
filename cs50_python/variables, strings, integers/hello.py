def main():
    name = input("What's your name? ").title()
    print(hello(name))

def hello(to = "loyal subject"):
    return "Hello, " + to 

main()