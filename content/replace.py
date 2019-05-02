import os

stack = []


def collect_md_files(file):
    if os.path.isdir(file):
        file_list = os.listdir(file)
        for file in file_list:
            collect_md_files(file)
    else:
        base, ext = os.path.splitext(file)
        print("base:", base, " ext:", ext)
        if ext == ".md":
            stack.append(file)


base_path = os.path.dirname(__file__)
file_list = os.scandir(os.path.join(base_path, "post"))
for file in file_list:
    collect_md_files(file)

print("stack size: ", len(stack))
for file in stack:
    print("stack: ", os.path.abspath(file))
