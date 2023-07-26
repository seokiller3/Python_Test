num = 255
print(hex(num)[2:].upper())
hex_str = ""
while num > 0:
  hex_digit = num % 16
  if hex_digit < 10:
    hex_str = str(hex_digit) + hex_str
  else:
    hex_str = chr(ord('A') + hex_digit - 10) + hex_str
  num = num // 16

print(hex_str)

