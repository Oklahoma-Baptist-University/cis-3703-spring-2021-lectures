# Define a program for testing chaotic behavior
def make_chaos():
    print("This is the chaos program")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)