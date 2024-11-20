import cv2
import numpy as np
from PIL import Image
import os
from datetime import datetime

# ASCII 字符集（从黑到白）
ASCII_CHARS = ["@", "#", "8", "&", "%", "$", "*", "!", "+", ":", ",", "."]

# 将像素转换为 ASCII 字符
def pixel_to_ascii(image):
    image = image.convert("L")  # 转为灰度图像
    pixels = np.array(image)
    ascii_chars = []
    for pixel in pixels:
        row = [ASCII_CHARS[val // 25] for val in pixel]
        ascii_chars.append(row)
    return ascii_chars

# 将 ASCII 内容渲染为图像
def ascii_to_image(ascii_data, width, height, char_width=10, char_height=18):
    # 创建一个空白图像
    img = np.zeros((height * char_height, width * char_width, 3), dtype=np.uint8)

    # 绘制 ASCII 字符
    font_scale = 0.5
    font = cv2.FONT_HERSHEY_SIMPLEX
    y_offset = char_height
    for y, row in enumerate(ascii_data):
        x_offset = 0
        for x, char in enumerate(row):
            color = (255, 255, 255)  # 白色
            cv2.putText(img, char, (x_offset, y_offset), font, font_scale, color, 1, cv2.LINE_AA)
            x_offset += char_width
        y_offset += char_height

    return img

# 视频转换为 ASCII 并输出为视频文件
def video_to_ascii(video_path, output_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("无法打开视频文件，检查路径是否正确")
        return None

    # 获取视频的帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 获取视频的尺寸
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if width == 0 or height == 0:
        print("视频宽度或高度为零，无法处理")
        return None

    print(f"视频分辨率: {width}x{height}, 帧率: {fps}, 总帧数: {frame_count}")

    # 设置 ASCII 视频输出尺寸
    new_width = 100
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)

    # 输出文件夹
    if not os.path.exists('./output'):
        os.makedirs('./output')

    # 获取当前日期时间
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")
    output_file = f"./output/{timestamp}.mp4"

    # 创建视频写入对象
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (new_width * 10, new_height * 18))

    # 逐帧处理
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 缩放图像
        frame = cv2.resize(frame, (new_width, new_height))

        # 转换为 PIL 图像
        pil_image = Image.fromarray(frame)

        # 转换为 ASCII
        ascii_art = pixel_to_ascii(pil_image)

        # 将 ASCII 转换为图像
        ascii_image = ascii_to_image(ascii_art, new_width, new_height)

        # 写入视频文件
        out.write(ascii_image)

    cap.release()
    out.release()
    print(f"视频转换完成，保存为 {output_file}")

# 主函数
if __name__ == "__main__":
    # 输入视频文件路径
    video_path = "input/20241121_033515.mp4"  # 请修改为你的视频文件路径

    # 调用函数
    video_to_ascii(video_path, "./output/")
