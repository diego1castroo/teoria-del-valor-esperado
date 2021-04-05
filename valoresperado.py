print("datos para la primera opcion\n")
x1 = float(input("ingresa cantidad a ganar:\t"))
p1 = float(input("ingresa probabilidad de ganar:\t"))
x2 = float(input("ingresa cantidad a perder:\t"))
p2 = float(input("ingresa probabilidad de perder:\t"))
print("\n\ndatos para la segunda opcion\n")
x11 = float(input("ingresa cantidad a ganar:\t"))
p11 = float(input("ingresa probabilidad de ganar:\t"))
x21 = float(input("ingresa cantidad a perder:\t"))
p21 = float(input("ingresa probabilidad de perder:\t"))

print("\nla opcion 1 queda de la siguiente manera:\nGanar ", x1," con ", p1, " de probabilidad o perder ", x2, " con ", p2, " de probabilidad ")
print("\nla opcion 2 queda de la siguiente manera:\nGanar ", x11," con ", p11, " de probabilidad o perder ", x21, " con ", p21, " de probabilidad ")

s1 = ((x1*(p1/100)) - (x2*(p2/100)))
s2 = ((x11*(p11/100)) - (x21*(p21/100))) 

if(s1>s2):
	print("\n<<<<<<<<la mejor opcion es la numero 1>>>>>>>>")
else:
	print("\n<<<<<<<<la mejor opcion es la numero 2>>>>>>>>")
