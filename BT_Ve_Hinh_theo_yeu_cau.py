#Đầu vào (người dùng nhập vào từ bàn phím):
#* Chọn khối hình (hình tròn, hình vuông, hình chữ nhật, ngũ giác, tam giác đều, oval, trái tim)
#* Kích thước muốn vẽ (tùy mỗi hình sẽ có thông tin khác nhau. Ví dụ: hình tròn là nhập bán kính,
# hình vuông là nhập cạnh, hình chữ nhật là nhập vào chiều dài/rộng,
# oval và trái tim thì có thể không cần nhập kích thước).
#* Số lượng hình muốn vẽ (quay đều các hình được vẽ theo tâm đường tròn).
#* Màu sắc (Người dùng có thể chọn màu ngẫu nhiên hoặc màu cụ thể: đỏ, vàng, xanh dương, xanh lá cây, tím,...)
#Kết quả: Các hình được vẽ trên màn hình theo đúng kích thước, số lượng, khối hình, màu sắc đã chọn.
import random
import turtle
import Draw_module

#Define Input function
def input_cubes():
    cubes_list = ['circle', 'square', 'triangle', 'rectangle', 'oval', 'pentagon', 'heart']
    while True:
            cubes = input("Please enter your cubes:")
            if cubes in cubes_list:
                return cubes
                break
            else:
                print("Please choose: circle, square, triangle, rectangle, oval, pentagon or heart:")

#Define input color of cubes
def input_color():
    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'white', 'black', 'brown', 'magenta', 'tan', 'olive', 'maroon', 'navy', 'aquamarine', 'turquoise', 'silver', 'lime', 'teal', 'indigo', 'violet', 'pink', 'gray', 'off white', 'navy blue', 'baby pink']
    while True:
        color = input("Please enter color of your cubes:")
        if color in color_list:
            return color
            break
        elif color == '':
            color = random.choice(color_list)
            return color
            break

#Define input the number of cubes:
def input_number():
    while True:
        try:
            number = int(input("Please enter the number of cubes you want:"))
            if number > 0:
                return number
                break
            else:
                print("Invalid!Please enter the integer!")
        except ValueError:
            print("Invalid!Please enter the integer!")

#Define input width, length, radius:
def input_data_cubes():
    global cubes_name
    while True:
        try:
            if cubes_name == 'circle' or cubes_name == 'oval':
                radius = float(input("Please enter a number > 0! Radius:"))
                if radius > 0:
                    return radius
                    break
                else:
                    print("Try again!")
            elif cubes_name == 'square' or cubes_name == 'triangle' or cubes_name == 'pentagon':
                length = float(input("Please enter a number > 0! Length:"))
                if length > 0:
                    return length
                    break
                else:
                    print("Try again!")
            elif cubes_name == 'rectangle':
                width = float(input("Please enter a number > 0! Width:"))
                long = float(input("Please enter a number > 0! Length:"))
                if width > 0 and long > 0:
                    return width, long
                    break
                else:
                    print("Try again!")
            else:
                break
        except ValueError:
            print("Invalid!Please enter the number > 0!")

#Define a function to draw cubes:
def draw_cubes():
    global cubes_name
    if cubes_name == 'circle':
        your_cubes = Draw_module.draw_circle(radius, color)
    elif cubes_name == 'oval':
        your_cubes = Draw_module.draw_oval(radius, color)
    elif cubes_name == 'square':
        your_cubes = Draw_module.draw_square(length, color)
    elif cubes_name == 'triangle':
        your_cubes = Draw_module.draw_triangle(length, color)
    elif cubes_name == 'pentagon':
        your_cubes = Draw_module.draw_pentagon(length, color)
    elif cubes_name == 'rectangle':
        your_cubes = Draw_module.draw_rectangle(width, long, color)
    elif cubes_name == "heart":
        your_cubes = Draw_module.draw_heart(color)
    else:
        print()
    return your_cubes

#Draw the cubes:
cubes_name = input_cubes()
cubes_number = input_number()
color = input_color()
radius = input_data_cubes()
length = input_data_cubes()
width, long = input_data_cubes()

turtle.title("Your " + cubes_name)
for i in range(cubes_number):
    draw_cubes()
    turtle.left(360 / cubes_number)

turtle.done()
