import random
import cv2
import os
import numpy as np
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Video2Image")
    parser.add_argument("-i", required=True)
    parser.add_argument("-m", required=True)
    parser.add_argument("-n", required=True)
    parser.add_argument("-o", required=True)
    args = parser.parse_args()
    input_path = args.i
    output_path = args.o
    m = int(args.m)
    n = int(args.n)
    if m <= 0 or n <= 0:
        exit(0)
    if not os.path.exists(input_path):
        print("文件{}不存在！".format(input_path))
        exit(0)
    frame_list = []
    cap = cv2.VideoCapture(input_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_list.append(frame)
        print("loading...")
    cap.release()
    total = m * n
    frame_list_length = len(frame_list)
    if total >= frame_list_length:
        total = frame_list_length
    # 如果能整除则等间隔取，否则就随机取
    result_list = []
    k = frame_list_length % total
    if k == 0:
        sep = frame_list_length / total
        for index, frame in enumerate(frame_list):
            if index % sep == 0:
                result_list.append(frame)
    else:
        index_list = random.sample(range(0, frame_list_length), total)
        # 升序排列
        index_list.sort()
        for index in index_list:
            result_list.append(frame_list[index])
    assert len(result_list) > 0
    width = result_list[0].shape[1]
    height = result_list[0].shape[0]
    target_img = np.zeros((height*m, width*n, 3), np.uint8)
    for index, frame in enumerate(result_list):
        i = index // n
        j = index % n
        print(i, j)
        target_img[i*height:height+i*height, j*width:width+j*width, :] = frame
    cv2.imwrite(output_path, target_img)
    print(output_path)
