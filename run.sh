python init.py --video_path ./data/video.mp4 --frame_factor 5 --reso_factor 1
CUDA_VISIBLE_DEVICES=4 python preprocess.py --input data/video_f5
CUDA_VISIBLE_DEVICES=4 python train.py --config configs/video_f5r1.txt