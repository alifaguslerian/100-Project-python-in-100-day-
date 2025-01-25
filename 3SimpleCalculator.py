# simple calculator

number1 = float(input("Masukkan angka pertama: "))
number2 = float(input("Masukkan angka kedua: "))

pertambahan = number1 + number2
pengurangan = number1 - number2
perkalian = number1 * number2
pembagian = number1 / number2 if number2 != 0 else "cannot divide by zero"

print("\n--- Hasil calculator ---")
print(f"pertambahan:{number1} + {number2} = {pertambahan}")
print(f"pengurangan:{number1} - {number2} = {pengurangan}")
print(f"perkalian: {number1} x {number2} = {perkalian}")
print(f"pembagian: {number1} / {number2} = {pembagian}")
