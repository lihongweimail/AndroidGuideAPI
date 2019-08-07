

# {'subject_ori': 'corporate environments', 'relation_ori': 'restrict', 'object_ori': 'device features', 'subject': 'corporate_environments', 'relation': 'restrict', 'object': 'device_features', 'subject_stand': 'corporate environment', 'relation_stand': 'restrict', 'object_stand': 'device feature', 'start_index': 11, 'end_index': 16, 'originalSent_len': 20, 'pos': 'JJ NNS VBP NN NNS', 'relationType': 'NonTaxo', 'rel_id': '11352_27_1'}
import ast
import os
import re

import pymysql


def insert_relation_data(sentence_list):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:
        cur.execute("delete from allRelations")

        sqli = "insert into allRelations values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # id#, subject_ori, relation_ori , object_ori, subject, relation, object, subject_stand, relation_stand, object_stand, start_index, end_index, originalSent_len , pos, relationType, rel_id

        for i, one_schema in enumerate(sentence_list):

            cur.execute(sqli, (i + 1, one_schema[0], one_schema[1], one_schema[2], one_schema[3], one_schema[4], one_schema[5], one_schema[6], one_schema[7], one_schema[8], one_schema[9], one_schema[10], one_schema[11], one_schema[12], one_schema[13], one_schema[14],one_schema[15],one_schema[16]))

    except:

        print("Error: unable write data to table")

    cur.close()
    conn.commit()
    conn.close()
    return
    # =====================


def get_all_sentence_data():
    all_sentence_dict = {}
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    try:
        cur.execute("select id, sentenceID,sentenceText from allSentences")
        results = cur.fetchall()

        for row in results:
            index = row[0]
            sentenceID = row[1]
            sentenceText = row[2]

            all_sentence_dict[sentenceID]=sentenceText
    except:
        print("Error: unable read data from table")

    cur.close()
    conn.close()

    return all_sentence_dict



def generateRelationTableData():
    data_path = os.pardir + '/tempdata'
    file_allsentence = open(data_path + '/androidAPIallCand5ICSME.txt', 'r')

    relation_list=[]
    # subject_ori, relation_ori , object_ori, subject, relation, object, subject_stand, relation_stand, object_stand, start_index, end_index, originalSent_len , pos, relationType, rel_id

    sentence_dict=get_all_sentence_data()

    for j, one_triple in enumerate(file_allsentence):
        one_triple=str(one_triple)

        if type(one_triple) is str or type(one_triple) is bytes:
            #Python 3 renamed the unicode type to str, the old str type has been replaced by bytes
            one_triple = eval(one_triple.strip('\n'))
        else :
            continue

        subject_ori=one_triple['subject_ori']
        relation_ori=one_triple['relation_ori']
        object_ori=one_triple['object_ori']
        subject=one_triple['subject']
        relation=one_triple['relation']
        object=one_triple['object']
        subject_stand=one_triple['subject_stand']
        relation_stand=one_triple['relation_stand']
        object_stand=one_triple['object_stand']
        start_index=one_triple['start_index']
        end_index=one_triple['end_index']
        originalSent_len=one_triple['originalSent_len']
        pos=one_triple['pos']
        relationType=one_triple['relationType']
        rel_id=one_triple['rel_id']
        sentence_id=rel_id.rsplit('_',1)[0]
        sentence_text=sentence_dict.get(sentence_id)
        if sentence_text is None:
            continue
        if len(sentence_text)>3000:
            continue
        if len(subject_ori)>1000 or len(relation_ori)>1000 or len(object_ori)>1000 or len(subject)>1000 or len(relation)>1000 or len(object)>1000 or len(subject_stand)>1000 or len(relation_stand)>1000 or len(object_stand)>1000 or len(pos)>1000 or len(relationType)>1000:
            continue
        relation_list.append((subject_ori, relation_ori , object_ori, subject, relation, object, subject_stand, relation_stand, object_stand, start_index, end_index, originalSent_len , pos, relationType, rel_id,sentence_id,sentence_text))

    file_allsentence.close()
    insert_relation_data(relation_list)


generateRelationTableData()
