import os, glob
import natsort


def rename_filename(src, global_count):
    dir_name = glob.glob(os.path.join(src, '*', '*'))
    for dir_count in dir_name:
        test_dir = glob.glob(os.path.join(dir_count, '*', '*'))
        for day in natsort.natsorted(test_dir):
            day_image = glob.glob(os.path.join(day, 'image', '*.jpg'))
            day_lidar = glob.glob(os.path.join(day, 'lidar', '*.npy'))
            for (image, lidar) in zip(natsort.natsorted(day_image), natsort.natsorted(day_lidar)):
                global_count_str = str(global_count).zfill(6)
                print(image[:-10] + global_count_str + '.jpg')
                print(lidar[:-10] + global_count_str + '.npy')
                global_count = global_count + 1
                #os.rename(image, )

if __name__ == "__main__":
    src = "src"
    global_count = 1
    rename_filename(src, global_count)