import os, glob

def trim_empty_anno_frames(src_path):
    dir_names = glob.glob(os.path.join(src_path,"*"))	#src_path 폴더 아래 모든 파일을 리스트로 구성
    for dir_ in dir_names:
        image_files = glob.glob(os.path.join(dir_, "image", "*.jpg"))	#dir_폴더 아래 image 폴더에서 jpg로 끝나는 파일을 리스트로
        lidar_files = glob.glob(os.path.join(dir_, "lidar", "*.npy"))	#dir_폴더 아래 lidar 폴더에서 npy로 끝나는 파일을 리스트로

        for lidar_file in lidar_files:
            checking_file = lidar_file.replace('src_directory', 'dst_directory/').replace('lidar/', 'image/').replace('.npy', '.jpg')	#파일의 경로 수정 및 lidar.npy를 image.jpg로 변환
            													#이를 통해 image파일과 lidar파일의 이름을 일치시킬 수 있음
            if checking_file not in image_files:			#lidar파일에서 변환된 image 파일이 있을경우 복사를 수행하는 반복문
                print("removed :", lidar_file)
                os.remove(lidar_file)


if __name__ == "__main__":
    src = "/src"		#처리할 파일 경로
    trim_empty_anno_frames(src)
