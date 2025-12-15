import tkinter as tk

# ASCII 小猫
cat = r"""
 /\_/\ 
( o.o )
 > ^ <
 _____
"""

# 创建窗口
root = tk.Tk()
root.title("Cute Cat 🐱")

# 创建文本标签显示猫
label = tk.Label(root, text=cat, font=("Consolas", 20), justify="center")
label.pack(padx=20, pady=20)

# 进入事件循环
root.mainloop()
