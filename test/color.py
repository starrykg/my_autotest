from colorama import init
from colorama import Fore,Back,Style

init()

#前景色是红色，背景色是蓝色，文字是hello,python
print(Fore.RED,Back.BLUE,'hello,python')

print("how are you")
print("this is my home")

#还原
print(Style.RESET_ALL)

print("被打回原型")
print("我回来了")