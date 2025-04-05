# import art
# print(art.logo)
### I made it more modular

def operation():
    op = input(r"""
     Enter the operator:
    +
    -
    *
    /
    """)
    return op
def add(n1, n2):
    return (n1 + n2)
def subt(n1,n2):
    return (n1 - n2)
def mult(n1, n2):
    return (n1 * n2)
def div(n1,n2):
    return (n1 / n2)

num1 = float(input("Enter the first number:"))
opera = operation()
num2 = float(input("Enter the second number:"))

def calci(n1,n2):
    if opera == '+':
     x =  add(n1,n2)
    elif opera == '-':
      x =  subt(n1,n2)
    elif opera == '*':
      x =  mult(n1,n2)
    elif opera == '/':
      x =  div(n1,n2)
    print(f"{n1} {opera} {n2} = {x}")
    return x

def iter():
    ter = False
    global current
    global opera ### opera is global changes here are everywhere.
    while not ter:
        state = input(
            f"Type 'y' to continue calculating with {current}, or type 'n' to start a new calculation:").lower()
        if state != 'y':
            return
        num = int(input("another number: "))
        opera = operation()
        current = calci(current, num)

current = calci(num1 , num2)
iter()
