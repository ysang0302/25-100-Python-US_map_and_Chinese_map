import pandas
import turtle as t

screen = t.Screen()
screen.setup(1200, 1200)
screen.title("中国省份猜猜猜")
image = "china_blank_map.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("../chinamap/省份坐标.csv")
all_provinces = data.省份.to_list()
guessed_provinces = []

while len(guessed_provinces) < 50:
    answer_province = screen.textinput(title=f"{len(guessed_provinces)}/34 provinces Correct",
                                       prompt="下一个省份的名字是什么？").title()
    if answer_province == "Exit":
        missing_provinces = []
        for state in all_provinces:
            if state not in guessed_provinces:
                missing_provinces.append(state)
        new_data = pandas.DataFrame(missing_provinces)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        province_data = data[data.省份 == answer_province]
        tim.goto(int(province_data.x), int(province_data.y))
        tim.write(answer_province, font=("New Roman", 14, "bold"))

screen.exitonclick()
