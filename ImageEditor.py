from PIL import Image
import random

# 1. Загрузка изображения

def load_image(path):
    try:
        img = Image.open(path)
        print(f'image size {img.size}')
        print("Изображение успешно загружено!")
        return img
    except FileNotFoundError:
        print("Файл не найден! Убедитесь, что картинка лежит в git-проекте.")
        exit()

# 2. Эффекты

def make_bw(img):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pix = img.getpixel((x, y))
            avg = (pix[0] + pix[1] + pix[2]) // 3
            img.putpixel((x, y), (avg, avg, avg))
    return img

def flip_vertical(img):
    w, h = img.size
    new_img = Image.new(img.mode, (w, h))
    for x in range(w):
        for y in range(h):
            pixel = img.getpixel((x, y))
            new_img.putpixel((x, h - y - 1), pixel)
    return new_img
    # return img.transpose(Image.FLIP_LEFT_RIGHT) есть уже готовый метод из библиотеки

def flip_horizontal(img):
    w, h = img.size
    new_img = Image.new(img.mode, (w, h))  #Почему-то если не создавать новое изображение, а менять уже имеющееся происходит забавный баг.
    for x in range(w):
        for y in range(h):
            pixel = img.getpixel((x, y))
            new_img.putpixel((w - x - 1, y), pixel)
    return new_img
    # return img.transpose(Image.FLIP_TOP_BOTTOM)

def paint_random_square(img, color):
    w, h = img.size
    pixels = img.load()
    min_size = min(w, h) // 5
    # Пришлось сделать ограничение по минимальному размеру, иначе прямоугольники получались слишком маленькими и незаметными.
    x0 = random.randint(0, w - min_size )
    y0 = random.randint(0, h - min_size)
    x1 = random.randint(x0, w - min_size)
    y1 = random.randint(y0, h - min_size)

    for x in range(x0, x1 + min_size ):
        for y in range(y0, y1 + min_size):
            pixels[x, y] = color

    return img

def add_noise(img):
    pixels = img.load()
    w, h = img.size
    num_pixels = (w * h) // 10  # 10% от суммы всех пикселей

    for _ in range(num_pixels):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)  # Выбираем случайные координаты для 10% пикселей
        pixels[x, y] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )  # случайный цвет каждого пикселя
    return img

def save_image(img):
    while True:
        filename = input("Введите имя файла для сохранения (например output.png): ")

        try:
            img.save(filename)
            print(f"Изображение сохранено как {filename}")
            exit()
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            print("Попробуйте снова.")

# 3. Основная программа

image_path = input("Введите путь к изображению: ")
img = load_image(image_path)

while True:
    print("Что вы хотите сделать?")
    print("1 — применить эффект")
    print("2 — сохранить изображение")
    choice = input("Ваш выбор: ")

    if choice == "1":
        print("Выберите эффект:")
        print("1 — сделать черно-белым")
        print("2 — отразить по вертикали")
        print("3 — отразить по горизонтали")
        print("4 — закрасить случайный квадрат")
        print("5 — добавить шум")

        effect = input("Номер эффекта: ")

        if effect == "1":
            img = make_bw(img)
            print("Изображение стало черно-белым.")
            img.show()

        elif effect == "2":
            img = flip_vertical(img)
            print("Отражено по вертикали.")
            img.show()

        elif effect == "3":
            img = flip_horizontal(img)
            print("Отражено по горизонтали.")
            img.show()

        elif effect == "4":
            print("Введите цвет в формате R G B (например: 255 0 0):")
            r, g, b = map(int, input().split())  #этот метод я подсмотрел
            img = paint_random_square(img, (r, g, b))
            print("Случайный квадрат закрашен.")
            img.show()

        elif effect == "5":
            img = add_noise(img)
            print("Добавлен шум.")
            img.show()

        else:
            print("Некорректный пункт.")

    elif choice == "2":
        save_image(img)

    else:
        print("Некорректный выбор. Повторите.")