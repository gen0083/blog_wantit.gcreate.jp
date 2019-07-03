import os
import re

stack = []


def collect_md_files(file):
    if os.path.isdir(file):
        files_in_dir = os.scandir(file)
        for f in files_in_dir:
            collect_md_files(f)
    else:
        base, ext = os.path.splitext(file)
        if ext == ".md":
            match = filter_truncated_description(file)
            if match:
                stack.append(dict(path=file.path, desc=match.group(0)))


def filter_truncated_description(file):
    with open(file, mode='r') as f:
        src = f.read()
        match = re.search(r'^description:.+', src, re.MULTILINE)
        f.close()
        return match


# collect target files
base_path = os.getcwd()
file_list = os.scandir(os.path.join(base_path, "content", "post"))
for file in file_list:
    collect_md_files(file)

for t in stack:
    print(f"{t['path']}\n{t['desc']}\n")
