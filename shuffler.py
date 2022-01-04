import os
import opencv
import imghdr

# random.shuffle(files)

def rename_folder_content(folder, prefix):
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{prefix}{str(count)}.jpg"
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)



def check_images( s_dir, ext_list):
    bad_images=[]
    bad_ext=[]
    s_list= os.listdir(s_dir)
    for klass in s_list:
        klass_path=os.path.join (s_dir, klass)
        print ('processing class directory ', klass)
        if os.path.isdir(klass_path):
            file_list=os.listdir(klass_path)
            for f in file_list:
                f_path=os.path.join (klass_path,f)
                tip = imghdr.what(f_path)
                if ext_list.count(tip) == 0:
                  bad_images.append(f_path)
                if os.path.isfile(f_path):
                    try:
                        img=cv2.imread(f_path)
                        shape=img.shape
                    except:
                        print('file ', f_path, ' is not a valid image file')
                        bad_images.append(f_path)
                else:
                    print('*** fatal error, you a sub directory ', f, ' in class directory ', klass)
        else:
            print ('*** WARNING*** you have files in ', s_dir, ' it should only contain sub directories')
    return bad_images, bad_ext

source_dir =r'c:\temp\people\storage'
good_exts=['jpg', 'png', 'jpeg', 'gif', 'bmp' ] # list of acceptable extensions
bad_file_list, bad_ext_list=check_images(source_dir, good_exts)
if len(bad_file_list) !=0:
    print('improper image files are listed below')
    for i in range (len(bad_file_list)):
        print (bad_file_list[i])
else:
    print(' no improper image files were found')


def main():
    # folder_dw = 'dataset_lettuce/Fungal/Downy mildew on lettuce'
    source = 'dataset_lettuce/train/f'

    files = os.listdir(source)
    # for folder_name in files:
    #     folder = 'dataset_lettuce/train/f/' + folder_name
    #
    #     prefix = folder_name.split()[0][0].lower()
    #     print(prefix)
    #     print('Renaming folder: ', folder)
    #     rename_folder_content(folder, prefix)
    # rename_folder_content(folder, )
    # folder = 'dataset_lettuce/Bacterial'
    # rename_folder_content(folder, 'b')
    #
    # folder = 'dataset_lettuce/Viral'
    # rename_folder_content(folder, 'v')
    # folder = 'dataset_lettuce/val/h'
    # rename_folder_content(folder, 'h')
    # folder = 'dataset_lettuce/val/v'
    # rename_folder_content(folder, 'v')
    # folder = 'dataset_lettuce/val/b'
    # rename_folder_content(folder, 'b')
    # folder = 'dataset_lettuce/val/f/d'
    # rename_folder_content(folder, 'd')
    # folder = 'dataset_lettuce/val/f/w'
    # rename_folder_content(folder, 'w')
    # folder = 'dataset_lettuce/val/f/p'
    # rename_folder_content(folder, 'p')
    # folder = 'dataset_lettuce/val/f/s'
    # rename_folder_content(folder, 's')

    folder = 'dataset_lettuce/train/f/d'
    rename_folder_content(folder, 'd')
    folder = 'dataset_lettuce/train/f/s'
    rename_folder_content(folder, 's')

if __name__ == '__main__':
    main()