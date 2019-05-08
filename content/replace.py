import os
import re

stack = []


def collect_md_files(file):
    if os.path.isdir(file):
        file_list = os.scandir(file)
        for file in file_list:
            collect_md_files(file)
    else:
        base, ext = os.path.splitext(file)
        print("base:", base, " ext:", ext)
        if ext == ".md":
            stack.append(file)


def replace_tags(src):
    open_p = re.compile(r'<p>')
    close_p = re.compile(r'</p>')
    tag_header = re.compile(r'<h(\d).*>(.+)</h\d>')
    tag_break = re.compile(r'<br.*>')
    rename_cover_image = re.compile(r'cover_image:')

    def convert_header(m):
        count = int(m.group(1))
        content = m.group(2)
        return "\n" + "#" * count + " " + content + "\n\n"

    def replace_source(source):
        dst = open_p.sub("", source)
        dst = close_p.sub("\n", dst)
        dst = tag_header.sub(convert_header, dst)
        dst = tag_break.sub("", dst)
        dst = rename_cover_image.sub("featuredimage:", dst)
        return dst

    return replace_source(src)


# collect target files
base_path = os.path.dirname(__file__)
file_list = os.scandir(os.path.join(base_path, "post"))
for file in file_list:
    collect_md_files(file)

# work on each file
print("stack size: ", len(stack))
for file in stack:
    file_path = os.path.abspath(file)
    print("stack: ", file_path)
    with open(file_path, mode="r+") as f:
        src = f.read()
        # do replace here
        after = replace_tags(src)
        # end replace
        f.close()
    with open(file_path, mode="w") as f:
        f.write(after)
        f.close()
