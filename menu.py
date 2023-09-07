import os
dirlist=list()
path=os.getcwd()
dirname=os.path.join(path,"bugs")
for i in os.listdir(dirname):
    if os.path.isdir(os.path.join(dirname,i)):
        dirlist.append(i)

numlist=list()
for i in dirlist:
    if i.isdigit():
        numlist.append(i)


titles=list()
time_stamps=list()
youtube_link=list()
for i in numlist:
    with open(os.path.join(dirname,i,"main.md"),mode="r",encoding="utf_8") as f_read:
        contents=f_read.readlines()
        titles.append(contents[0][2:-1])
        time_stamps.append(contents[1][4:-1])
        youtube_link.append(contents[2][4:-1])

note=list()

note.append("# 目次")
note.append("\n")
note.append("|項目(クリックで詳細ファイル)|日付|報告タイトル|バグレポートリンク|動画リンク|")
note.append("\n")
note.append("|--|--|--|--|--|--|")
note.append("\n")

for i in range(len(numlist)):
    a_line="|[MC-"+numlist[i]+"](bugs/"+numlist[i]+"/main.md)"+"|"+time_stamps[i]+"|"+titles[i]+"|"+"https://bugs.mojang.com/browse/MC-"+numlist[i]+"|"+youtube_link[i]+"|"
    note.append(a_line)
    note.append("\n")

with open(os.path.join(path,"menu.md"),mode="r",encoding="utf_8") as f_read:
    note=note+["\n"]+f_read.readlines()


with open ("README.md",encoding="utf_8",mode="w") as f_menu:
    f_menu.writelines(note)




