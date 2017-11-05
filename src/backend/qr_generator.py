import tkinter as tk
import qrcode
from PIL import ImageTk


def get_text():
    """
    Фуннкция чтения информации из виджета Text
    :return: Введенная пользователем информация в формате "строка"
    """
    return text.get(1.0, tk.END).rstrip('\r\n')


def generate_qr():
    """
    Функция генерации QR-кода.
        ERROR_CORRECT_L: About 7% or less errors can be corrected.
        ERROR_CORRECT_M: (default) About 15% or less errors can be corrected.
        ERROR_CORRECT_Q: About 25% or less errors can be corrected.
        ERROR_CORRECT_H: About 30% or less errors can be corrected.
    """
    # Настройка QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # Информация, подлежащая кодированию
    data = get_text()
    # Создание QR-метки
    qr.add_data(data)
    qr.make(fit=True)
    # Сохраняем QR-метку в изображение
    img = qr.make_image()
    img.save(IMAGE_NAME)


def show_qr():
    """
    Функция для вывода изображения QR-метки на экран (в новом окне)
    """
    generate_qr()
    new_window = tk.Toplevel()
    new_window.title("QR-code")
    im = ImageTk.PhotoImage(file=IMAGE_NAME)
    panel = tk.Label(new_window, image=im)
    panel.pack()
    new_window.mainloop()


if __name__ == "__main__":
    IMAGE_NAME = "qr_code.jpg"
    text = "Example"
    root = tk.Tk()
    root.title('QR-code generator')

    text = tk.Text(root, width=20, height=1, bg='white')
    button = tk.Button(root, text="Generate QR-code", command=show_qr)
    text = tk.Text(root, width=20, height=1, bg='white')

    button.pack()
    text.pack()

    root.mainloop()
