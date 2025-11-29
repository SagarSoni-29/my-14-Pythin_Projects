#      calculator 

print("Choice Your Operators\n1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\nExit")
n=int(input("Enter Your Operator:"))
if n==1:
    num1=int(input("Enter your first No.1:"))
    num2=int(input("Enter your first No.2:"))
    print(f'Your given No. is {num1} and {num2} and Sum is:{num1+num2}')
elif n==2:
    num1=int(input("Enter your first No.1:"))
    num2=int(input("Enter your first No.2\nIs grater then No.1:"))
    print(f'Your given No. is {num1} and {num2} and Sub is:{num1-num2}')
elif n==3:
    num1=int(input("Enter your first No.1:"))
    num2=int(input("Enter your first No.2:"))
    print(f'Your given No. is {num1} and {num2} and Mult. is:{num1*num2}')
elif n==4:
    num1=int(input("Enter your first No.1:"))
    num2=int(input("Enter your first No.2\nIs grater then No.1:"))
    print(f'Your given No. is {num1} and {num2} and div. is:{num1/num2}')
else:
    exit
