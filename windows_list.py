import pygetwindow as gw

# 获取所有打开的窗口
windows = gw.getAllTitles()

# 打印每个窗口的标题
for window in windows:
    if window:  # 排除空标题窗口
        print(window)