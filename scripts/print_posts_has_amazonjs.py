import os
import re
import sys
import termios

stack = []
# refer: https://qiita.com/tortuepin/items/9ede6ca603ddc74f91ba
# 標準入力のファイルディスクリプタを取得
fd = sys.stdin.fileno()

# fdの端末属性をゲットする
# oldとnewには同じものが入る。
# newに変更を加えて、適応する
# oldは、後で元に戻すため
old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)

# new[3]はlflags
# ICANON(カノニカルモードのフラグ)を外す
new[3] &= ~termios.ICANON
# ECHO(入力された文字を表示するか否かのフラグ)を外す
new[3] &= ~termios.ECHO


def collect_md_files(file):
    if os.path.isdir(file):
        files_in_dir = os.scandir(file)
        for f in files_in_dir:
            collect_md_files(f)
    else:
        base, ext = os.path.splitext(file)
        if ext == ".md":
            match = filter_has_amazonjs_block(file)
            if len(match) > 0:
                stack.append(dict(path=file.path, amazon=match))


def filter_has_amazonjs_block(file):
    with open(file, mode='r') as f:
        src = f.read()
        match = re.findall(r'.*<div data-role="amazonjs".+', src)
        f.close()
        return match


def user_input_without_enter(count):
    print(f"remain {count} posts: if exit scripts: enter [q] / print next enter [any]:")
    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)
    return ch


# collect target files
base_path = os.getcwd()
file_list = os.scandir(os.path.join(base_path, "content", "post"))
for file in file_list:
    collect_md_files(file)

count = len(stack)
print(f"matched posts are {count}")
for t in stack:
    print(t["path"])
    for amazon in t["amazon"]:
        match = re.match(r'.*data-asin="(?P<asin>.+?)".*<a.+?>(?P<title>.+?)</a>.*', amazon)
        print(f"{match['title']}: https://amazon.co.jp/dp/{match['asin']}")
    print("")
    count -= 1
    if count == 0:
        exit(0)
    # judge to continue or exit by user
    users_input = user_input_without_enter(count)
    if users_input.strip() == "q":
        print("aborted!")
        exit(0)
