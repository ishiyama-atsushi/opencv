import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

#save_all_frames('data/oregairuop.mp4', 'data/temp/result_png', 'sample_video_img', 'jpg')

#番号で指定したフレームを抜いてくる。
def save_frame(video_path, frame_num, result_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(os.path.dirname(result_path), exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(result_path, frame)

#save_frame('data/oregairuop.mp4', 500, 'data/temp2/result_single/sample_500.jpg')



def save_frame_range(video_path, start_frame, stop_frame, step_frame,
                     dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    for n in range(start_frame, stop_frame, step_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
        else:
            return

save_frame_range('data/oregairuop.mp4',
                 200, 300, 10,
                 'data/temp3/result_range', 'sample_video_img')
