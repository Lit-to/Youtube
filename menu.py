# menu.md作成用
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

line_out =list()
for i in range(len(numlist)):
    with open(os.path.join(dirname,numlist[i],"main.md"),mode="r",encoding="utf_8") as f_read:
        contents=f_read.readlines()
        inp={"titles":str(),"page_id":int(),"time_stamps":str(),"youtube_link":str()}
        line_out.append(inp)
        line_out[i]["titles"]=contents[0][2:-1]
        line_out[i]["page_id"]=int(contents[1][4:8]+contents[1][9:11]+contents[1][12:14]+contents[1][15:17]+contents[1][18:20]+contents[1][21:23]+contents[1][24:26]+contents[1][27:29]+contents[1][30:32])
        line_out[i]["time_stamps"]=contents[1][4:-1]
        line_out[i]["youtube_link"]=contents[2][4:-1]
        line_out[i]["numlist"]=numlist[i]

line_out=sorted(line_out, key=lambda x:x["page_id"])
note=list()

note.append("# 目次")
note.append("\n")
note.append("|項目(クリックで詳細ファイル)|日付|報告タイトル|バグレポートリンク|動画リンク|")
note.append("\n")
note.append("|--|--|--|--|--|")
note.append("\n")


for i in range(len(numlist)):
    a_line="|[MC-"+str(line_out[i]["numlist"])+"](bugs/"+str(line_out[i]["numlist"])+"/main.md)"+"|"+line_out[i]["time_stamps"]+"|"+line_out[i]["titles"]+"|"+"https://bugs.mojang.com/browse/MC-"+str(line_out[i]["numlist"])+"|"+line_out[i]["youtube_link"]+"|"
    note.append(a_line)
    note.append("\n")

with open(os.path.join(path,"menu.md"),mode="r",encoding="utf_8") as f_read:
    note=note+["\n"]+f_read.readlines()


with open ("README.md",encoding="utf_8",mode="w") as f_menu:
    f_menu.writelines(note)




