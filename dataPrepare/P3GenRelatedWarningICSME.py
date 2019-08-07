# operate mysql database
import os
import re

import pymysql


def delete_waring_alldata():

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:

        cur.execute("delete from Warning")
    except:

        print("Error: unable write data to table")

    cur.close()
    conn.commit()
    conn.close()
    return
    # =====================

def insert_waring_data(warning_list):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    try:

        sqli = "insert into Warning values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # id#, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId, Relationid

        for i, one_schema in enumerate(warning_list):
            cur.execute(sqli, (i + 1, one_schema[0], one_schema[1], one_schema[2], one_schema[3], one_schema[4], one_schema[5],one_schema[6]))
    except:

        print("Error: unable write data to table")

    cur.close()
    conn.commit()
    conn.close()
    return
    # =====================

def get_all_sentence_data():
    all_sentence_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    try:
        cur.execute("select id, sentenceID,sentenceText from allSentences")
        results = cur.fetchall()

        for row in results:
            index = row[0]
            sentenceID = row[1]
            sentenceText = row[2]

            all_sentence_list.append((index, sentenceID,sentenceText))
    except:
        print("Error: unable read data from table")

    cur.close()
    conn.close()

    return all_sentence_list

# =========
# searching warning pattern text in sentence
#
def searchingWarningPatterninSentence(keywords):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Sentences_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select id, sentenceId,sentenceText  from allSentences where sentenceText like %s ", ('%' + keywords + '%'))

        # cur.execute("select id, sentenceId,sentenceText  from allSentences where FIND_IN_SET(%s, sentenceText)!=0 or  sentenceText like %s", (keywords, '%' + keywords + '%'))
        results = cur.fetchall()

        cur.close()

        for row in results:
            id = row[0]
            sentenceId = row[1]
            sentenceText = row[2]

            all_Sentences_list.append((id, sentenceId,sentenceText))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_Sentences_list



# get the filename URL and ID
def get_filenamelistWithID():
    data_path = os.pardir + '/tempdata'
    file_filelist= open(data_path + '/filenamelist_copy.csv')
    # file_path + '/filenamelist_copy.csv'
    # /Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata/filenamelist_copy.csv
    filename_list={}
    for filenameline in file_filelist:
        filenames=filenameline.split(',',1)
        if len(filenames)==2 :
            key,value=filenames[0],filenames[1].strip('\n')
            filename_list[key]=value
    return filename_list

# get relation data

def get_all_relation_data():
    all_relation_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("select id, EntityOne, Relation, EntityTwo,  RelationSection, RelationURL, RelationText, URLid, Sentenceid, Relationid, POSinfo, SectionType from EntitiesRelation")
    results = cur.fetchall()

    for row in results:
        index = row[0]
        EntityOne = row[1]
        Relation = row[2]
        EntityTwo = row[3]
        RelationSection = row[4]
        RelationURL = row[5]
        RelationText = row[6]
        URLid = row[7]
        Sentenceid = row[8]
        Relationid = row[9]
        POSinfo=row[10]
        SectionType=row[11]

        all_relation_list.append((index, EntityOne, Relation, EntityTwo, RelationSection, RelationURL, RelationText, URLid,  Sentenceid, Relationid,POSinfo,SectionType))


# except:
#     print("Error: unable read data from table")

    cur.close()
    conn.close()

    return all_relation_list

    # =====================


# =====get relation ids
def get_all_relation_id_data(sentence_id):
    all_relation_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    rel_ids = ''
    try:
        cur.execute("select DISTINCT rel_id from allRelations where allRelations.sentence_id like %s",sentence_id)
        results = cur.fetchall()

        rel_ids=''

        for row in results:
            rel_ids=rel_ids+'\t'+str(row[0])

        rel_ids=rel_ids.lstrip('\t')

    except:
        print("Error: unable read data from table")

    cur.close()
    conn.close()


    return rel_ids
# =======


def generate_warning_data():
    # (warningtext, warningType, warningTag)
    # warning Type： Restricted ； Conditional；Explicit
    warning_define_list = [
        ('if ', 'Restricted', 'Condition'),
        ('when ', 'Restricted', 'Condition'),
        ('whether ', 'Restricted', 'Condition'),


        ('before ', 'Restricted', 'Temporal'),
        ('after ', 'Restricted', 'Temporal'),
        ('assume that ', 'Restricted', 'Temporal'),




        (' instead of ', 'Explicit', 'Alternative'),
        (' instead ', 'Explicit', 'Alternative'),
        (' rather than ', 'Explicit', 'Alternative'),
        (' otherwise ', 'Explicit', 'Alternative'),




        (' null ', 'Explicit', 'Error/Exception'),
        ('susceptible ', 'Explicit', 'Error/Exception'),
        ('non thread safe', 'Explicit', 'Error/Exception'),
        ('illegal ', 'Explicit', 'Error/Exception'),
        ('insecure ', 'Explicit', 'Error/Exception'),
        ('throw ', 'Explicit', 'Error/Exception'),
        ('throws ', 'Explicit', 'Error/Exception'),
        ('thrown ', 'Explicit', 'Error/Exception'),
        ('exception', 'Explicit', 'Error/Exception'),
        ('inappropriate ', 'Explicit', 'Error/Exception'),

        ('do not', 'Explicit', 'Imperative'),
        ('no event can be dispatched ', 'Explicit', 'Imperative'),
        ('dispatched ', 'Explicit', 'Imperative'),
        ('deprecated ', 'Explicit', 'Imperative'),
        ('deprecation ', 'Explicit', 'Imperative'),


        ('note', 'Explicit', 'Note'),
        ('note that', 'Explicit', 'Note'),
        ('notably', 'Explicit', 'Note'),
        ('caution', 'Explicit', 'Note'),
        ('see also', 'Explicit', 'Note'),

        ('deprecate ', 'Explicit', 'Recommendation'),
        ('better', 'Explicit', 'Recommendation'),
        ('best to', 'Explicit', 'Recommendation'),
        ('highly recommended', 'Explicit', 'Recommendation'),
        (' recommended ', 'Explicit', 'Recommendation'),
        ('less desirable ', 'Explicit', 'Recommendation'),
        (' might ', 'Explicit', 'Recommendation'),
        (' may ', 'Explicit', 'Recommendation'),
        ('discourage ', 'Explicit', 'Recommendation'),

        ('must', 'Generic', 'Affirmative'),
        ('should', 'Generic', 'Affirmative'),
        ('have to', 'Generic', 'Affirmative'),
        ('has to', 'Generic', 'Affirmative'),
        ('need to', 'Generic', 'Affirmative'),
        # need move Explicit Affirmative to Generic Affirmative

        (' warning', 'Generic', 'Affirmative'),
        (' can ', 'Generic', 'Affirmative'),
        ('can\'t ', 'Generic', 'Affirmative'),
        (' could ', 'Generic', 'Affirmative'),

        (' none ', 'Generic', 'Emphasis'),
        (' only ', 'Generic', 'Emphasis'),
        (' always ', 'Generic', 'Emphasis'),
        ('notification that', 'Generic', 'Emphasis'),
        ('will ', 'Generic', 'Emphasis'),


        (' always ', 'Generic', 'Negative'),
        (' not thread safe ', 'Generic', 'Negative'),
        (' not ', 'Generic', 'Negative'),
        (' do not ', 'Generic', 'Negative'),
        (' not secure ', 'Generic', 'Negative'),
        (' never ', 'Generic', 'Negative'),
        ('not guaranteed ', 'Generic', 'Negative')

        ]



    # ====
    #
    #
    # 发现一些新的syntactic patterns，可以考虑一下。
    #
    # 1，推荐句，比如you  are better[database:509] off[database:1]，
    # it is highly recommended[database:26]，
    # it is best to[database:21]
    #
    # 2，转折比较句，比如，
    # 。。。 otherwise[database:11311]。。。，
    #  。。。 instead of[database:1189] 。。。，
    #
    # 3，祈使句，
    # do not [database: 2162]  pass  [1129]。。。，
    # do not confuse[8]。。。,
    #  confuse[28]
    #
    # 4，explicit  terms，
    # not thread safe[database:15]，
    # not secure[7]，
    # not guaranteed[174]，
    # illegal[150]，
    # inappropriate[118]
    #
    # 5，注释，
    # notably[8]，
    # caution[28]
    # caution: [149]
    # caution![7]
    #
    # 6，不太清楚叫什么，暂定叫强调句，
    # 比如no event can be dispatched[98],
    # dispatched[333]，
    # only objects[16] running on the ui thread have access
    #
    #
    # otherwise，3，4，5，6）算成explicit， 1 2 这种都有点推荐  general


    # explicit term "deprecated / deprecation"
    #
    #
    # explicit recommend “discourage”

    #
    # explict error “insecure”

    #
    # general affirmative “have to” “has to”
    #
    # explicit recommend “less desirable”
    #
    # explicit error “susceptible”
    #
    # assume that;
    # before;
    # after 这类能不能算condition？


    # file_allsentence = open(data_path + '/androidAPIallSentICSME.txt', 'r')
    # dict_allsentence = {}
    # for line in file_allsentence:
    #     data = re.split(r'\t+', line.rstrip('\t').rstrip('\r').rstrip('\n'))
    #     if len(data) == 2:
    #         key, value = data[0], data[1]
    #         dict_allsentence[key] = value


    warningList = []
    # relation:  0index, 1EntityOne, 2Relation, 3EntityTwo, 4Section, 5URL, 6RelationText, 7URLid, 8Sentenceid, 9Relationid

    filenameDict=get_filenamelistWithID()

    # generate warning list
    collectingset = set()

    for warningword in warning_define_list:
        print(warningword)
        warningsentencelist=searchingWarningPatterninSentence(warningword[0])
        # 去除重复
        warningsentencelist=list(set(warningsentencelist))

        countj=0
        lengthwarningtype=len(warningsentencelist)
        for sentence in warningsentencelist:
            WarningTag=warningword[2]
            WarningSection=''
            WarningText=sentence[2]
            sentence_id=sentence[1]
            doc_id=sentence_id.split('_')[0]

            WarningType=warningword[1]
            WarningURL=filenameDict.get(doc_id)
            WarningSentenceId=sentence_id
            Relationids=get_all_relation_id_data(sentence_id).split('\t')
            print('warning:'+str(countj)+' / '+str(lengthwarningtype) )
            countj=countj+1



            #   id, ## WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId , Relationid
            for i in range(0,len(Relationids)):
                if i==0 and Relationids[i]=='':
                    break
                collectingset.add((WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentenceId , Relationids[i]))


    warningList=list(collectingset)
    print(len(warningList))
    return warningList


#compare_exact_string
def c_e_s(checkword, checkString):
    str1list=checkword.lower().split()
    str2list=checkString.lower().split()
    flag=True
    for word in str1list:
        if word not in str2list :
            flag=False
            break
    return flag


# running
def main():
    # all_relation_list=get_all_relation_data()


    warning_list=generate_warning_data()

    delete_waring_alldata()
    insert_waring_data(warning_list)
    return

main()