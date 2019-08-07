# coding:utf-8
## quick get entities from crawl data : androidAPI_id_tag_full_info_training
import urllib.parse
from functools import cmp_to_key


from selenium import webdriver
import pymysql
import pymysql.cursors
import re

def get_api_class_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_class_list = {}

    try:
        cur.execute("select distinct  name, class_name, doc_website from api_class order by class_name ")
        results = cur.fetchall()

        cur.close()

        for row in results:

            name=row[0] #qualified name
            class_name=row[1]
            doc_website=row[2]

            all_api_class_list[class_name]=(name,doc_website)

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_class_list


def get_api_method_list():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_api_method_list = {}

    try:
        cur.execute("select distinct  name, class_name, doc_website from api_method order by class_name ")
        results = cur.fetchall()

        cur.close()

        for row in results:

            name=row[0] #qualified name
            class_name=row[1]
            doc_website=row[2]

            all_api_method_list[class_name]=(name,doc_website)

    except:
        print("Error: unable read data from table")

    conn.close()

    return all_api_method_list

# operate mysql database
def generate_entity_todatabase(schema_list):

    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute("delete from entities")
    sqli = "insert into entities values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (i + 1, one_schema[0].encode('utf-8'), one_schema[1].encode('utf-8'), one_schema[2].encode('utf-8'), one_schema[3].encode('utf-8'), one_schema[4].encode('utf-8'), one_schema[5].encode('utf-8'), one_schema[6].encode('utf-8'), one_schema[7].encode('utf-8')))
    cur.close()
    conn.commit()
    conn.close()


# select the triple
def entity_selection():
    file_id_tag = open('/Users/Grand/Downloads/HDSKG/tempdata/androidAPI_id_tag_full_info_copy.csv')
    #the line of this file:
    # 4	,SIGTERM	,https://developer.android.com/reference/android/system/OsConstants.html	,https://developer.android.com/OsConstants.html#SIGTERM
    #5	,fragment_app_restriction_schema.xml	,https://developer.android.com/samples/AppRestrictionSchema/res/layout/fragment_app_restriction_schema.html	,h1



    file_filelist= open('/Users/Grand/Downloads/HDSKG/tempdata/filenamelist_copy.csv')


    filename_list={}
    for filenameline in file_filelist:
        filenames=filenameline.split(',',1)
        if len(filenames)==2 :
            key,value=filenames[1].strip('\n'),filenames[0]
            filename_list[key]=value





    phrase_list = []
    section_list = []
    url_list = []
    p_uid_list = []
    dict_pair={}
    headerlist=['h1','h2','h3','h4','h5','h6']

    schema_list = []

    all_api_class_dict=get_api_class_list()

    for one_id_tag_line in file_id_tag:
        # print(one_id_tag_line)
        phrase_u_id = one_id_tag_line.split('\t,')[0]
        pure_phrase = one_id_tag_line.split('\t,')[1]
        pure_url=one_id_tag_line.split('\t,')[2]
        #pure_url = urllib.parse.unquote(pure_url).decode('utf8')
        groups=one_id_tag_line.split('\t,')
        pure_section=(''.join(groups[3:])).strip('\n')
        #pure_section = urllib.parse.unquote(pure_section).decode('utf8')

        if pure_phrase.isdigit() :
            continue
        breakphrase=pure_phrase.split(' ')
        if len(breakphrase)>1 :
            continue

        #checking, if it has collected in the list
        # choice the first one
        flagfornewitem=True
        for item in schema_list:
            if pure_phrase in item[0] :
                if pure_section.lower() in headerlist:
                    temp_pure_section = pure_url + '#' + pure_phrase
                    if temp_pure_section in item[1]:
                        flagfornewitem = False
                        break
                elif pure_section in item[1] :
                    flagfornewitem=False
                    break

        # there is the same phrase , then find next
        if flagfornewitem is False:
            continue






        pure_parent=''
        pure_type=''
        pure_original=''
        classname=''
        qualifiedname = ''

        #the first step , just get the entities from  the reference
        #next steps , it can add more from guide/topic/example/training ....
        #generate phrase type information



        if "http" not in pure_section:
            #h1 h2 ...
            if ("https://developer.android.com/reference" in pure_url):
                pure_type = pure_section
                pure_section=pure_url+'#'+pure_phrase
                phrase_list.append(pure_phrase)
                section_list.append(pure_section)
                url_list.append(pure_url)
                p_uid_list.append(phrase_u_id)
                page_position = ''
                page_url = ''

                pure_parent=''
                pure_original = pure_phrase
                # get the type of entity(class, method , filed ),  entity parent

                print(phrase_u_id)

                schema_list.append((pure_phrase, pure_section.strip('\n'), pure_url.strip('\n'), pure_parent, pure_type,pure_original, filename_list[pure_url.strip('\n')], qualifiedname))


        elif ("https://developer.android.com/reference" in pure_section):
            #Class  method field ==》qualified name
            if pure_section not in section_list:
                phrase_list.append(pure_phrase)
                section_list.append(pure_section)
                url_list.append(pure_url)
                p_uid_list.append(phrase_u_id)
                page_position=''
                page_url=''
                #get the type of entity(class, method , filed ),  entity parent
                if '#' in pure_section:

                    pageinfo=pure_section.split('#')
                    page_url=pageinfo[0]
                    classname=page_url.rsplit('/',1)[1]
                    if '.' in classname:
                        classname=classname.rsplit('.',1)[0]

                    pure_parent=classname

                    page_position=pageinfo[1]
                    pure_original=page_position
                    if '(' in page_position:
                        pure_type='Method'
                    else:
                        pure_type='Field'
                else:
                    classname = pure_section.rsplit('/', 1)[1]
                    if '.' in classname:
                        classname = classname.rsplit('.',1)[0]
                    pure_original=classname
                    pure_type='Class'

                #find qualified name from api_class
                qualifiedname = ''

                if pure_type is 'Class':
                    if pure_phrase in all_api_class_dict:
                        pure_section_url=pure_section
                        if pure_section_url in all_api_class_dict[pure_phrase][1]:
                            qualifiedname=all_api_class_dict[pure_phrase][0]

                if pure_type is 'Method':
                    if pure_parent in all_api_class_dict:
                        pure_section_url=pure_section.rsplit('#',1)[0]
                        if pure_section_url in all_api_class_dict[pure_parent][1]:
                            qualifiedname=all_api_class_dict[pure_parent][0]

                if pure_type is 'Field':
                    if pure_parent in all_api_class_dict:
                        pure_section_url=pure_section.rsplit('#',1)[0]
                        if pure_section_url in all_api_class_dict[pure_parent][1]:
                            qualifiedname=all_api_class_dict[pure_parent][0]



                print(phrase_u_id)

                schema_list.append((pure_phrase,pure_section.strip('\n'),pure_url.strip('\n'),pure_parent,pure_type,pure_original,filename_list[pure_url.strip('\n')],qualifiedname))

    file_id_tag.close()
#    print(schema_list)

    schema_list.sort(key=lambda tup: tup[1])
    print(len(schema_list))
    return schema_list


# compare_exact_string
def check_string_in_list(checkword, checkString):
    ablankre = re.compile(r'\s+')
    checkString=ablankre.sub(' ',checkString)
    checkword = ablankre.sub(' ', checkword)
    str1list = checkword.split()
    str2list = checkString.split()
    flag = True
    for word in str1list:
        if word not in str2list:
            flag = False
            break
    return flag




#running
def main():
    schema_list= entity_selection()
    generate_entity_todatabase(schema_list)

main()