print("欢迎使用ChatRick，本模型基于Rick Astley于27 July 1987发表的论文:Ne jamais vous abandonner.")
print("清选择模型输出方式：")
print("======================")
print("1. 长文本输出")
print("2. 连续对话")
print("0. 退出")
print("======================")

def run(var):
    if var == 1:
        print("请输入选择：1")
        print("请输入想要生成的主题：如何学习机器学习")
        print("正在为您生成，请勿中途关闭，以免影响参数。")
        print("\r{:^3.2f}%[{}->{}]".format(100, "▓" * 100, ""), end="")
        print("\n")
        print("1. 学习Python，并用于算法编程。\n"
              "2. 深入了解机器学习的基础知识。\n"
              "3. 学习各种机器学习算法，并理解如何在真实世界的场景中应用它们。\n"
              "4. 进一步探索机器学习的应用。\n"
              "5. 找到一个特别感兴趣的领域，并深入探索。")
        print("请输入想要生成的主题：")
    else:
        print("请输入选择：2")
        print("正在初始化模型，请勿中途关闭，以免影响参数。")
        print("\r{:^3.2f}%[{}->{}]".format(100, "▓" * 100, ""), end="")
        print("\n输入：我的作业得了F，这是什么意思?\n")
        print("ChatRick:F在评分制度中通常表示fail,意思是不及格。\n"
              "在美国学制中，F是最低的分数，通常表示学生未能达到要求的标准。\n"
              "如果你的作业得了F，意味着你需要努力补最低的分数，通常表示学生未能达到要求的标准。\n"
              "如果你的作业得了F，意味着你需要努力补习，提高自己的学习能力，以便在下次考试中取得更好的成绩。\n")
        print("输入：我该如何提高我的成绩？\n")
        print("ChatRick:要想提高成绩，首先你应该指定一个计划，并努力实施。\n"
              "其次，你应该养成预习的习惯，在学习新知识时，提前预习。\n"
              "最后，你应该养成及时复习的习惯，以确保对知识的理解。\n")
        print("输入：")


run(2)