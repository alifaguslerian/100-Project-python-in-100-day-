# perbandingan dua angka

num1 = float(input("masukkan angka pertama: "))
num2 = float(input("masukkan angka kedua: "))

print("\n--- hasil perbandingan ---")
if num1 == num2:
    print(f"nilai kedua nya sama: {num1}")
elif num1 > num2:
    print (f"{num1} lebih besar dari {num2}")
else:
    print(f"{num2} lebih besar dari {num1}")

if num1 == 0 or num2 == 0:
    print("\n ada satu nilai nol.")
else:
    print("\n kedua nilai ga ada nol.")