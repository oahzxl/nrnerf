import argparse
import os
import cv2
import shutil
import subprocess
from video2img import read_video
from preprocess import preprocess
import configargparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, default='./data/0325_3_black.mp4')
    parser.add_argument("--frame_factor", type=int, default=2)
    parser.add_argument("--reso_factor", type=int, default=2)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    save_path = './data/' + args.video_path.split('/')[-1][:-4] + '_f%d' % args.frame_factor
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    read_video(args.video_path, os.path.join(save_path, 'images'), args.frame_factor)

    # config
    config_name = args.video_path.split('/')[-1][:-4] + '_f%dr%d' % (args.frame_factor, args.reso_factor)
    with open("./configs/example_sequence.txt", 'r') as f:
        config = f.readlines()
    config[1] = 'datadir = ' + save_path + '\n'
    config[3] = 'rootdir = logs' + '\n'
    config[4] = 'expname = ' + config_name + '\n'
    config[11] = 'factor = %d' % args.reso_factor + '\n'
    with open(os.path.join('./configs', config_name + '.txt'), 'w+') as f:
        f.writelines(config)
