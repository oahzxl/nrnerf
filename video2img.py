import os
import shutil
import cv2
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, default='./data/3_black.mp4')
    parser.add_argument("--reso_factor", type=int, default=1)
    parser.add_argument("--frame_factor", type=int, default=1)
    return parser.parse_args()


def read_video(video_path, save_path, frame_factor):
    cap = cv2.VideoCapture(video_path)
    n = 0
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.mkdir(save_path)
    _, frame = cap.read()
    while frame is not None:
        if n % frame_factor == 0:
            name = str(n)
            name = '0' * (6 - len(name)) + name
            cv2.imwrite(os.path.join(save_path, '%s.png' % name), frame)
        _, frame = cap.read()
        n += 1
    cap.release()


if __name__ == '__main__':
    args = parse_args()
    images_save_path = './data/' + args.video_path.split('/')[-1][:-4] + \
                       '_f%d' % args.frame_factor
    if not os.path.exists(images_save_path):
        os.mkdir(images_save_path)

    read_video(args.video_path, os.path.join(images_save_path, 'images'), args.frame_factor)
