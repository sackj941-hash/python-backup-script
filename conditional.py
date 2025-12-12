day_of_week = input("Enter the day of the week: ").lower()
print(day_of_week)

if day_of_week == "staurday" or day_of_week == "sunday":
    print("I will learn live devops")
else:
    print("I will practice devops")

    num1 = int(input ("enter first number: "))
    num2 = int(input ("enter second number:"))

    choice = input("enter the operation: (+, -, *, /): ")

    if choice == "+":
        sum_of_num = num1 + num2
        print(" addition:", sum_of_num)
    elif choice == "-":
        diff_of_num = num1 - num2
        print("subtraction:", diff_of_num)
    elif choice == "*":
        prod_of_num = num1 * num2
        print(" multiplication:", prod_of_num)
    elif choice == "/":
        div_of_num = num1 / num2
        print(" division:", div_of_num)
    else:
        print("invalid operation")