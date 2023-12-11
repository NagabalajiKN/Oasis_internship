print("\n")
print("           ██████╗░███╗░░░███╗██╗")
print("           ██╔══██╗████╗░████║██║")
print("           ██████╦╝██╔████╔██║██║")
print("           ██╔══██╗██║╚██╔╝██║██║")
print("           ██████╦╝██║░╚═╝░██║██║")
print("           ╚═════╝░╚═╝░░░░░╚═╝╚═╝")

print("+-----------------------------------------------+")
print("|                 Shape Shifter                 |")
print("+-----------------------------------------------+")
print("|               Calculate Your BMI              |")
print("+-----------------------------------------------+\n")

weight = float(input("Enter your weight in kilograms: ")) # input weight in kg
height = float(input("Enter your height in meters: "))    # input height in meters
if weight <= 0 or height <= 0:                            # check if weight or height is negative
    print("Invalid input. Please enter positive values only.")
    exit()                                                 # exit program if input is invalid
                         
def bmi_calculate(weight, height):                         # function to calculate BMI
    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    return bmi

def category_print(bmi):
    if bmi < 18.5:                                           # print category
        print("Category : underweight.")
        print("You should gain weight 💪")
    elif bmi < 25:
        print("Category : healthy weight.")
        print("Well done!! Keep it up😁")
    elif bmi < 30:
        print("Category : overweight.")
        print("You should lose some weight and exercise more.⛹️")
    else:
        print("Category : obese.")
        print("You should take immediate action to lose weight.You can do it🙂")

bmi = bmi_calculate(weight,height)                         # call function to calculate BMI
print(f" \nBMI : {bmi}\n")                           # print BMI     

category_print(bmi)