import os
f = input("是否首次使用？(y/n):")
if f == "y":
    os.system('D:\imaginationos\mm\scratch_2.py')
    print("密码以发送至您的邮箱，请查收！")
    os.system('D:\imaginationos\imaginationos.py')
elif f == "n":
    os.system('D:\imaginationos\imaginationos.py')
