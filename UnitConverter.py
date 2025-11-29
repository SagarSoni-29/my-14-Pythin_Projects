while True:
    print("This is a Unit Converter....")
    try:
        n=int(input("1.M into Kilometer\n2.Celsius to Fahrenheit\nEnter No.:."))
        match(n):
            case(1):
                a=int(input("Enter in Meter: "))
                print(f'Meter into Kilometer: {a/1000}')
                break
            case(2):
                a=float(input("Enter in Celsius: "))
                f=(a*9/5)+32
                print(f'Celsius into Fahrenheit: {f}')
                break

    except:
        print("Invaild Input")
 