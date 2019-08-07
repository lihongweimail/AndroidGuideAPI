import os

import pymysql


def genfilename():
    path=os.pardir

    file_filelist = open(os.pardir+'/tempdata/filenamelist_copy.csv')
    filename_list = []
    for filenameline in file_filelist:
        filenames = filenameline.split(',', 1)
        if len(filenames) == 2:
            filename_list.append((filenames[0],filenames[1].strip('\n')))

    return filename_list



def gendata(lists):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:

        sqli = "insert into filenamelist values(%s,%s,%s)"
        # id#, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid

        for i, one_schema in enumerate(lists):
            cur.execute(sqli, (i + 1, one_schema[0], one_schema[1]))
    except:

        print("Error: unable write data to table")

    cur.close()
    conn.commit()
    conn.close()
    return
        # =====================

def main():
    lists=genfilename()
    gendata(lists)
    return

main()


