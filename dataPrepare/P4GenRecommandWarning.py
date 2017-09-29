
# operate mysql database
import string

import pymysql


def insert_recommand_waring_data(schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='lhw', passwd='lhw', db='AndroidGuideAPI')
    cur = conn.cursor()

    cur.execute("delete from RecommandWarning")

    sqli = "insert into RecommandWarning values(%s,%s,%s)"

    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (i + 1, one_schema[0], one_schema[1]))
    cur.close()
    conn.commit()

    conn.close()
    return


# =====================

def get_all_entities_data():
    conn = pymysql.connect(host='localhost', port=3306, user='lhw', passwd='lhw', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = []

    try:
        cur.execute(
            "select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid from Entities")
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

            all_Entities_list.append((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_Entities_list


def get_all_warning_data():
    conn = pymysql.connect(host='localhost', port=3306, user='lhw', passwd='lhw', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_warning_list = []

    try:
        cur.execute(
            "select id, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentId from Warning")
        results = cur.fetchall()

        cur.close()

        for row in results:
            id = row[0]
            WarningTag = row[1]
            WarningSection = row[2]
            WarningText = row[3]
            WarningType = row[4]
            WarningURL = row[5]
            WarningSentId = row[6]


            all_warning_list.append((id, WarningTag, WarningSection, WarningText, WarningType, WarningURL, WarningSentId) )
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_warning_list


def get_all_relation_data():
    all_relation_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='lhw',passwd='lhw', db='AndroidGuideAPI')
    cur = conn.cursor()
    # try:
    cur.execute("select id, EntityOne, Relation, EntityTwo,  RelationSection, RelationURL, RelationText, URLid, Sentenceid, Relationid from EntitiesRelation")
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

        all_relation_list.append((index, EntityOne, Relation, EntityTwo, RelationSection, RelationURL, RelationText, URLid,  Sentenceid, Relationid))


# except:
#     print("Error: unable read data from table")

    cur.close()
    conn.close()

    return all_relation_list

    # =====================



# generate recommand warning list

def generate_recommand_data(all_Entities_list,all_warning_list,all_Relation_list):
    recommand_list=[]

    for relation in all_Relation_list:
        for warning in all_warning_list :
            sentid=relation[8]
            urlid=relation[7]
            wurlid=warning[6].split('_')[0]

            if (warning[6] == sentid) and (wurlid==urlid) :
                for entity in all_Entities_list:
                    eurlid=entity[7]
                    if (urlid==eurlid) and (wurlid==urlid) :
                        if c_e_s(entity[1].lower(),warning[3].lower()) and (c_e_s(entity[1].lower(),relation[1].lower()) or c_e_s(entity[1].lower(),relation[3].lower()) ) :
                            recommand_list.append((warning[0],entity[0]))

    recommand_list=list(set(recommand_list))


    return recommand_list


# compare_exact_string
def c_e_s(checkword, checkString):
    str1list = checkword.split()
    str2list = checkString.split()
    flag = True
    for word in str1list:
        if word not in str2list:
            flag = False
            break;
    return flag

# running
def main():
    all_Entities_list=get_all_entities_data()
    all_warning_list=get_all_warning_data()
    all_Relation_list=get_all_relation_data()

    recommand_list=generate_recommand_data(all_Entities_list,all_warning_list,all_Relation_list)

    insert_recommand_waring_data(recommand_list)
    return

main()