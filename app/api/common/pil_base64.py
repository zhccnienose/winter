from base64 import b64encode


# 图像转化成base64字符串
def pil_base64(head_image_path):
    with open(head_image_path, "rb") as image:
        image_data = image.read()
    return b64encode(image_data).decode("utf-8")
