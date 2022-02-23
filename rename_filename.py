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


def create_directory(src):
    dir_name = glob.glob(os.path.join(src, '*'))
    for date_count in dir_name:
        date = date_count.split('/')[-1:][0]
        resolution_dir = glob.glob(os.path.join(date_count, '*'))
        for resolution_count in resolution_dir:
            resolution = resolution_count.split('/')[-1:][0]
            region_dir = glob.glob(os.path.join(resolution_count, '*'))
            for region_count in region_dir:
                count = 1
                region = region_count.split('/')[-1:][0]
                file_dir = glob.glob(os.path.join(region_count, '*'))
                for file in file_dir:
                    count_str = str(count).zfill(4)
                    bag_name = file
                    count = count + 1
                    renamed_file = date + '_' + resolution + '_' + region + '_' + count_str + '.bag'
                    os.rename(bag_name, renamed_file)


if __name__ == "__main__":
    src_img = "/home/ri/workspace/test_image_picture"
    src_dir = "/home/ri/workspace/test_bagfiles"
    global_count = 1
    #rename_filename(src_img, global_count)
    create_directory(src_dir)