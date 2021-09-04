import re


def parse(markdown):
    s = markdown
    s=re.sub(r"__(.+?)__",r"<strong>\1</strong>",s) # --
    s=re.sub(r"_(.+?)_",r"<em>\1</em>",s) # - 
    s=re.sub(r"^\*\s*(.+?$)",r"<li>\1</li>",s,flags=re.M) # *
    s=re.sub(r"(<li>.*</li>)",r"<ul>\1</ul>",s,flags=re.S) # li 
    for i in range(6,0,-1):
        s=re.sub(r"^{}\s*(.*?$)".format("#"*i),r"<h{0}>\1</h{0}>".format(i),s,flags=re.M) # title h
    s=re.sub (r"^(?!<[hul])(.*?$)",r"<p>\1</p>",s,flags=re.M) # <hul p
    s=re.sub(r"\n","",s) # \n
    return s