
# operate mysql database
import logging
import multiprocessing
import string

import os
import traceback

import pymysql
import re
from multiprocessing import Pool


def insert_recommand_waring_data(schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    cur.execute("delete from RecommandWarning")

    sqli = "insert into RecommandWarning values(%s,%s,%s,%s)"

    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (i + 1, one_schema[0], one_schema[1], one_schema[2]))
    cur.close()
    conn.commit()

    conn.close()
    return


# =====================

def get_all_entities_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = []

    try:
        cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities")
        results = cur.fetchall()

        cur.close()

        for row in results:
            id = row[0]
            EntityName = row[1]
            EntitySection = row[2]
            EntityURL = row[3]
            EntityParent = row[4]
            EntityType = row[5]
            EntityOriginal = row[6]
            URLid = row[7]
            QualifiedName=row[8]

            all_Entities_list.append((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_Entities_list


#get warning data
def get_all_warning_data():
    all_warning_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("select id, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid from Warning")
    results = cur.fetchall()

    cur.close()

    for row in results:
        id = row[0]
        WarningTag = row[1]
        WarningSection = row[2]
        WarningText = row[3]
        WarningType = row[4]
        WarningURL = row[5]
        WarningSentenceId = row[6]
        Relationid=row[7]

        all_warning_list.append((id, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid) )
    # except:
    #     print()
    #     print("Error: unable read data from table")

    conn.close()

    return all_warning_list

#get all relation data
def get_all_relation_data():
    all_relation_list = {}
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("select id, EntityOne, Relation, EntityTwo,  RelationSection, RelationURL, RelationText, URLid, Sentenceid, Relationid, POSinfo, SectionType from EntitiesRelation")
    results = cur.fetchall()

    # for row in results:
    #     index = row[0]
    #     EntityOne = row[1]
    #     Relation = row[2]
    #     EntityTwo = row[3]
    #     RelationSection = row[4]
    #     RelationURL = row[5]
    #     RelationText = row[6]
    #     URLid = row[7]
    #     Sentenceid = row[8]
    #     Relationid = row[9]
    #     POSinfo = row[10]
    #     SectionType = row[11]
    #
    #     all_relation_list.append((index, EntityOne, Relation, EntityTwo, RelationSection, RelationURL, RelationText, URLid,  Sentenceid, Relationid, POSinfo, SectionType))

    for row in results:
        all_relation_list[row[9]]=(row[0],row[1],row[2],row[3],row[9],row[7],row[5])


# except:
#     print("Error: unable read data from table")

    cur.close()
    conn.close()

    return all_relation_list

    # =====================







# compare_exact_string
def c_e_s(checkword, checkString, single):
    ablankre = re.compile(r'\s+')
    checkString=ablankre.sub(' ',checkString)
    if single is True:
        if '.' in checkword:
            checkword=checkword.replace('.',' ')
    checkword = ablankre.sub(' ', checkword)
    str1list = checkword.split(' ')
    str2list = checkString.split(' ')
    flag = True
    for word in str1list:
        if word not in str2list:
            flag = False
            break
    return flag



#get all doc dictionary
def get_all_doc():

    all_doc_dic={}
    data_path = os.pardir + '/tempdata'
    file_doc = open(data_path + '/AndroidAPI_Doc_out_ascii.txt')
    for one_doc in file_doc:
        doc_split=one_doc.split('\t')
        if len(doc_split) == 2:
            doc_id=doc_split[0]
            doc_content=doc_split[1]
            all_doc_dic[doc_id]=doc_content

    return all_doc_dic



# generate recommand warning list

def generate_recommand_data(i, all_Entities_list, warning_list, all_Relation_list, all_doc_dic,part_recommand_list):

    print("processing ...")
    print("Task :"+str(i)+"warning have :"+str(len(warning_list)))
    fulllen= len(warning_list) * len(all_Entities_list)

    count=1
    resultcount=0
    for warning in warning_list :
        wrelationid=warning[7]
        for entity in all_Entities_list:
            print("Task :"+str(i)+" Realtion No. :" + str(count) + " / " + str(fulllen))
            count = count + 1
            qualifiedname=''
            # check entity is the entityone or entitytwo in realtion
            entity_one = all_Relation_list[wrelationid][1]
            entity_two = all_Relation_list[wrelationid][3]
            if ((c_e_s(entity[1], entity_one, False)) or (c_e_s(entity[1], entity_two, False))):
                if entity[8] is not '':
                    qualifiedname = entity[8]
                elif entity[4] is not '':
                    qualifiedname = entity[4]
                else:
                    entitysection = entity[2]
                    if 'https://developer.android.com/' in entitysection:
                        entitysection = entitysection.split('https://developer.android.com/')[1]
                    if '.html' in entitysection:
                        entitysection = entitysection.split('.html')[0]
                    if '/' in entitysection:
                        entitysection = '.'.join(entitysection.split('/'))
                    qualifiedname = entitysection

                classname = qualifiedname
                if '.' in qualifiedname:
                    classname = qualifiedname.rsplit('.', 1)[1]

                relationURL = all_Relation_list[wrelationid][6]
                if 'https://developer.android.com/' in relationURL:
                    relationURL = relationURL.split('https://developer.android.com/')[1]

                if '.html' in relationURL:
                    relationURL = relationURL.split('.html')[0]

                relationURLkeywords = ' '.join(relationURL.split('/'))

                # check is the qualified name (entity[8]) in the warning text or in the webpage
                # and check the class name in this webpage

                warning_text = warning[3]
                doc_text = all_doc_dic[all_Relation_list[wrelationid][5]]

                if ((c_e_s(qualifiedname, warning_text, False)) or (c_e_s(qualifiedname, doc_text, False)) or (
                c_e_s(classname, relationURLkeywords, False)) and (c_e_s(classname, doc_text, True))):
                    part_recommand_list.append((warning[0], entity[0], all_Relation_list[wrelationid][0]))
                    resultcount = resultcount + 1
                    print("Task :"+str(i)+" Results. :" + str(resultcount))

    part_recommand_list = list(set(part_recommand_list))
    return part_recommand_list


# for multiprocess , it can chunk a list to many pices part with almost same size
def chunkListtoPices(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

# running
def main():
    all_Entities_list=get_all_entities_data()
    all_warning_list=get_all_warning_data()
    all_Relation_list=get_all_relation_data()
    all_doc_dic=get_all_doc()
    recommand_list=[]
    results=[]

    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        multiprocessing.freeze_support()
        cpus = multiprocessing.cpu_count()
        #cpus=3
        pool = multiprocessing.Pool()
        partition_warning = chunkListtoPices(all_warning_list, cpus)

        for i in range(0,cpus):
            result=pool.apply_async(generate_recommand_data, args=(i, all_Entities_list, partition_warning[i], all_Relation_list, all_doc_dic,recommand_list, ), callback=recommand_list.append )
            results.append(result)

        print('Waiting for all subprocesses done...')
        pool.close()
        pool.join()
        # print(recommand_list)

        insert_recommand_list=[]
        print('All subprocesses done.')


        for x in recommand_list:
            for y in x:
                insert_recommand_list.append(y)

        insert_recommand_list.sort(key=lambda tup: tup[1])

        # recommand_list=generate_recommand_data(all_Entities_list,all_warning_list,all_Relation_list)

        insert_recommand_waring_data(insert_recommand_list)
    return

main()