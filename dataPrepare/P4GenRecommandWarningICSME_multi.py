
import os
# from selenium import webdriver
import pymysql
import pymysql.cursors


# === get link Entities table data ==================

def get_all_linkentitysnew_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_linkEntities_list = []

    try:
        cur.execute("select id, entityid,relationid from linkEntitysNew")
        results = cur.fetchall()

        cur.close()

        for row in results:
            id = row[0]
            entityid = row[1]
            relationid = row[2]


            all_linkEntities_list.append((id, entityid,relationid))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_linkEntities_list


# === get warning table data ==================

def get_all_warning_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_warning_list = []

    try:
        cur.execute("select id,relationid from Warning")
        results = cur.fetchall()

        cur.close()

        for row in results:
            id = row[0]
            relationid = row[1]


            all_warning_list.append((id,relationid))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_warning_list

# === searching in Warning table data ==================

def searching_in_Warning_data(relationid):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Warningid_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select  id from Warning where Relationid=%s",relationid)

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where %s like '%'"+"EntityName"+"'%' ",(keywords))

        results = cur.fetchall()

        cur.close()

        for row in results:

            id = row[0]
            all_Warningid_list.append(id)
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_Warningid_list

# === searching in Warning table data ==================

def searching_in_EntitiesRelation_data(relationid):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_ERid_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select  id from EntitiesRelation where Relationid=%s",relationid)

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where %s like '%'"+"EntityName"+"'%' ",(keywords))

        results = cur.fetchall()

        cur.close()

        for row in results:

            id = row[0]
            all_ERid_list.append(id)
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_ERid_list


def searching_in_linkentitysnew_data(relationid):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_linkentitys_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select  id, entityid, relationid from linkEntitysNew where relationid=%s", relationid)

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where %s like '%'"+"EntityName"+"'%' ",(keywords))

        results = cur.fetchall()

        cur.close()

        for row in results:

            id = row[0]
            entityid=row[1]
            relationid=row[2]
            all_linkentitys_list.append((id, entityid, relationid))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_linkentitys_list

# ============
def insert_generate_data(schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    lastid=0

    cur.execute('SELECT id FROM RecommandWarning ORDER BY id DESC LIMIT 1')
    results = cur.fetchall()
    for row in results:
        lastid = row[0]


    sqli = "insert into RecommandWarning values(%s,%s,%s,%s)"
    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (lastid+i + 1, one_schema[0], one_schema[1], one_schema[2]))
    cur.close()
    conn.commit()
    conn.close()
    return



# operate mysql database
def generate_data(schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute("delete from RecommandWarningx")

    sqli = "insert into RecommandWarningx values(%s,%s,%s,%s)"
    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (i + 1, one_schema[0], one_schema[1], one_schema[2]))
    cur.close()
    conn.commit()
    conn.close()
    return



# === start programer ====

def generate_recommand_data(i,all_warning,all_data):
    schemalist = []
    all_data = []

    print("processing ...")
    print("Task :" + str(i) + "warning have :" + str(len(all_warning)))

    j=0
    for onewarning in all_warning:
        print("checking >> "+str(j))
        j=j+1
        warningid = onewarning[0]
        relationid = onewarning[1]
        linklist = searching_in_linkentitysnew_data(relationid)
        ERlist = searching_in_EntitiesRelation_data(relationid)
        print(linklist)
        print(ERlist)
        print("==============")
        if len(linklist)==0 or len(ERlist)==0:
            continue
        for onelinklist in linklist:
            for oneERlist in ERlist:
                schemalist.append((warningid, onelinklist[1], oneERlist))
                all_data.append((warningid, onelinklist[1], oneERlist))

        insert_generate_data(schemalist)
        schemalist = []
    all_data = list(set(all_data))
    return all_data



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
    schemalist = []
    all_data = []
    all_warning = get_all_warning_data()
    print("total: " + str(len(all_warning)))
    j = 0
    recommand_list=[]
    results=[]

    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        multiprocessing.freeze_support()
        cpus = multiprocessing.cpu_count()
        #cpus=3
        pool = multiprocessing.Pool()
        partition_warning = chunkListtoPices(all_warning, cpus)

        for i in range(0,cpus):
            result=pool.apply_async(generate_recommand_data, args=(i,  partition_warning[i],recommand_list, ), callback=recommand_list.append )
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

        generate_data(insert_recommand_list)
    return

main()
