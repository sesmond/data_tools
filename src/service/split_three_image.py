#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Title   : 拆分样本
@File    :   split_three_image.py    
@Author  : vincent
@Time    : 2021/4/17 下午5:55
@Version : 1.0 
"""
import os

from PIL import Image

from src.utils import file_utils


def split_process(input_path, output_path):
    """
    拆分流程
    :param input_path:
    :param output_path:
    :return:
    """
    img_list = file_utils.get_files(input_path)
    file_utils.check_path(output_path)
    for fp in img_list:
        # cv2 有损，用PIL包切图更准确
        # img = cv2.imread(fp)
        img = Image.open(fp)
        w, h = img.size
        small_h = h // 3
        h1 = small_h
        h2 = small_h * 2
        base_name = os.path.basename(fp)
        print("处理图片：", w, h, base_name)
        img1 = img.crop((0, 0, w, h1))
        img1.save(os.path.join(output_path, "1_" + base_name))
        img2 = img.crop((0, h1, w, h2))
        img2.save(os.path.join(output_path, "2_" + base_name))
        img3 = img.crop((0, h2, w, h))
        img3.save(os.path.join(output_path, "3_" + base_name))


if __name__ == '__main__':
    # 图片输入路径
    input_path = "./data/5"
    # 图片输出路径
    output_path = "./data/5_out"
    split_process(input_path, output_path)
