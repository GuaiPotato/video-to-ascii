# 视频转彩色 ASCII 艺术

本项目基于 Python ，将视频文件转换为彩色的 ASCII 艺术视频。输出的视频将以当前日期和时间为文件名保存为 MP4 格式。

---

## 功能

- 将视频的每一帧转换为彩色的 ASCII 艺术。
- 输出为 MP4 格式的视频文件。
- 输出文件会自动保存在 `output/` 文件夹中，文件名格式为 `YYYY_MM_DD_HH_MM_SS.mp4`。

---

## 环境要求

- Python 3.7 及以上版本
- 依赖库：
  - OpenCV (`opencv-python`)
  - Numpy (`numpy`)
  - Pillow (`pillow`)

---

## 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/your-username/video-to-ascii.git
   cd video-to-ascii
   ```
2. 安装依赖：

   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 将你的视频文件放置在项目目录中，并修改 `convert_video_to_ascii.py` 文件中的 `video_path` 变量：

   ```
   video_path = "input_video.mp4"  # 替换为你的视频文件路径
   ```
2. 运行脚本：

   ```
   python convert_video_to_ascii.py
   ```
3. 转换后的 ASCII 视频将保存在 `output/` 文件夹中，文件名格式为 `YYYY_MM_DD_HH_MM_SS.mp4`，例如 `output/2024_11_21_14_30_00.mp4`。

---

## 输出示例

- 输入视频： 原始视频文件。
- 输出视频： 由每一帧的彩色 ASCII 字符组成的视频，代表了输入视频的内容。

---

## 自定义配置

你可以根据需要修改脚本中的以下参数：

- **视频分辨率**： 修改 `new_width` 来调整输出的 ASCII 视频分辨率：

  ```
  new_width = 100  # 增大此值可提高分辨率，减少此值可以加快处理速度
  ```
- **ASCII 字符集**： 修改 `ASCII_CHARS` 列表来定制你想使用的字符：

  ```
  ASCII_CHARS = ["@", "#", "8", "&", "%", "$", "*", "!", "+", ":", ",", "."]
  ```

---

## 已知问题

- 处理高分辨率的大视频可能会消耗较长时间和较多内存。
- 输出文件的大小可能比输入视频更大，具体取决于分辨率和帧率。

---

## 贡献

欢迎大家 fork 本仓库并提交 pull request，以改进和新增功能。

---

## 许可证

本项目采用 MIT 许可证，详情请见 `LICENSE` 文件。

---

## 致谢

- 灵感来源于 ASCII 艺术及其创意应用。
- 使用 OpenCV、Numpy 和 Pillow 构建。
