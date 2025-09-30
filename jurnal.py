import csv

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []

            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
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

        # Menulis data ke file output di luar loop
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['name', 'math', 'science', 'english', 'average', 'status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)

        print(f"Data mahasiswa telah disimpan ke {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
    except KeyError:
        print("Data tidak lengkap.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Pemanggilan fungsi
input_file = 'student.csv'  # Nama file input
output_file = 'student_report.csv'  # Nama file output
process_student_data(input_file, output_file)
