import sys
import time
from math import sqrt


def run():
    x = 0
    while True:
        time.sleep(0.05)
        x += 0.01
        y = 100 * (x - sqrt(x)) / (x - 1)
        finsh = "▓" * int(y)
        need_do = "-" * (100 - int(y))
        print("\r", end="")
        print("\r{:^3.2f}%[{}->{}]".format(y, finsh, need_do), end="")


print("欢迎使用ChatRick，本模型基于Rick Astley于27 July 1987发表的论文:Ne jamais vous abandonner.")
print("清选择模型输出方式：")
print("======================")
print("1. 长文本输出")
print("2. 连续对话")
print("0. 退出")
print("======================")
while True:
    choice = input("请输入选择：")
    if choice.isdigit():
        if int(choice) < 0 or int(choice) > 2:
            print("输入错误，请重新输入。")
            continue
        else:
            if int(choice) == 1:
                input("请输入想要生成的主题：")
                print("正在为您生成，请勿中途关闭，以免影响参数。")
                run()
            elif int(choice) == 2:
                print("正在初始化模型，请勿中途关闭，以免影响参数。")
                run()
            elif int(choice) == 0:
                print("正在保存模型，请勿中途关闭。")
                run()
    else:
        print("输入错误，请重新输入。")
        continue
