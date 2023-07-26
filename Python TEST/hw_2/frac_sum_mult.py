frac1 = "1/2"
frac2 = "2/3"

a, b = frac1.split('/')
c, d = frac2.split('/')

a = int(a)
b = int(b)
c = int(c)
d = int(d)

frac_sum = (a*d + b*c) / (b*d)

frac_mult = (a*c) / (b*d)

print(frac_sum)
print(frac_mult)