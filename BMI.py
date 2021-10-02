hight = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight: "))

#print("Body Mass Index: weight / hight(meter) *  hight(meter)")
bmi = weight / (hight * hight)
if bmi < 18.5:
    print("Thin")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")