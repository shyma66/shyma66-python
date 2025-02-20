from PyPDF2 import PdfMerger

# Укажите пути к вашим файлам
pdf_files = ["IVK FOS 2023 2024.pdf","Mittlerere Reife 2023 2024.pdf","Abschluss Zeugnis Ukraine.pdf", "B1 Kurs.pdf",
             "Bestätigung des Abschlusses.pdf","BIKV Berufsschule 2022 2023.pdf","Mittelschule 9 2022.pdf",
             "Certificate DevOps.pdf","Certificate HTML&CSS JS.pdf",
             "Certificate Python.pdf","Leben in Deutschland.pdf"]

# Создаем объект для объединения
merger = PdfMerger()

# Добавляем каждый файл
for pdf in pdf_files:
    merger.append(pdf)

# Сохраняем объединенный файл
merger.write("Datei Maksym Shylov.pdf")
merger.close()

print("PDF-файлы успешно объединены!")
