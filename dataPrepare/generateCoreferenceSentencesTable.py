import os
import re

import pymysql


def insert_sentence_data(sentence_list):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:
        cur.execute("delete from allCoreferenceSentences")

        sqli = "insert into allCoreferenceSentences values(%s,%s,%s)"
        # id#, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid

        for i, one_schema in enumerate(sentence_list):
            if len(one_schema[1])<3000:
                cur.execute(sqli, (i + 1, one_schema[0], one_schema[1]))
    except:

        print("Error: unable write data to table")

    cur.close()
    conn.commit()
    conn.close()
    return
    # =====================

def generateSentencesTableData():
    data_path = os.pardir + '/tempdata'
    file_allsentence = open(data_path + '/androidAPICoreferenceSentenceICSME.txt', 'r')
    sentence_list=[]
    for line in file_allsentence:
        data = re.split(r'\t+', line.rstrip('\t').rstrip('\r').rstrip('\n'))
        if len(data) == 2:
            key, value = data[0], data[1]
            sentence_list.append((key,value))
    insert_sentence_data(sentence_list)


generateSentencesTableData()
