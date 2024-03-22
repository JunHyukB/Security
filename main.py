# This is a sample Python script.
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# 문단 정렬
#from docx.enum.text import WD_ALIGN_PARAGRAPH
# 문자 스타일 변경
#from docx.enum.style import WD_STYLE_TYPE
# 가장 기본적인 기능(문서 열기, 저장, 글자 쓰기 등등)
#from docx import Document
import pandas as pd
from datetime import datetime, timedelta
import re
import tkinter as tk
from tkinter import filedialog

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
"""
def docx():
    doc = Document()
    doc.save('/Users/jun/Desktop/test.docx')

def excel(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    df = df.replace(np.nan,'',regex=True) #엑셀 공백 처리

    #html(df.head())
    text_name = ""
    text_src = ""
    text_dst = ""
    p = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+") #ip 정규표현식

    for i in df.index:
        if df['탐지유형'][i] != "":
            text_name = text_name + df['탐지유형'][i] + "(" + df['탐지 이벤트'][i] + "건)\n"

        if df['공격대상'][i] != "":
            if p.match(df['공격대상'][i]):
                if text_src != (df['공격대상'][i] + "(" + df.iat[i,5] + "), "): #중복제거 로직 아직 미완
                    text_src = text_src + df['공격대상'][i] + "(" + df.iat[i,5] + "), "
            else:
                if df.iat[i, 7] == "" and text_src !="": #소스열이 IP가 아니고8번째 열이 빈칸이면
                    text_src = text_src[:-2]            #", " 지우고 줄바꾸기
                    text_src = text_src + "\n"

        if p.match(df.iat[i,7]):        #목적지 열이 ip면
            text_dst = text_dst + df.iat[i,7] + "(tcp/" + df.iat[i,8] + "), "
        else:
            if df.iat[i,7] == "" and text_dst != "":    #목적지 열이 빈칸이고 목적지 변수가 널값이 아니면
                text_dst = text_dst[:-2]
                text_dst = text_dst + "\n"
    text_name = text_name[:-1]
    text_src = text_src[:-2]
    text_dst = text_dst[:-2]
    list1 = text_name.split("\n")
    list2 = text_src.split("\n")
    list3 = text_dst.split("\n")

    html("""<!DOCTYPE html><html><head><title>report</title><meta charset="UTF-8"></head><body><table>""")
    for j in range(0,len(list1)):
        #print(list1[j])
        #print(list2[j])
        #print(list3[j])
        html("◼︎"+list1[j])
        html("<table border='1' width='700>")
        html("<tr height='30'><th rowspan='1'width='100'>출발지</th><td>"+list2[j]+"</td></tr>")
        html("<tr height='30'><th rowspan='1'>목적지</th><td>"+list3[j]+"</td></tr>")
        html("<tr height='30'><th><td></td></th></tr>")
        html("<tr height='30'><th><td></td></th></tr>")
        html("<tr height='30'><th><td></td></th></tr></table>")
    html("""</body></html>""")


def html(excelfile):
    #html_text = """<!DOCTYPE html><html><head><title>report</title><meta charset="UTF-8"></head><body>""" + excelfile.to_html() + """</body></html>"""
    html_text = ""
    html_text = html_text + excelfile

    #html_file = open("/Users/jun/Desktop/report.html",'w')
    html_file = open("/Users/jun/Desktop/report.html", 'a+')
    html_file.write(html_text)
    html_file.close()

def tktk():
    files = filedialog.askopenfilename(initialdir="./",title="hi")
    return files

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    a = datetime.today()#- timedelta(1)
    #filename = "/Users/jun/Desktop/탐지분석_"+a.strftime("%Y-%m-%d")+".xlsx"
    filename = tktk()
    excel(filename)
