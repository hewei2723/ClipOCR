# clipboard_module.py

from PIL import ImageGrab
import win32clipboard
import io

def get_clipboard_image():
    try:
        # 打开剪贴板
        win32clipboard.OpenClipboard()

        # 尝试获取剪贴板数据
        data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)

        # 如果存在图像数据
        if data:
            # 使用 Pillow 打开图像
            image = ImageGrab.Image.frombytes("RGB", ImageGrab.size(), data)
            return image
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭剪贴板
        win32clipboard.CloseClipboard()

    return None
