import os
import shutil


def traverse_copy_obj(origin_path, target_path):
    classes = os.listdir(origin_path)
    count = 0
    for class_name in classes:
        cls_path = os.path.join(origin_path, class_name)
        tg_cls_path = os.path.join(target_path, class_name)
        item_list = os.listdir(cls_path)
        for item in item_list:
            crt_path = os.path.join(cls_path, item, "models/model_normalized.obj")
            tg_path  = os.path.join(tg_cls_path, item)
            if not os.path.exists(crt_path):
                continue
            if not os.path.exists(tg_path):
                os.makedirs(tg_path)
            file_path = os.path.join(tg_path, "model_normalized.obj")
            if os.path.exists(file_path):
                count += 1
                continue
            shutil.copyfile(crt_path, file_path)
            count += 1
            if count % 1000 == 0:
                print("{} have been copied.".format(count))
    print("Copy Finished.")


def traverse_copy_img(origin_path, target_path):
    classes = os.listdir(origin_path)
    count = 0
    for class_name in classes:
        cls_path = os.path.join(origin_path, class_name)
        tg_cls_path = os.path.join(target_path, class_name)
        item_list = os.listdir(cls_path)
        for item in item_list:
            crt_path = os.path.join(cls_path, item, "rendering")
            if not os.path.exists(crt_path):
                continue
            img_lst = os.listdir(crt_path)
            tg_path = os.path.join(tg_cls_path, item)
            if not os.path.exists(tg_path):
                os.makedirs(tg_path)
            for img_name in img_lst:
                file_path = os.path.join(tg_path, img_name)
                if os.path.exists(file_path):
                    count += 1
                    if count % 500 == 0:
                        print("{} have been copied.".format(count))
                    continue
                img_src = os.path.join(crt_path, img_name)
                # print(img_src, "===>", file_path)
                shutil.copyfile(img_src, file_path)
                count += 1
                if count % 500 == 0:
                    print("{} have been copied.".format(count))
    print("Copy Finished.")


if __name__ == "__main__":
    # origin_path = "/media/yunhaoli/YunhaoLi_CS/ShapeNet/TrainingDataTemp"
    # target_path = "/media/yunhaoli/YunhaoLi_CS/ShapeNet/TrainingData"
    # traverse_copy_obj(origin_path, target_path)
    origin_path = "/media/yunhaoli/YunhaoLi_CS/ShapeNet/ShapeNetRendering"
    target_path = "/media/yunhaoli/YunhaoLi_CS/ShapeNet/TrainingData"
    traverse_copy_img(origin_path, target_path)