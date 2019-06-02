import re

tag_header = re.compile(r'<h(\d).*>(.+)</h\d>')
source = """
<p>これはpタグ</p>
<h2>これはh2</h2>
<h3>これはh3</h3>
<h2 title="hoge">hoge</h2>
あああああああ
いいいいいいい
"""


def convert_header(m):
    count = int(m.group(1))
    content = m.group(2)
    return "#" * count + " " + content


result = tag_header.sub(convert_header, source)
result = re.sub(r"<p>", "-ppp-", result)
result = re.sub(r"</p>", "\n", result)
print(result)
