import csv

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)

            # Debugging: Tampilkan header yang terbaca
            print(f"Header yang terbaca: {reader.fieldnames}")

            # Perbaiki header jika ada nama yang salah
            header_mapping = {
                'Dcience': 'Science'  # Perbaiki header yang salah
            }
            updated_headers = [header_mapping.get(h, h) for h in reader.fieldnames]

            # Debugging: Tampilkan header yang diperbaiki
            print(f"Header setelah diperbaiki: {updated_headers}")

            # Buat reader baru dengan header yang diperbaiki
            reader.fieldnames = updated_headers

            # Periksa apakah semua header yang diperlukan ada
            expected_headers = ['Name', 'Math', 'Science', 'English']
            missing_headers = [header for header in expected_headers if header not in reader.fieldnames]

            if missing_headers:
                print(f"Header berikut tidak ditemukan dalam file CSV: {', '.join(missing_headers)}")
                return

            student_reports = []
            for row in reader:
                try:
                    name = row['Name'].strip()
                    math = int(row['Math'].strip())
                    science = int(row['Science'].strip())
                    english = int(row['English'].strip())
                    average = round((math + science + english) / 3, 2)
                    status = "pas" if average >= 60 else "tidak pas"

                    student_report = {
                        'name': name,
                        'math': math,
                        'science': science,
                        'english': english,
                        'average': average,
                        'status': status
                    }
                    student_reports.append(student_report)
                except (ValueError, KeyError):
                    print(f"Baris data tidak lengkap atau tidak valid: {row}")
                    continue

        # Menulis data ke file output di luar loop
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['name', 'math', 'science', 'english', 'average', 'status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)

        print(f"Data mahasiswa telah disimpan ke {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Pemanggilan fungsi
input_file = 'student.csv'  # Nama file input
output_file = 'student_report.csv'  # Nama file output
process_student_data(input_file, output_file)
