shopping_list = []

def show_menu():
    print("\n--- Shopping list menu ---")
    print("1. Lihat daftar belanja")
    print("2. tambahkan item")
    print("3. hapus item")
    print("4. Clear list")
    print("5. Bayar belanjaan")

while True:
    show_menu()
    choice = input("Masukkan pilihan mu (1-5): ")

    if choice == "1":
        print("\n--- Shopping list ---")
        if not shopping_list:
            print("Daftar belanja kamu masih kosong.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")

    elif choice == "2":
        item = input("Masukkan item untuk ditambahkan: ")
        shopping_list.append(item)
        print(f"{item} Telah ditambahkan ke daftar belanja.")

    elif choice == "3":
        item = input("Masukkan barang yang akan dihapus: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} Telah dihapus dari daftar belanja.")
        else:
            print(f"{item} Tidak ada didaftar belanja.")

    elif choice == "4":
        shopping_list.clear()
        print("Daftar belanja telah dikosongkan.")

    elif choice == "5":
        print("Barang telah dibayar, Terima kasih Happy shopping!")
        break

    else:
        print("Pilihan invalid! PLease try again.")




