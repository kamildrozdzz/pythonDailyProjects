x = input("Hours: ")
y = input("Rate: ")

fx = float(x)
fy = float(y)

if fx>40:
    reg = y*x
    otp = (fx - 40.0) * (fy * 0.5)
    z = reg + otp
else:
    z = fx * fy
print("Pay:",z)