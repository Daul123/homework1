import math

def calc_area():
    print("Выбери фигуру:")
    print("Круг 1")
    print("Прямоугольник 2")
    print("Треугольник 3")
    print("Квадрат 4")
    
    choice = input("фигура (1-4): ")
    
    if choice == "1":
        radius = float(input("радиус: "))
        area = math.pi * radius ** 2
        print("Площадь круга:", area)
        
    elif choice == "2":
        length = float(input("длина: "))
        width = float(input("ширина: "))
        area = length * width
        print("Площадь прямоугольника:", area)
        
    elif choice == "3":
        base = float(input("основание: "))
        height = float(input("высота: "))
        area = 0.5 * base * height
        print("Площадь треугольника:", area)
        
    elif choice == "4":
        side = float(input("сторонa: "))
        area = side ** 2
        print(f"Площадь квадрата:", area)
        
    else:
        print("Error!")

calc_area()
