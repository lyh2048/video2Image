import argparse
from fileinput import filename
import os
import cv2


'''
Video2Image
'''


def run(video_path, ouput, interval):
    # 判断视频文件是否存在
    if not os.path.exists(video_path):
        print(f'文件 {video_path} 不存在')
        exit(-1)
    # 判断输出目录是否存在
    if not os.path.exists(output):
        os.makedirs(output)
    # 提取视频名称
    video_name = video_path.split('/')[-1]
    # 读入视频
    cap = cv2.VideoCapture(video_path)
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % interval == 0:
            filename = f'{video_name.split(".")[0]}_{str(i)}.png'
            save_image(output, filename, frame)
        i += 1
    cap.release()


def save_image(output, filename, img):
    cv2.imwrite(os.path.join(output, filename), img)
    print(f'write:{os.path.join(output, filename)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video2Image')
    parser.add_argument('-input', type=str, required=True, help='输入视频的路径')
    parser.add_argument('-output', type=str, default='./output', help='保存位置')
    parser.add_argument('-interval', type=int, default=5, help='指定间隔')
    args = parser.parse_args()
    video_path = args.input
    output = args.output
    interval= args.interval
    print('---- Video2Image ----')
    run(video_path, output, interval)
    print('处理完成, 输出路径:', output)
    print('---- Video2Image ----')