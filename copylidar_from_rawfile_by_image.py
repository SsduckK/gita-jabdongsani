import os, glob
import shutil


def trim_empty_anno_frames(src_path, dst_path):
    dir_names = glob.glob(os.path.join(src_path,"*"))	#src_path 폴더 아래 모든 파일을 리스트로 구성
    dest_dir = glob.glob(os.path.join(dst_path, "*"))	#dst_path 폴더 아래 모든 파일을 리스트로 구성
    for (dir_, dest) in zip(dir_names, dest_dir):	
        image_files = glob.glob(os.path.join(dest, "image", "*.jpg"))	#dest폴더 아래 image 폴더에서 jpg로 끝나는 파일을 리스트로
        lidar_files = glob.glob(os.path.join(dir_, "lidar", "*.npy"))	#dir_ 폴더 아래 lidar 폴더에서 npy로 끝나는 파일을 리스트로
        lidar_directory = os.path.join(dest, "lidar")			#dest폴더 아래 lidar 폴더를 리스트로

        for lidar_file in lidar_files:
            checking_file = lidar_file.replace('src_directory/', 'dst_directory/').replace('lidar/', 'image/').replace('.npy', '.jpg')	#파일의 경로 수정 및 lidar.npy를 image.jpg로 변환
            													#이를 통해 image파일과 lidar파일의 이름을 일치시킬 수 있음
            if checking_file in image_files:			#lidar파일에서 변환된 image 파일이 있을경우 복사를 수행하는 반복문
                print("copied :", lidar_file)
                shutil.copy(lidar_file, lidar_directory)


if __name__ == "__main__":
    src = "src"		#복사할 파일 경로
    dst = "dst"		#복사한 파일 경로
    trim_empty_anno_frames(src, dst)
