import qrcode

# Текст, который вы хотите закодировать в QR-код
data = "https://www.reuters.com/technology/space/us-faa-moves-streamline-key-commercial-space-launch-hurdle-2024-12-13/"

# Создайте объект QRCode
qr = qrcode.QRCode(
    version=1,  # Версия QR-кода (зависит от количества данных)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок
    box_size=10,  # Размер одного квадрата QR-кода в пикселях
    border=4,  # Количество белых рамок вокруг QR-кода
)

# Добавьте данные в QR-код
qr.add_data(data)
qr.make(fit=True)

# Создайте изображение QR-кода и сохраните его в файл
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_QR-code.png")

