import os
import multiprocessing
import time


def copy_work(source_dir, dest_dir, file_name):
    # 拼接源文件的路径和目标文件的路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path + "----->" + dest_path, end="\t")
    print(multiprocessing.current_process())
    with open(source_path, "rb") as source_file:
        # 创建目标文件
        with open(dest_path, "wb") as dest_file:
            # 循环读取文件
            while True:
                file_data = source_file.read(1024)
                if file_data:
                    dest_file.write(file_data)
                else:
                    break
    time.sleep(0.5)


if __name__ == '__main__':
    # 1.定义变量，保存源文件夹和目标文件夹
    source_dir = "./text"
    dest_dir = "./QAQ"
    # 2.在目标路径创建的文件夹
    try:
        os.mkdir(dest_dir)
    except Exception as e:
        print(f"文件夹已存在{e}")
    # 创建进程池
    pool = multiprocessing.Pool(3)
    # 显示文件夹内列表
    file_list = os.listdir(source_dir)
    for file_name in file_list:
        # 原路径 目标路径 名称
        # copy_work(source_dir, dest_dir, file_name)
        pool.apply_async(copy_work, (source_dir, dest_dir, file_name))

    pool.close()
    pool.join()
