#Problem 1.1

def print_shifted_triangle(n, m, symbol):
    line = ""
    for i in range(n):
        line = ((m + n - i) * " ") + ((2 * i) +1 ) * symbol
        print(line)

print_shifted_triangle(3,4,'+')


#Problem 1.2

def print_shifted_triangle(rows,shift,symbol):
    for i in range(rows):
        line = ((shift+rows - i) * " ") + ((2 * i) + 1) * symbol
        print(line)


def print_pine_tree(n,symbol):
    for i in range(n):
        print_shifted_triangle(i+2,n-(i+2),symbol)


#Problem 1.3

def main():
    n = int(input("Please enter the n number of triangle sequences: "))
    symbol = input("Please enter the symbol: ")
    print_pine_tree(n,symbol)

main()