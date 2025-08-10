# Конвертируем .jpg в .txt с помощью библиотеки easyocr
# import easyocr
# from PIL import Image
# import os

# Путь к сохранённому .jpg
# Путь к файлу передавать без всяких кавычек, например:
# C:\Users\pl\PycharmProjects\photo_2025-08-10_code.jpg
#
# input_jpg_1 = "C://Users//pl//OneDrive//Рабочий стол//photo_2025-08-10_code.jpg"
# input_jpg_1 = "C:\Users\pl\OneDrive\Рабочий стол\photo_2025-08-10_code.jpg"
# output_pdf_1 = "C:\Users\pl\Documents\Подготовка\CV\Al_P_CV_Updated.pdf"

# reader = easyocr.Reader(['ru', 'en'])  # указать языки для распознавания
# Конвертация
# result = reader.readtext(input_jpg_1, detail=0)
# result = reader.readtext('your_photo.jpg', detail=0)
# print(' '.join(result))

# result
# result
# import easyocr - Эта строка импортирует библиотеку EasyOCR, которая используется для оптического распознавания текста (OCR). Распознаёт текст на изображении.
# import os - Работает с путями и файловой системой.

import os

import easyocr


def image_to_text_easyocr(my_image_path: str, output_file=None, my_scope_languages=['en', 'ru']):
    """
    Конвертирует изображение с текстом в текстовый файл с помощью EasyOCR.

    Путь к файлу передавать без всяких кавычек, например: C:\Users\pimal\PycharmProjects\photo_2025-08-10_code.jpg

    :param my_image_path: путь к изображению (JPG/PNG)
    :param output_file: путь к выходному файлу (если None, создаётся автоматически)
    :param my_scope_languages: список языков (['en'] - английский, ['ru'] - русский, ['en','ru'] - оба)
    :return: путь к сохранённому файлу
    """
    try:
        # Создаём ридер (указываем языки)
        # reader = easyocr.Reader(['ru', 'en'])  # указать языки для распознавания, 'ru', 'en' - оба языка
        reader = easyocr.Reader(my_scope_languages)

        # Читаем текст с картинки
        result = reader.readtext(my_image_path, detail=0)  # detail=0 → только текст

        # Объединяем строки
        text = "\n".join(result)

        # Если выходной файл не указан, создаём автоматически
        if output_file is None:
            # Разбивает путь к файлу на имя и расширение:
            base_name = os.path.splitext(my_image_path)[0]
            # Создаёт автоматическое имя для выходного файла:
            output_file = f"{base_name}.txt"

        # Сохраняем в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)

        print(
            f"✅ Текст сохранён в: {output_file}")  # ✅ Текст сохранён в: C:\Users\pimal\PycharmProjects\photo_2025-08-10_code.txt
        return output_file

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None


if __name__ == "__main__":
    image_path = input("Введите путь к изображению (JPG/PNG): ").strip()

    # Проверяет, существует ли файл:
    if not os.path.exists(image_path):
        print("❌ Файл не найден!")
    else:
        lang = input("Язык текста (en/ru/en+ru): ").strip().lower()
        if lang == 'ru':
            languages = ['ru']
        elif lang == 'en':
            languages = ['en']
        else:
            languages = ['en', 'ru']  # по умолчанию оба

        image_to_text_easyocr(image_path, my_scope_languages=languages)
