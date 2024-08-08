import pyautogui
import pygetwindow as gw
import time
import cv2

# 确保已安装OpenCV：pip install opencv-python

# 定义目标窗口标题
window_title = "解限机"
small_window_title_keyword = "检查更新"  # 假设小窗口标题包含这个关键词

# 获取目标窗口对象
target_window = None
for window in gw.getAllTitles():
    if window_title in window:
        target_window = gw.getWindowsWithTitle(window)[0]
        break

if target_window is not None:
    # 将窗口最小化并恢复，以确保其显示在前面
    target_window.minimize()
    time.sleep(0.5)  # 等待最小化动作生效
    target_window.restore()
    time.sleep(0.5)  # 等待恢复动作生效

    # 将窗口置于前台
    target_window.activate()
    time.sleep(1)  # 等待窗口激活

    # 窗口左上角鼠标位置为: (324, 161)  继续下载按钮鼠标位置为: (1406, 870)   设置按钮鼠标位置为: (1539, 871)
    # 指定点击位置 (相对于窗口左上角)

    click_x, click_y = 1215, 700

    # 获取窗口位置（左上角的坐标）
    window_left, window_top = target_window.left, target_window.top

    # 计算实际屏幕坐标
    actual_click_x = window_left + click_x
    actual_click_y = window_top + click_y

    # 截图指定区域（前面两个参数是截图开始的xy坐标，后面两个参数是截图的大小参数，可以根据实际情况调整）
    screenshot_region = (actual_click_x - 10, actual_click_y - 10, 50, 50)
    screenshot = pyautogui.screenshot(region=screenshot_region)

    # 保存临时截图以便调试（可选）
    screenshot.save("screenshot.png")

    # 尝试在整个屏幕上查找目标图像（confidence参数设置匹配精度）
    try:
        button_location = pyautogui.locateOnScreen("settings_button.png", confidence=0.95)
    except pyautogui.ImageNotFoundException:
        print("未找到 'settings_button.png' 图像文件")
        button_location = None

    if button_location:
        # 移动到目标位置
        pyautogui.moveTo(actual_click_x, actual_click_y, duration=1)
        # 如果找到按钮，则执行点击操作
        pyautogui.click(actual_click_x, actual_click_y)

        # 第二次操作：等待小窗口出现并进行下一步操作
        time.sleep(2)  # 等待小窗口出现

        small_window = None
        for window in gw.getAllTitles():
            if small_window_title_keyword in window:
                small_window = gw.getWindowsWithTitle(window)[0]
                break

        if small_window is not None:
            # 操作小窗口，比如点击小窗口中的某个按钮
            small_window_left, small_window_top = small_window.left, small_window.top
            small_click_x, small_click_y = 10, 10  # 小窗口中按钮的相对位置
            actual_small_click_x = small_window_left + small_click_x
            actual_small_click_y = small_window_top + small_click_y

            # 点击小窗口中的按钮
            pyautogui.moveTo(actual_small_click_x, actual_small_click_y, duration=1)
            pyautogui.click(actual_small_click_x, actual_small_click_y)
        else:
            print("未找到小窗口")

    else:
        print("未找到 '继续下载' 按钮")

else:
    print(f"未找到名为 '{window_title}' 的窗口")