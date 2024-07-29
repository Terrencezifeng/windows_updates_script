
import pyautogui
import time

print("5秒内将鼠标移至所需位置...")
time.sleep(5)
currentMouseX, currentMouseY = pyautogui.position()
print(f"鼠标位置为: ({currentMouseX}, {currentMouseY})")



'''
import pygetwindow as gw
import pyautogui
import time

def get_update_button_coords(window_title, button_image_path):
    # 获取指定窗口
    print(f"Button image path: {button_image_path}")
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print("未找到目标应用程序窗口")
        return None

    app_window = windows[0]
    app_window.activate()
    time.sleep(1)  # 等待窗口激活

    # 截取当前屏幕
    screenshot = pyautogui.screenshot()

    # 在截图中查找按钮图像
    button_location = pyautogui.locate(button_image_path, screenshot)

    if button_location is not None:
        # 获取按钮中心点坐标
        button_center_x, button_center_y = pyautogui.center(button_location)
        print(f"按钮位置: ({button_center_x}, {button_center_y})")
        return button_center_x, button_center_y
    else:
        print("未找到按钮")
        return None

def check_for_updates():
    window_title = "永劫无间"  # 替换为实际应用程序标题
    button_image_path = "update_button.png" # 按钮图像路径，需要提前截取并保存按钮图片

    # 获取按钮坐标
    coords = get_update_button_coords(window_title, button_image_path)
    if coords:
        button_x, button_y = coords
        print(f"Moving to ({button_x}, {button_y})")

        # 将鼠标移到“检查更新”按钮上
        pyautogui.moveTo(button_x, button_y, duration=1)

        print("Clicking the 'Check for Updates' button")
        # 点击“检查更新”按钮
        pyautogui.click()

        print("Clicked the button, checking for updates...")

# 调用函数并观察输出
check_for_updates()

'''