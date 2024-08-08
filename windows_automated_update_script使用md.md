## 项目说明
用于windows上给解限机的启动器自动更新的脚本
## 文件说明

1. Mouse_position_detection.py：鼠标定位检测文件，用来检测定位你想要的按钮的位置
2. windows_list.py：检测你的后台运行的进程的名字
3. updates_script.py：模拟鼠标移动和点击进行检测更新
4. screenshot.png：检测截图，用于校验和debug
4. continue_download_button.png：目标继续下载照片
6. update_button.png:目标更新按钮图片
7. continue_update_button.png:目标继续更新按钮图片

## 操作流程

1. 先用Mouse_position_detection.py确定窗口的左上角的xy坐标，以及你想要的按钮的中心的xy坐标，算出两者xy坐标的相对差值，填入updates_script.py中的click_x, click_y参数
2. windows_list.py，检测你的后台运行的进程的名字，找到你想要进行命令的进程，填入updates_script.py中的window_title参数中
3. 

## 注意事项
1. 游戏启动器一般会有脚本检测，建议使用管理员权限运行该脚本
2. 脚本的鼠标移动距离参数是按照我自己的电脑外接屏幕设置的，一般台式机都可以用，但是对笔记本和尺寸比较少见的显示器，建议按照以上的操作流程用Mouse_position_detection.py进行重新定位