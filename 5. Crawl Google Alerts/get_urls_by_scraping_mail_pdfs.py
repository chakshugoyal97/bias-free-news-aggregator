import pdfquery
import pandas as pd
import re
from os import listdir
from os.path import isfile, join
from datetime import datetime

def string_clean(s):
    return re.sub(r'[^\x00-\x7f]',r' ', s).strip()

def process_pdf(pdf_link, filename, folder):
    print(pdf_link)
    pdf = pdfquery.PDFQuery(pdf_link)
    pdf.load()
    pdf_holder = []
    as_i = -20
    news_alert_date = ''
    pages = pdf.pq('LTPage')

    #pdf.tree.write("test2.xml", pretty_print=True, encoding="utf-8")

    ###########
    date_label = pdf.pq(pdf.pq(pdf.pq(pages[0])('LTTextBoxHorizontal')[0])('LTTextLineHorizontal')[2]).text()
    date_label = date_label[date_label.find(':')+1:].strip()
    date_label = ' '.join(date_label.split()[1:4])
    print(date_label)
    print("--------")

    for i, p in enumerate(pages):
        page = pdf.pq(p)
        URLs = page('Annot')
        for i, url in enumerate(URLs):
            url = str(pdf.pq(url))
            formatted = url[url.find('url=')+len('url='):]
            formatted = formatted[:formatted.find('&amp')]
            link_to_story = formatted
            if(link_to_story[0:4]=="http"):
                pdf_holder.append([date_label, link_to_story])

    df = pd.DataFrame(pdf_holder, columns=['feed-date', 'link'])
    return(df)


base_directory = r'base_o'
subfolders = ['alerts_4', 'alerts_3', 'alerts_2', 'alerts_5', 'alerts_24', 'alerts_23', 'alerts_15', \
'alerts_12', 'alerts_13', 'alerts_14', 'alerts_22', 'alerts_25', 'alerts_0', 'alerts_7', 'alerts_9', \
'alerts_8', 'alerts_6', 'alerts_1', 'alerts_20', 'alerts_18', 'alerts_11', 'alerts_16', 'alerts_17', \
'alerts_10', 'alerts_19', 'alerts_21']

all = []
for d in subfolders:
    folderPath = '{}/{}'.format(base_directory, d)
    onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    toprocess = ['{}/{}'.format(folderPath, o) for o in onlyfiles if '.pdf' in o]
    for t in toprocess:
        all.append(t)

frames = []
for a in all:
    df = process_pdf(a, a.split('/')[-1], a.split('/')[-2])
    frames.append(df)

output = pd.concat(frames)
output.to_csv(base_directory + '/output.csv', index=False)