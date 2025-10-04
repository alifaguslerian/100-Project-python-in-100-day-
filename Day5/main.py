import time

start = int(input("masukkan nilai untuk mulai hitung mundur dari: "))

print("\n--- hitung mundur mulai ---")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1

print ("hitung mundur selesai!")