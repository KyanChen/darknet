import os
import glob

trainPath = "data/kaikeba_drone/data4YOLO/train"
testPath = "data/kaikeba_drone/data4YOLO/train"
names = ["train.txt", "test.txt"]
img_format = 'jpg'


def gen_img_path_list(phase, path):
    dirlist = glob.glob(os.path.abspath(os.path.join(path, '*.%s' % img_format)))
    # 生成txt
    with open(phase, "w") as fp:
        for index, file in enumerate(dirlist):
            fp.write(file)
            if index == len(dirlist)-1:
                break
            fp.write("\n")
        fp.close()


for phase in names:
    if phase == "train.txt":
        gen_img_path_list(phase, trainPath)
    else:
        gen_img_path_list(phase, testPath)




