import json
import os

TASK_FILE = 'tasks.json'

# Buat file JSON jika belum ada
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

# Load tasks from JSON
def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Save tasks to JSON
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# Add a new task
def add_task():
    task_name = input("Masukkan Nama Task: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "incomplete"})
    save_tasks(tasks)
    print(f'Task "{task_name}" berhasil ditambahkan.')

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- Daftar Task ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} - Status: {task['status']}")
    else:
        print("\n--- Daftar Task Kosong ---")

# Update task status
def update_status():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Masukkan nomor task yang ingin diubah statusnya: ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Masukkan status baru (complete/incomplete): ").strip()
            tasks[task_index]['status'] = new_status
            save_tasks(tasks)
            print("Status task berhasil diubah.")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Nomor task harus berupa angka.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Masukkan nomor task yang ingin dihapus: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' berhasil dihapus.")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Nomor task harus berupa angka.")

# Display menu
def display_menu():
    print("\n--- Menu ---")
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Ubah Status Task")
    print("4. Hapus Task")
    print("5. Keluar")

# Main program
def main():
    while True:
        display_menu()
        choice = input("Masukkan pilihanmu (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_status()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    main()
