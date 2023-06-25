import os


class File_system:
    path = None
    file_list = None

    def __init__(self, path):
        self.path = path
        self.file_list = os.listdir(path)

    def check_new_files(self):
        current_files = os.listdir(self.path)
        new_files = [file for file in current_files if file not in self.file_list]
        self.file_list = current_files  # 更新文件列表
        return new_files


if __name__ == "__main__":
    # 示例用法
    test = File_system("./temp")
    print(test.file_list)

    # 检查是否出现新的文件
    new_files = test.check_new_files()
    if new_files:
        print("发现新的文件:")
        for file in new_files:
            print(file)
    else:
        print("没有发现新的文件")
