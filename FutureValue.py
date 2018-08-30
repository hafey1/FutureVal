# This program calculates value of investment carried to n amount of years.


def main():
    print("This program will let you calculate value of an investment after any amount of years")

    years = eval(input("Enter in the number of years the money will sit stashed away:"))
    principal = eval(input("Enter in the initial investment please:"))
    apr = eval(input("Enter in annual interest rate in terms of a decimal please:"))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value of the initial investment after", years, "years:", principal)

main()