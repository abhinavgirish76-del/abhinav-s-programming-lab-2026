
import calmodule

while True:
    print("\nSelect the option")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program terminated")
        break

    if choice in (1, 2, 3, 4):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if choice == 1:
            print(a, "+", b, "=", calmodule.addition(a, b))
        elif choice == 2:
            print(a, "-", b, "=", calmodule.substraction(a, b))
        elif choice == 3:
            print(a, "*", b, "=", calmodule.multiplication(a, b))
        elif choice == 4:
            print(a, "/", b, "=", calmodule.division(a, b))
    else:
        print("Invalid choice. Please select 1 to 5.")
