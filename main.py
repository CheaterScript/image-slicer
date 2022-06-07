import cv2
import os
import numpy as np
import os

# 等分
rows = 16
cols = 16

# 要处理的文件路径
img_path = './input.raw'
# 输出文件名
output_name = 'image'
# 输出文件存放路径
output_path = './output/'

# 支持的格式, 不在其中的会跳过处理
FILE_TYPES = ('.jpg', '.jpge', '.png', '.raw')


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    pass


def loadFile():
    _, extension_name = os.path.splitext(img_path)
    extension_name = extension_name.lower()
    if extension_name not in FILE_TYPES:
        raise Exception("文件验证失败：" + i)
    if extension_name == '.tga':
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise Exception("文件验证失败：" + i)
    else:
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise Exception("文件验证失败：" + i)


def handleRAW():
    # img = cv2.imread(img_path)
    img = np.fromfile(img_path, dtype=np.uint8)
    img = img.reshape((65536, 65536, 3))
    shape = img.shape
    # _, ExtensionName = os.path.splitext(img_path)
    singleWidth = int(shape[0] / cols)
    singleHeight = int(shape[1] / rows)

    mkdir(output_path)

    for i in range(rows):
        for j in range(cols):
            print("正在处理%d/%d张……" % (i*rows+j / rows*cols))
            x = j * singleWidth
            y = i * singleHeight
            print("%d_%d" % (x, y))
            new_img = cv2.cvtColor(
                img[y:y+singleHeight, x: x+singleWidth], cv2.COLOR_BGR2RGB)
            cv2.imwrite("%s%s_%03d%s" %
                        (output_path, output_name, i*singleHeight+j, ".jpg"), new_img)

    print('处理完成')


def handlePNG():
    pass


def handleJPG():
    pass


def saveFile():


if __name__ == '__main__':
    main()
