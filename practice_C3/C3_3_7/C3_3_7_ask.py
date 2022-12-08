import C3_3_7_square_figure


r = float(input("Введите радиус круга:"))
q1 = float(input("Введите длину первой стороны квадрата:"))
q2 = float(input("Введите длину сторой стороны квадрата:"))
r_q = C3_3_7_square_figure.square_round(r)
q_q = C3_3_7_square_figure.square_rectangle(q1, q2)

if r_q > q_q:
    print("Площадь круга больше!")
elif r_q < q_q:
    print("Площадь квадрата больше!")
else:
    print("Площади фигур равны!")

