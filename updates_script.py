'''
import pygetwindow as gw
import pyautogui
import time
from PIL import Image, ImageChops

def capture_screenshot(region, filename):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)

def images_are_equal(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()

def check_for_updates():
    time.sleep(5)

    windows = gw.getWindowsWithTitle("永劫无间")  # 替换为实际应用程序标题
    if len(windows) == 0:
        print("未找到目标应用程序窗口")
        return

    app_window = windows[0]

    if app_window.isMinimized:
        app_window.restore()
        time.sleep(1)

    app_window.activate()
    time.sleep(1)

    if not app_window.isActive:
        print("窗口未成功激活")
        return

    window_x, window_y = app_window.topleft
    print(f"窗口位置: ({window_x}, {window_y})")

    update_button_x, update_button_y = window_x + 857, window_y + 537  # 替换为实际捕获的坐标

    print(f"Moving to ({update_button_x}, {update_button_y})")

    capture_region = (update_button_x - 10, update_button_y - 10, 20, 20)  # 定义区域大小
    capture_screenshot(capture_region, 'before_click.png')

    pyautogui.moveTo(update_button_x, update_button_y, duration=1)

    print("Clicking the 'Check for Updates' button")
    pyautogui.click(update_button_x, update_button_y)

    time.sleep(5)  # 增加等待时间

    capture_screenshot(capture_region, 'after_click.png')

    if images_are_equal('before_click.png', 'after_click.png'):
        print("点击操作未检测到变化，可能失败")
    else:
        print("点击操作已成功完成")

check_for_updates()

'''

import pyautogui
import pygetwindow as gw
import time

# 定义目标窗口标题
window_title = "泪桥 - 伍佰"

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

    # 鼠标位置为: (438, 149)  鼠标位置为: (963, 849)
    # 指定点击位置 (相对于窗口左上角)
    click_x, click_y = 525, 700

    # 获取窗口位置
    window_left, window_top = target_window.left, target_window.top

    # 计算实际屏幕坐标
    actual_click_x = window_left + click_x
    actual_click_y = window_top + click_y

    # 移动并点击
    pyautogui.moveTo(actual_click_x, actual_click_y, duration=1)
    pyautogui.click(actual_click_x, actual_click_y)
else:
    print(f"未找到名为 '{window_title}' 的窗口")