import os
import pymysql

# get the android api class full information into an array
def get_unique_api_class_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    unique_api_class_list = []

    try:
        cur.execute("select DISTINCT name, class_name, type,  doc_website from api_class order by name ")
        # select DISTINCT name, class_name, type,  doc_website from api_class order by name

        results = cur.fetchall()

        cur.close()
        index=0

        for row in results:
            name=row[0]
            class_name=row[1]
            type=row[2]
            doc_website=row[3]



            unique_api_class_list.insert(index , ( name, class_name, type,  doc_website))
            index=index+1

    except:
        print("Error: unable read data from table")

    conn.close()

    return unique_api_class_list

# get the android api class full information into an array
def get_api_class_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_class_list = []

    try:
        cur.execute("select api_class_id,  name, class_name, extend_class, type, package_id, doc_website from api_class order by api_class_id ")
        results = cur.fetchall()

        cur.close()

        for row in results:
            api_class_id=row[0]
            name=row[1]
            class_name=row[2]
            extend_class=row[3]
            type=row[4]
            package_id=row[5]
            doc_website=row[6]

            all_api_class_list.insert(api_class_id,( api_class_id,  name, class_name, extend_class, type, package_id, doc_website))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_class_list

# get the android api class full information into an dictionary
def get_api_class_dict():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_class_dict = {}

    try:
        cur.execute("select api_class_id,  name, class_name, extend_class, type, package_id, doc_website from api_class order by api_class_id ")
        results = cur.fetchall()

        cur.close()

        for row in results:
            api_class_id=row[0]
            name=row[1]
            class_name=row[2]
            extend_class=row[3]
            type=row[4]
            package_id=row[5]
            doc_website=row[6]

            all_api_class_dict[api_class_id]=( name, class_name, extend_class, type, package_id, doc_website)

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_class_dict


# get the android api libray full information into an array
def get_api_library_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_library_list = []

    try:
        cur.execute("select library_id, name, orgnization , doc_website from api_library order by library_id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            library_id=row[0];
            name=row[1];
            orgnization=row[2];
            doc_website=row[3];

            all_api_library_list.insert(library_id,(library_id, name, orgnization , doc_website))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_library_list



# get the android api method full information into an array
def get_api_method_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_method_list = []

    try:
        cur.execute("select  api_method_id, name, comment, annotation, return_class, return_string, class_id, is_static from api_method order by api_method_id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            api_method_id=row[0];
            name=row[1];
            comment=row[2];
            annotation=row[3];
            return_class=row[4];
            return_string=row[5];
            class_id=row[6];
            is_static=row[7]

            all_api_method_list.insert(api_method_id,(api_method_id, name, comment, annotation, return_class, return_string, class_id, is_static))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_method_list


# get the android api package full information into an array
def get_api_package_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_package_list = []

    try:
        cur.execute("select  api_package_id, name, doc_website, library_id from api_package order by api_package_id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            api_package_id=row[0];
            name=row[1];
            doc_website=row[2];
            library_id=row[3];

            all_api_package_list.insert(api_package_id,(api_package_id, name, doc_website, library_id))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_package_list


# get the android api package full information into an dictionary
def get_api_package_dict():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_package_dict = {}

    try:
        cur.execute("select  api_package_id, name, doc_website, library_id from api_package order by api_package_id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            api_package_id=row[0];
            name=row[1];
            doc_website=row[2];
            library_id=row[3];

            all_api_package_dict[api_package_id]=(name, doc_website, library_id)

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_package_dict


#get the method_id to fetch its parameters
def get_api_parameter_via_method_list(current_method_id):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    one_method_api_parameter_list = []

    try:
        cur.execute("select  parameter_id, name, class_id, method_id, type_class, type_string from api_parameter where method_id=%s order by parameter_id ",(current_method_id))

        results = cur.fetchall()

        cur.close()

        for row in results:
            parameter_id=row[0];
            name=row[1];
            class_id=row[2];
            method_id=row[3];
            type_class=row[4];
            type_string=row[5];


            one_method_api_parameter_list.insert(parameter_id,(parameter_id, name, class_id, method_id, type_class, type_string))

    except:
        print("Error: unable read data from table")

    conn.close()

    return one_method_api_parameter_list


# get the android api package full information into an array
def get_api_parameter_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_parameter_list = []

    try:
        cur.execute("select  parameter_id, name, class_id, method_id, type_class, type_string from api_parameter order by method_id, parameter_id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            parameter_id=row[0];
            name=row[1];
            class_id=row[2];
            method_id=row[3];
            type_class=row[4];
            type_string=row[5];


            all_api_parameter_list.insert(parameter_id,(parameter_id, name, class_id, method_id, type_class, type_string))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_parameter_list



# get the android api_package_list full information into an array
def get_api_package_list_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_package_list_list = []

    try:
        cur.execute("select  id, package_name, package_url from api_package_list order by id ")

        results = cur.fetchall()

        cur.close()

        for row in results:
            id=row[0];
            package_name=row[1];
            package_url=row[2];

            all_api_package_list_list.insert(id,(id, package_name, package_url))

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_package_list_list


#clean the entites table  !  caustion!!!
def clean_all_entites_table():
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute("delete from entities")
    cur.close()
    conn.commit()
    conn.close()

#insert entity information to database
def insert_entity_todatabase(entities_schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute("select * from entities")
    i=cur.rowcount

    sqlInsertStr = "insert into entities values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    for one_schema in entities_schema_list:
        cur.execute(sqlInsertStr, (i+1 , str(one_schema[0]).encode('utf-8'), str(one_schema[1]).encode('utf-8'), str(one_schema[2]).encode('utf-8'), str(one_schema[3]).encode('utf-8'), str(one_schema[4]).encode('utf-8'), str(one_schema[5]).encode('utf-8'), str(one_schema[6]).encode('utf-8'), str(one_schema[7]).encode('utf-8')))
        i=i+1

    cur.close()
    conn.commit()
    conn.close()

# get the filename URL and ID
def get_filenamelistWithID():
    file_path=os.getcwd()
    file_filelist= open(file_path + '/filenamelist_copy.csv')
    # file_path + '/filenamelist_copy.csv'
    # /Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata/filenamelist_copy.csv
    filename_list={}
    for filenameline in file_filelist:
        filenames=filenameline.split(',',1)
        if len(filenames)==2 :
            key,value=filenames[1].strip('\n'),filenames[0]
            filename_list[key]=value
    return filename_list


# begin get data to tables
def insert_entities_from_package_list():

    filenamelist=get_filenamelistWithID()

    package_entities_list=get_api_package_list_list()
    # id, package_name, package_url

    lenstr=str(len(package_entities_list))

    entities_list=[]
    # EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName

    i=0

    for oneLibrary in package_entities_list:
        EntityName=oneLibrary[1]
        EntitySection=""
        EntityURL=oneLibrary[2]
        EntityParent=""
        EntityType="Library"
        EntityOriginal=EntityName
        URLid=filenamelist.get(EntityURL)
        QualifiedName=EntityName

        entities_list.insert(oneLibrary[0],(EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName))
        i=i+1
        print("collecting: "+str(i) +" / "+lenstr)

    #write to database
    insert_entity_todatabase(entities_list)


def insert_entities_from_class_list():
    filenamedict = get_filenamelistWithID()


    unique_class_entities_list = get_unique_api_class_list()
    # name, class_name, type,  doc_website
    lenstr=str(len(unique_class_entities_list))


    entities_list = []
    # EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName


    index=0
    for oneClass in unique_class_entities_list:
        EntityName = oneClass[1]
        EntitySection = oneClass[3]
        EntityURL = oneClass[3]
        # remove class_name from name get package name
        parentName =oneClass[0]
        parentName=parentName[:parentName.rfind('.'+oneClass[1])]

        EntityParent = parentName
        EntityType = oneClass[2]
        EntityOriginal = oneClass[0]
        URLid = filenamedict.get(EntityURL)
        QualifiedName = oneClass[0]

        entities_list.insert(index,(EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
        index=index+1
        print("collecting: " + str(index) +" / "+lenstr)

        # ### debug statement ! caution!!
        # if len(entities_list)==100:
        #     break



    # write to database
    insert_entity_todatabase(entities_list)


#Find item in multidimensional list
# EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName
def find_item_inEntitieslist(itemNameKey, entitiesLists, itemQualifiedName):
    flag=False
    for index, sublist in enumerate(entitiesLists):
        if (sublist[0] == itemNameKey) and (sublist[7] == itemQualifiedName) :
            flag=True
            break

    return flag




#insert method entitie into database
def insert_entities_from_method_list():
    filenamedict = get_filenamelistWithID()

    classdict=get_api_class_dict()
    # api_class_id:  name, class_name, extend_class, type, package_id, doc_website

    methodList=get_api_method_list()
    # api_method_id, name, comment, annotation, return_class, return_string, class_id，
    lenstr= str(len(methodList))





    method_entities_list = set()
    # EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName

    i=0
    j=0

    for oneMethod in methodList:
        doc_website=classdict.get(oneMethod[6])[5]
        qualifiedname=classdict.get(oneMethod[6])[0]+'.'+oneMethod[1]
        method_id=oneMethod[0]

        j=j+1


        EntityName = oneMethod[1]
        EntitySection = doc_website+'#'+oneMethod[1]
        EntityURL = doc_website
        EntityParent = classdict.get(oneMethod[6])[0]
        EntityType = "Method"

        orginalStrings = "("
        qualifedStr = "("


        # paraStart=next(obj for obj in parameterList if obj[3]==method_id)

        myparametersList=get_api_parameter_via_method_list(method_id)
        # parameter_id, name, class_id, method_id, type_class, type_string


        if len(myparametersList)> 0 :


            for onePara in myparametersList :
                orginalStrings = orginalStrings + onePara[5] + ' ' + onePara[1] + ', '
                qualifedStr = qualifedStr + onePara[5] + ', '

            orginalStrings = orginalStrings[:orginalStrings.rfind(", ")] + ")"
            qualifedStr = qualifedStr[:qualifedStr.rfind(", ")] + ")"
        elif len(myparametersList)<1:
            orginalStrings =orginalStrings+ ")"
            qualifedStr =qualifedStr+ ")"




        EntityOriginal = oneMethod[1]+orginalStrings  #need update from parameter information (make up by checking table: Entities_copy)
        URLid = filenamedict.get(doc_website)
        QualifiedName = qualifiedname+qualifedStr


        # if (EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName) in method_entities_list  :
        #     continue

        # method_entities_list.insert(oneMethod[0],(EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))

        method_entities_list.add((EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))

        i=i+1
        print("searching:"+str(j)+" / "+lenstr+"collecting : "+str(i) )

        # ### debug statement ! caution!!
        # print(len(method_entities_list))
        # if len(method_entities_list)==10 :
        #     break

    # write to database
    #convert set to list

    insert_entity_todatabase(list(method_entities_list))



#insert parameters entities into database
def insert_entities_from_parameters_list():
    filenamedict = get_filenamelistWithID()

    classdict=get_api_class_dict()
    # api_class_id:  name, class_name, extend_class, type, package_id, doc_website

    methodList=get_api_method_list()
    # api_method_id, name, comment, annotation, return_class, return_string, class_id，

    parameterList=get_api_parameter_list()
    # parameter_id, name, class_id, method_id, type_class, type_string

    lenstr= str(len(parameterList))

    #construct two entities list from parameter table and method table
    parameter_entities_list=set()

    method_entities_list = []
    # EntityName,EntitySection,EntityURL,EntityParent,EntityType,EntityOriginal,URLid,QualifiedName

    i=0
    for onePara in parameterList:
        if (onePara[2] is  None) and (onePara[3] is  None):
            continue
        if onePara[2] is not None:
            class_id=onePara[2]
            typename="Field"
            sectionname=onePara[1]
            qualifiedname = classdict.get(class_id)[0] + '.'
            parentname= classdict.get(class_id)[0]


        if onePara[3] is not None:
            method_id=onePara[3]
            typename = "Parameter"
            sectionname=methodList[method_id][1]
            class_id=methodList[method_id][6]
            qualifiedname = classdict.get(class_id)[0] + '.'+methodList[method_id][1]
            parentname = qualifiedname

        doc_website = classdict.get(class_id)[5]
        qualifiedname = qualifiedname + '.'+onePara[1]



        EntityName = onePara[1]
        EntitySection = doc_website+'#'+sectionname
        EntityURL = doc_website
        EntityParent = parentname
        EntityType = typename
        EntityOriginal = onePara[5]+' '+onePara[1]
        URLid = filenamedict.get(doc_website)
        QualifiedName = qualifiedname

        # change to set for removing repeating tuples while adding
        # if (EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName) in parameter_entities_list :
        #     continue
        #
        # parameter_entities_list.insert(onePara[0],(EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))


        parameter_entities_list.add((EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
        i=i+1
        print("collecting : "+str(i)+" / "+lenstr)


        # #### debug statement ! caution!!
        # print(len(parameter_entities_list))
        # if len(parameter_entities_list)==100 :
        #     break

    # write to database
    # convert set to list
    insert_entity_todatabase(list(parameter_entities_list))


def main():
    clean_all_entites_table()
    # print("insert package entites")
    # insert_entities_from_package_list()
    # print("insert class entites")
    # insert_entities_from_class_list()
    print("insert method entites")
    insert_entities_from_method_list()
    print("insert parameter entites")
    insert_entities_from_parameters_list()


if __name__ == '__main__':
    main()