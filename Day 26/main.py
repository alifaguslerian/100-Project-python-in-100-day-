class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = password
        self.set_password(password)

    # Getter untuk email
    def get_email(self):
        return self._email
    
    # Setter untuk email
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email berhasil diperbarui!")
        else:
            print("Format email tidak valid. Harap masukkan email yang valid.")

    # Getter untuk password
    def get_password(self):
        return self._password

    # Setter untuk password
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Password harus memiliki panjang minimal 6 karakter.")
        else:
            self._password = new_password
            print("Password berhasil diperbarui!")

    # Menampilkan profil
    def display_profile(self):
        print("\n--- Profil Pengguna ---")
        print(f"Username: {self.username}")
        print(f"Email: {self._email}")
        print(f"Password: {self._password}")

# Program utama
user_profiles = []  # List untuk menyimpan banyak profil pengguna

def create_user():
    username = input("Masukkan username: ")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")
    user = UserProfile(username, email, password)
    user_profiles.append(user)
    print("Profil pengguna berhasil dibuat!")

def view_profiles():
    if not user_profiles:
        print("Tidak ada profil pengguna.")
    else:
        for user in user_profiles:
            user.display_profile()

def update_email():
    username = input("Masukkan username: ")
    for user in user_profiles:
        if user.username == username:
            new_email = input("Masukkan email baru: ")
            user.set_email(new_email)
            return
    print("Pengguna tidak ditemukan.")

# Menu utama
while True:
    print("\n--- Aplikasi Profil Pengguna Aman ---")
    print("1. Buat Profil Pengguna")
    print("2. Lihat Profil Pengguna")
    print("3. Perbarui Email")
    print("4. Keluar")

    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        create_user()
    elif choice == "2":
        view_profiles()
    elif choice == "3":
        update_email()
    elif choice == "4":
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Harap pilih opsi yang benar (1-4).")
