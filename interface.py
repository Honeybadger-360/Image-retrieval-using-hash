import tkinter as tk
from tkinter import filedialog
from PIL import Image
import imagehash
import os
import glob
import numpy as np
import json

al = 132
ash = 195
ba = 154
bo = 214
ch = 543
co = 59
he = 67
je = 161
ke = 121
ma = 685
ne = 458
ori = 95
ox = 1502
pi = 108
ra = 282
tr = 217
wo = 70


def Compare(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    # x = len(hash1)
    # y = len(hash1[0])
    for i in range(len(hash1)):
        for j in range(len(hash1[0])):
            # 不相等则n计数+1，n最终为相似度
            if hash1[i][j] != hash2[i][j]:
                n = n + 1
    return n  # 1 - n / 64

def getHash2(im):
    # 缩小图片
    resize_width = 33
    resize_height = 32
    # 1. resize to (9,8)
    smaller_image =  im.resize((resize_width, resize_height))

    # 2. 灰度化 Grayscale
    grayscale_image = smaller_image.convert("L")

    # 3. 比较相邻像素
    pixels = list(grayscale_image.getdata())
    difference = []

    for row in range(resize_height):
        row_start_index = row * resize_width
        for col in range(resize_width - 1):
            left_pixel_index = row_start_index + col
            difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])

    # 转化为16进制(每个差值为一个bit,每8bit转为一个16进制)
    decimal_value = 0
    hash_string = ""
    for index, value in enumerate(difference):
        if value:  # value为0, 不用计算, 程序优化
            decimal_value += value * (2 ** (index % 8))
        if index % 8 == 7:  # 每8位的结束
            hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
            decimal_value = 0
    return hash_string


def getDifference(hash1, hash2):
    difference = (int(hash1, 16)) ^ (int(hash2, 16))
    return bin(difference).count("1")



def phash():
    count1 = 0
    count2 = 0
    Pos = 0
    Recall = 0
    hammin_arr = []
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    compare_hash1 = imagehash.phash(Image.open(file_path), hash_size=32)
    (filepath1, tempfilename) = os.path.split(file_path)
    (filename1, extension) = os.path.splitext(tempfilename)
    if filepath1.endswith('oxbuild_images'):
        paths = glob.glob(os.path.join(filepath1, '*.jpg'))
        print(len(paths))
        for path in paths:
            (filepath2, tempfilename) = os.path.split(path)
            (filename2, extension) = os.path.splitext(tempfilename)
            if filename1.startswith('al', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('al', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / al * 100,2))
            if filename1.startswith('ash', 0, 3):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ash', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ash * 100, 2))
            if filename1.startswith('ba', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ba', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ba * 100, 2))
            if filename1.startswith('bo', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('bo', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / bo * 100, 2))
            if filename1.startswith('ch', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ch', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ch * 100, 2))
            if filename1.startswith('co', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('co', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / co * 100, 2))
            if filename1.startswith('he', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('he', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / he * 100, 2))
            if filename1.startswith('je', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('je', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / je * 100, 2))
            if filename1.startswith('ke', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ke', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ke * 100, 2))
            if filename1.startswith('ma', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ma', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ma * 100, 2))
            if filename1.startswith('ne', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ne', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ne * 100, 2))
            if filename1.startswith('ori', 0, 3):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ori', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ori * 100, 2))
            if filename1.startswith('ox', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ox', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ox * 100, 2))
            if filename1.startswith('pi', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('pi', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / pi * 100, 2))
            if filename1.startswith('ra', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('ra', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ra * 100, 2))
            if filename1.startswith('tr', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('tr', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / tr * 100, 2))
            if filename1.startswith('wo', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
                if hanm <= 40:
                    if filename2.startswith('wo', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / wo * 100, 2))
    else:
        yuantu = (int(int(filename1) / 10))
        # imagelist = os.listdir(filepath1)
        paths = glob.glob(os.path.join(filepath1, '*.jpg'))
        print(len(paths))
        for path in paths:
            (filepath2, tempfilename) = os.path.split(path)
            (filename2, extension) = os.path.splitext(tempfilename)
            duibi = (int(int(filename2) / 10))
            if duibi == yuantu:
                Pos += 1
            compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
            hanm = Compare(str(compare_hash1.hash), str(compare_hash2.hash))
            # sim = 1 - (compare_hash1 - compare_hash2) / len(compare_hash2.hash) ** 2
            if  hanm <= 40:
                if duibi == yuantu:
                    Recall += 1
            # if sim >= 0.545:
                hammin_arr.append([hanm, path])
                count2 += 1
            if count1 % 100 == 0:
                print(count1)
            count1 += 1
        c = json.dumps(round(Recall / Pos * 100, 2))
    result = tk.Tk()
    result.title('汇总结果 by：索琰琰')
    result.geometry('300x300')
    a = json.dumps(len(paths))
    b = json.dumps(round(Recall/count2 * 100, 2))
    tk.Label(result, text='该文件夹中共有图片：' + a).place(x=10, y=50)
    tk.Label(result, text='此次检测精度为：' + b + '%').place(x=10, y=100)
    tk.Label(result, text='此次检测召回率为：' + c + '%').place(x=10, y=150)
    hammin_arr = np.array(hammin_arr)
    hammin_arr = hammin_arr[hammin_arr[:, 0].argsort()]
    for i in hammin_arr[:3]:
        img = Image.open(i[1])
        img.show()


def dhash():
    count1 = 0
    count2 = 0
    Pos = 0
    Recall = 0
    hammin_arr = []
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    compare_hash1 = getHash2(Image.open(file_path))
    (filepath1, tempfilename) = os.path.split(file_path)
    (filename1, extension) = os.path.splitext(tempfilename)
    if filepath1.endswith('oxbuild_images'):
        paths = glob.glob(os.path.join(filepath1, '*.jpg'))
        print(len(paths))
        for path in paths:
            (filepath2, tempfilename) = os.path.split(path)
            (filename2, extension) = os.path.splitext(tempfilename)
            if filename1.startswith('al', 0, 2):
                compare_hash2 = getHash2(Image.open(path))
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('al', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / al * 100, 2))
            if filename1.startswith('ash', 0, 3):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ash', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ash * 100, 2))
            if filename1.startswith('ba', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ba', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ba * 100, 2))
            if filename1.startswith('bo', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('bo', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / bo * 100, 2))
            if filename1.startswith('ch', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ch', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ch * 100, 2))
            if filename1.startswith('co', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('co', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / co * 100, 2))
            if filename1.startswith('he', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('he', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / he * 100, 2))
            if filename1.startswith('je', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('je', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / je * 100, 2))
            if filename1.startswith('ke', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ke', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ke * 100,2))
            if filename1.startswith('ma', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ma', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ma * 100, 2))
            if filename1.startswith('ne', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ne', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ne * 100,2))
            if filename1.startswith('ori', 0, 3):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ori', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ori * 100, 2))
            if filename1.startswith('ox', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ox', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ox * 100, 2))
            if filename1.startswith('pi', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('pi', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / pi * 100,2))
            if filename1.startswith('ra', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('ra', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / ra * 100, 2))
            if filename1.startswith('tr', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('tr', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / tr * 100, 2))
            if filename1.startswith('wo', 0, 2):
                compare_hash2 = imagehash.phash(Image.open(path), hash_size=32)
                hanm = getDifference(str(compare_hash1), str(compare_hash2))
                if hanm <= 490:
                    if filename2.startswith('wo', 0, 2):
                        Recall += 1
                    hammin_arr.append([hanm, path])
                    count2 += 1
                if count1 % 100 == 0:
                    print(count1)
                count1 += 1
                c = json.dumps(round(Recall / wo * 100, 2))
    else:
        yuantu = (int(int(filename1) / 10))
        print(yuantu)
        # imagelist = os.listdir(filepath1)
        paths = glob.glob(os.path.join(filepath1, '*.jpg'))
        print(len(paths))
        for path in paths:
            (filepath1, tempfilename) = os.path.split(path)
            (filename1, extension) = os.path.splitext(tempfilename)
            duibi = (int(int(filename1) / 10))
            if duibi == yuantu:
                Pos += 1
            compare_hash2 = getHash2(Image.open(path))
            hanm = getDifference(str(compare_hash1), str(compare_hash2))
            # sim = 1 - (compare_hash1 - compare_hash2) / len(compare_hash2.hash) ** 2
            if  hanm <= 490:
                if duibi == yuantu:
                    Recall += 1
            # if sim >= 0.545:
                hammin_arr.append([hanm, path])
                count2 += 1
            if count1 % 100 == 0:
                print(count1)
            count1 += 1
        c = json.dumps(round(Recall / Pos * 100, 2))
    result = tk.Tk()
    result.title('汇总结果 by：索琰琰')
    result.geometry('300x300')
    a = json.dumps(len(paths))
    b = json.dumps(round(Recall/count2 * 100, 2))
    tk.Label(result, text='该文件夹中共有图片：' + a).place(x=10, y=50)
    tk.Label(result, text='此次检测精度为：' + b + '%').place(x=10, y=100)
    tk.Label(result, text='此次检测召回率为：' + c + '%').place(x=10, y=150)
    hammin_arr = np.array(hammin_arr)
    hammin_arr = hammin_arr[hammin_arr[:, 0].argsort()]
    for i in hammin_arr[:3]:
        img = Image.open(i[1])
        img.show()



if __name__ == '__main__':
    Jmian = tk.Tk()
    Jmian.geometry('500x300')
    Jmian.title('图像检索 by:索琰琰')
    bt_login = tk.Button(Jmian, text='选择照片进行phash比对', command=phash)
    bt_login.place(x=200, y=100)
    bt_login = tk.Button(Jmian, text='选择照片进行dhash比对', command=dhash)
    bt_login.place(x=200, y=200)

    Jmian.mainloop()