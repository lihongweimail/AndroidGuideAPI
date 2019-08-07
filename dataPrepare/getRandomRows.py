import re

import pymysql



def getOneSentence():
    all_Sent_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("SELECT * FROM allCoreferenceSentences AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM allCoreferenceSentences)-(SELECT MIN(id) FROM allCoreferenceSentences))+(SELECT MIN(id) FROM allCoreferenceSentences)) AS id) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id LIMIT 1")
    results = cur.fetchall()

    for row in results:
        id= row[0]
        sentenceid = row[1]
        sentencetext = row[2]

        doc_id='1'
        if '_'  in sentenceid:
            doc_id=sentenceid.split('_')[0]

        cur.execute('select fileURL from filenamelist where fileID=%s', doc_id)
        newres=cur.fetchall()
        url=''
        for row2 in newres:
            url=row2[0]

        all_Sent_list.append((sentenceid,sentencetext,url))

    cur.close()
    conn.close()

    return all_Sent_list




def generate_sent_data(sent_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute('SELECT id FROM RandomSentence ORDER BY id DESC LIMIT 1')
    results = cur.fetchall()
    lastid=0
    for row in results:
        lastid = row[0]
    sqli = "insert into RandomSentence values(%s,%s,%s,%s)"
    for i, one_schema in enumerate(sent_list):
        cur.execute(sqli, (lastid+i + 1, one_schema[0],one_schema[1],one_schema[2]))
    cur.close()
    conn.commit()
    conn.close()
    return


def get_N_Sentence(N):

    for i in range(0,N):
        sentence=getOneSentence()
        generate_sent_data(sentence)
    return


def updateAllrelation():

    relationlist=[]

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute('SELECT id,sentence_id FROM allRelations ORDER BY id')
    results = cur.fetchall()


    for row in results:
        id=row[0]
        sentence_id=row[1]
        relationlist.append((id,sentence_id))
    cur.close()
    conn.commit()

    cur = conn.cursor()
    doc_id=''

    for rows in relationlist:
        doc_id=rows[1].split('_')[0]
        sqli="update allRelations set urlid=%s where id=%s"
        cur.execute(sqli, (doc_id,rows[0]))
    cur.close()
    conn.commit()


    conn.close()
    return


def getOneLink(openlink,declaredlink):
    # maxid  16115244
    # minid  1

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:

        # try:
        cur.execute("SELECT * FROM linkEntitysNew AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM linkEntitysNew)-(SELECT MIN(id) FROM linkEntitysNew))+(SELECT MIN(id) FROM linkEntitysNew)) AS id) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id LIMIT 1")
        results = cur.fetchall()

        for row in results:
            id= row[0]
            entity_id= row[1]
            relation_id = row[2]

            rel_urlid=''
            if '_'  in relation_id:
                rel_urlid=relation_id.split('_')[0]

        # print('entity_id:',entity_id)


        warning_id=''
        rel_id=''






        cur.execute('select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from  entities where id=%s', entity_id)
        newEtities=cur.fetchall()
        entity_urlid=''

        for row2 in newEtities:
            entity_id= row2[0]
            entity_name= row2[1]
            entity_senction= row2[2]
            entity_url = row2[3]
            entity_parent= row2[4]
            entity_type= row2[5]
            entity_original= row2[6]
            entity_urlid= row2[7]
            entity_qualifiedname= row2[8]
            # print("row2 : entities\n")
            # print(row2)

        if len(entity_name)>4:

            # print(rel_urlid,entity_urlid)


            cur.execute("select id, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid from Warning where relationid=%s", relation_id)
            warningrecods=cur.fetchall()

            for oneWarning in warningrecods:
                warning_id=oneWarning[0]
                warning_Tag=oneWarning[1]
                warning_Section =oneWarning[2]
                warning_Text=oneWarning[3]
                warning_Type=oneWarning[4]
                warning_URL=oneWarning[5]
                warning_SentenceId=oneWarning[6]
                warning_Relationid=oneWarning[7]
                # print("oneWarning: warning\n")
                # print(oneWarning)



            cur.execute('select id , subject_ori, relation_ori, object_ori,  pos  from allrelations where rel_id=%s',relation_id)
            relationlist=cur.fetchall()

            for onerelation in relationlist:
                rel_id=onerelation[0]
                subject_ori=onerelation[1]
                relation_ori=onerelation[2]
                object_ori=onerelation[3]
                pos=onerelation[4]
                # print("relation : \n")
                # print(onerelation)

            # print(entity_id,warning_id,rel_id)

            if entity_id!='' and warning_id!='' and  rel_id!='':

                if rel_urlid == entity_urlid:
                    declaredlink.append((entity_id,entity_name,entity_url,warning_id,rel_id,warning_Text, warning_URL, subject_ori,relation_ori,object_ori,pos,warning_Tag,warning_Type))
                    # print((entity_id,entity_name,entity_url,warning_id,rel_id,warning_Text, warning_URL, subject_ori,relation_ori,object_ori,pos,warning_Tag,warning_Type))

                else:
                    openlink.append((entity_id,entity_name,entity_url,warning_id,rel_id,warning_Text, warning_URL, subject_ori,relation_ori,object_ori,pos,warning_Tag,warning_Type))

    except:

        print("Error: unable write data to table")

    cur.close()
    conn.close()

    return


# =====================


def generate_declared_sample_data(sent_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute('SELECT id FROM randomLinkRows ORDER BY id DESC LIMIT 1')
    results = cur.fetchall()
    lastid=0
    for row in results:
        lastid = row[0]
    sqli = "insert into randomLinkRows values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    i=0
    for  one_schema in sent_list:
        cur.execute(sqli, (lastid+i + 1, one_schema[0],one_schema[1],one_schema[2], one_schema[3],one_schema[4],one_schema[5], one_schema[6],one_schema[7],one_schema[8], one_schema[9],one_schema[10], one_schema[11],one_schema[12]))
        i=i+1

    print('write an declared link data')
    print(lastid)
    cur.close()
    conn.commit()
    conn.close()
    return
# =======


def generate_openlink_sample_data(sent_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute('SELECT id FROM randomOpenLinkRows ORDER BY id DESC LIMIT 1')
    results = cur.fetchall()
    lastid=0
    for row in results:
        lastid = row[0]
    sqli = "insert into randomOpenLinkRows values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    i=0
    for  one_schema in sent_list:
        cur.execute(sqli, (lastid+i + 1, one_schema[0],one_schema[1],one_schema[2], one_schema[3],one_schema[4],one_schema[5], one_schema[6],one_schema[7],one_schema[8], one_schema[9],one_schema[10], one_schema[11],one_schema[12]))
        i=i+1

    print('write an open link data')
    print(lastid)
    cur.close()
    conn.commit()
    conn.close()
    return

# ===



def get_N_sample(N):

    for i in range(0,N):
        openlink=[]
        declaredlink=[]

        getOneLink(openlink, declaredlink)

        if len(declaredlink)>0:
            generate_declared_sample_data(declaredlink)
        if len(openlink)>0:
            generate_openlink_sample_data(openlink)
    return


def generate_allsent_data(sent_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()


    sqli = "insert into allSentences values(%s,%s,%s)"
    for i, one_schema in enumerate(sent_list):
        cur.execute(sqli, (i + 1, one_schema[0],one_schema[1]))
    cur.close()
    conn.commit()
    conn.close()
    return

def getallsentence():
    file_allsentence = open('/Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata/AndroidAPI_allSent_ascii.txt')
    allsentencelist=[]
    for line in file_allsentence:
        data = re.split(r'\t+', line.strip('\t').rstrip('\r').rstrip('\n'))
        if len(data) == 2:
            if len(data[1])<3000:
                allsentencelist.append((data[0], data[1]))
    file_allsentence.close()

    generate_allsent_data(allsentencelist)

    return


# compare_exact_string
def c_e_s(checkword, checkString):
    ablankre = re.compile(r'\s+')
    checkString=ablankre.sub(' ',checkString)
    checkword = ablankre.sub(' ', checkword)
    str1list = checkword.split()
    str2list = checkString.split()
    flag = True
    for word in str1list:
        if word not in str2list:
            flag = False
            break;
    return flag




def getOneSentencefromAll():
    all_Sent_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("SELECT * FROM allSentences  AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM allSentences)-(SELECT MIN(id) FROM allSentences))+(SELECT MIN(id) FROM allSentences)) AS id) AS t2 WHERE  t1.id >= t2.id ORDER BY t1.id LIMIT 1")
    results = cur.fetchall()

    for row in results:
        id= row[0]
        sentenceid = row[1]
        sentencetext = row[2]

        doc_id='1'
        if '_'  in sentenceid:
            doc_id=sentenceid.split('_')[0]

        cur.execute('select fileURL from filenamelist where fileID=%s', doc_id)
        newres=cur.fetchall()
        url=''
        for row2 in newres:
            url=row2[0]
        if len(sentencetext)>50:
            if c_e_s('this',str.lower(sentencetext)) or c_e_s('that',str.lower(sentencetext)) or c_e_s('it', str.lower(sentencetext)) or c_e_s('those', str.lower(sentencetext)) or c_e_s('these', str.lower(sentencetext)) or c_e_s('which', str.lower(sentencetext)) or c_e_s('the', str.lower(sentencetext)) or c_e_s('they', str.lower(sentencetext)) or c_e_s('who', str.lower(sentencetext)) or c_e_s('our', str.lower(sentencetext)) or c_e_s('you', str.lower(sentencetext)) or c_e_s('your', str.lower(sentencetext)) or c_e_s('he', str.lower(sentencetext)) or c_e_s('his', str.lower(sentencetext)) or c_e_s('its', str.lower(sentencetext)) or c_e_s('we', str.lower(sentencetext)) or c_e_s('developers', str.lower(sentencetext)) or c_e_s('developer', str.lower(sentencetext)) or c_e_s('him', str.lower(sentencetext)) or c_e_s('she', str.lower(sentencetext)) or c_e_s('her', str.lower(sentencetext)):
                all_Sent_list.append((sentenceid,sentencetext,url))

    cur.close()
    conn.close()

    return all_Sent_list





def generate_sent_alldata(sent_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute('SELECT id FROM RandomSentence ORDER BY id DESC LIMIT 1')
    results = cur.fetchall()
    lastid=0
    for row in results:
        lastid = row[0]
    sqli = "insert into RandomSentence values(%s,%s,%s,%s)"
    for i, one_schema in enumerate(sent_list):
        cur.execute(sqli, (lastid+i + 1, one_schema[0],one_schema[1],one_schema[2]))
    cur.close()
    conn.commit()
    conn.close()
    return

def get_N_SentencefromAll(N):

    for i in range(0,N):
        sentence=getOneSentencefromAll()
        generate_sent_alldata(sentence)
    return







def get_declared_relation_count():
    all_Sent_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("SELECT id , sentence_id, sentence_text  FROM allRelations")
    results = cur.fetchall()
    count=0
    for row in results:
        id= row[0]
        sentenceid = row[1]
        sentencetext = row[2]


        if len(sentencetext)>50:
            if c_e_s('this method',str.lower(sentencetext)) or c_e_s('this function',str.lower(sentencetext)) or c_e_s('this function', str.lower(sentencetext)) or c_e_s('this implementation', str.lower(sentencetext)) or c_e_s('the method', str.lower(sentencetext)) or c_e_s('the function', str.lower(sentencetext)) or c_e_s('the class', str.lower(sentencetext)) or c_e_s('this class', str.lower(sentencetext)) :
                count=count+1

    print('the decrlation relation is : ')
    print(count)
    cur.close()
    conn.close()

    return




def get_unique_sentenceLinkapi():
    all_Sent_list = set()
    all_warning_list=set()
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("select DISTINCT uniquelink.relationid from uniquelink")
    results = cur.fetchall()
    count=0
    for row in results:
        sentenceid = row[0].rsplit('_', 1)[0]

        all_Sent_list.add(sentenceid)

    cur.execute("select DISTINCT WarningSentenceId from warning ")
    results = cur.fetchall()
    count = 0
    for row in results:
        sentenceid = row[0]

        all_warning_list.add(sentenceid)


    print('the  sentence link with API is : ')
    print(len(all_Sent_list & all_warning_list))
    cur.close()
    conn.close()

    return


get_unique_sentenceLinkapi()