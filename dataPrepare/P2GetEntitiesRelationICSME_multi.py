# coding:utf-8
import multiprocessing
from functools import cmp_to_key

import os
# from selenium import webdriver
import pymysql
import pymysql.cursors
import re

# extract data using webdriver
# def start():
#     executable_path = '/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs'  # phantomjs engine, used as browser
#     # /usr/local/Cellar/phantomjs/2.1.1
#     driver = webdriver.PhantomJS(executable_path=executable_path)
#     # driver = webdriver.Firefox()   # can use firefox or other brower as well
#     extract_ele(driver)
#     return

# extract by xpath
def extract_ele(driver):
    data_path = os.pardir + '/tempdata'
    file_keyPhrase = open(data_path+'/all_rel_section_out_ICSME.txt', 'w')
    file_filenamelist = open(data_path+'/filenamelist_copy.csv')



    for one_line in file_filenamelist:
        one_line=one_line.rstrip('\n').rstrip('\r')
        # all_url.remove('')



        urlsplit=one_line.split(',')
        url_id = urlsplit[0]
        print("processing file :"+one_line)
        # goal_website = (one_url.split('/guideAPI/')[1]).strip('\n')
        goal_website = (''.join(urlsplit[1:])).strip('\n')
        # goal_website = 'developer.android.com/training/accessibility/accessible-app.html'
        # driver.get('https://' + goal_website)
        driver.get( goal_website)

        basic_xpath = '//*[@id="body-content"]/div[2]'
        basic_headerpath = '//*[@id="body-content"]/div[1]'


        findtext = driver.find_elements_by_xpath('//*[@id="body-content"]/div[1]')
        if findtext is not None:
            basic_xpath = '//*[@id="body-content"]/div[2]'
            basic_headerpath = '//*[@id="body-content"]/div[1]'
        else :
            findtext = driver.find_elements_by_xpath('//*[@itemprop="articleBody"]/div[1]')
            if findtext is not None:
                basic_xpath = '//*[@itemprop="articleBody"]/div[2]'
                basic_headerpath = '//*[@itemprop="articleBody"]/div[1]'
            else:
                findtext = driver.find_elements_by_xpath('//*[@class="gc-documentation"]/div[1]')
                if findtext is not None:
                    basic_xpath = '//*[@class="gc-documentation"]/div[2]'
                    basic_headerpath = '//*[@class="gc-documentation"]/div[1]'
                else:
                    continue


        header_list = []
        api_list = []
        header_h1 = driver.find_elements_by_xpath(basic_headerpath+'/h1')
        if header_h1 != [] and header_h1[0].text != '':
            header_list.append((header_h1[0].text, 0, 'h1'))
            # (header's name, its sequence mark, type)
            # sequence mark is for confirming api belongs to which section
        else:
            header_list.append(('unknow header1', 0, 'h1'))
            # some webs do not have h1 or the xpath is wrong

        # count the total num of p, h2, h3 for loop later
        para_last_sibling = driver.find_elements_by_xpath(basic_xpath + '/p[last()]/preceding-sibling::p | ' +basic_xpath + '/p[last()]')

        para_total_count = len(para_last_sibling)

        h2_last_sibling = driver.find_elements_by_xpath(basic_xpath + '/h2[last()]/preceding-sibling::h2 | ' +basic_xpath + '/h2[last()]')

        h2_total_count = len(h2_last_sibling)

        h3_last_sibling = driver.find_elements_by_xpath(basic_xpath + '/h3[last()]/preceding-sibling::h3 | ' +basic_xpath + '/h3[last()]')

        h3_total_count = len(h3_last_sibling)

        print("paras:"+para_total_count, "h2 count:"+h2_total_count,"h3 count:"+ h3_total_count)

        for i in range(1, para_total_count + 1):
            api_code = driver.find_elements_by_xpath(basic_xpath + '/p[' + str(i) + ']//code')
            for one_api in api_code:
                if one_api.text != '':
                    api_list.append((one_api.text, i - 1))          # i - 1 is sequence mark

        for i in range(1, h2_total_count + 1):
            header_h2 = driver.find_element_by_xpath(basic_xpath + '/h2[position() = ' + str(i) + ']')
            if header_h2.text != '':
                sibling_h2 = driver.find_elements_by_xpath(basic_xpath + '/h2[position() = '
                                                           + str(i) + ']/preceding-sibling::p')
                position_h2 = len(sibling_h2)           # this is how sequence mark comes from,
                # use num of preceding-sibling p tags
                header_list.append((header_h2.text, position_h2, 'h2'))

        for i in range(1, h3_total_count + 1):
            header_h3 = driver.find_element_by_xpath(basic_xpath + '/h3[position() = ' + str(i) + ']')
            if header_h3.text != '':
                sibling_h3 = driver.find_elements_by_xpath(basic_xpath + '/h3[position() = '
                                                           + str(i) + ']/preceding-sibling::p')
                position_h3 = len(sibling_h3)
                header_list.append((header_h3.text, position_h3, 'h3'))

        #python 3  there no "cmp" parameter for sort
        header_list.sort(key=takeListSecond)

        print(len(header_list))
        print(len(api_list))
        for one_api in api_list:
            file_keyPhrase.write(url_id + ', ')
            file_keyPhrase.write(one_api[0] + ', ')
            write_flag = 0
            for i, one_header in enumerate(header_list):
                # find api's section based on sequence mark
                if one_api[1] < one_header[1]:
                    file_keyPhrase.write(header_list[i - 1][0] + ', ')
                    write_flag = 1
                    break
            if not write_flag:
                file_keyPhrase.write(header_list[-1][0] + ', ')
            file_keyPhrase.write(goal_website + '\n')

            # break

    file_keyPhrase.close()
    file_filenamelist.close()
    return



def takeListSecond(elem):
    return elem[1]


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





# === get Entities table data ==================

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

# === searching in Entities table data ==================

# def searching_in_entities_data(keywords,urlid):
def searching_in_entities_data(keywords1, keywords2):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    collectsetitmes = set()

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select DISTINCT  id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where FIND_IN_SET(EntityName,%s)!=0 or FIND_IN_SET(EntityName,%s)!=0  ",(keywords1, keywords2))

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where %s like '%'"+"EntityName"+"'%' ",(keywords))

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

            collectsetitmes.add((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return collectsetitmes

# find the just current name from qualified name
def getKeywordsonly(keywords):
    if '(' in keywords:
        keywords = keywords.rsplit('(')[0]

    if '[' in keywords:
        keywords = keywords.rsplit('[')[0]

    if '.' in keywords:
        keywords = keywords.rsplit('.', 1)[1]

    return keywords


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


# select the triple
def triple_selection():
    data_path = os.pardir + '/tempdata'

    # get relation from Cand_file  with POS
    file_triple = open(data_path+'/androidAPIallCand5ICSME.txt','r')

    filetriplelist=[]
    # # get entities from Entities table
    # all_Entities = get_all_entities_data()
    for line in enumerate(file_triple):
        filetriplelist.append(line)

    file_triple.close()


    file_allsentence = open(data_path+'/androidAPIallSentICSME.txt','r')

    filenameDict=get_filenamelistWithID()

    #allSent example:  "id \t text"
    #11352_27	Go further to support business use of your app by enabling restrictions that administrators can use to remotely configure your app: Manage Devices and Apps.


    dict_allsentence={}
    for line in file_allsentence:
        data=re.split(r'\t+', line.rstrip('\t').rstrip('\r').rstrip('\n'))
        if len(data)==2:
            key,value=data[0],data[1]
            dict_allsentence[key]=value


    schema_list = []
    collectingentityid=set()
    entitidstringlist = ''

    results=[]

    print('Parent Process %s.'% os.getpid())
    multiprocessing.freeze_support()
    cpus = multiprocessing.cpu_count()
    # cpus=3
    pool = multiprocessing.Pool()
    partition = chunkListtoPices(filetriplelist, cpus)

    for i in range(0, cpus):
        result = pool.apply_async(multiSelect, args=(
            collectingentityid, dict_allsentence, partition[i], filenameDict,
            schema_list,),callback=schema_list.append)
        results.append(result)

    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()

    insert_recommand_list = []
    print('All subprocesses done.')

    for x in schema_list:
        for y in x:
            insert_recommand_list.append(y)

    # insert_recommand_list.sort(key=lambda tup: tup[1])




    # print(schema_list)
    # remove duplicates
    schema_list=list(set(insert_recommand_list))

    print(len(schema_list))
    return schema_list

# =====
# for multiprocess , it can chunk a list to many pices part with almost same size
def chunkListtoPices(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def multiSelect(collectingentityid, dict_allsentence, file_triple, filenameDict, schema_list):

    for j, one_triple in enumerate(file_triple):

        if type(one_triple) is str or type(one_triple) is bytes:
            # Python 3 renamed the unicode type to str, the old str type has been replaced by bytes
            one_triple = eval(one_triple.strip('\n'))
        else:
            continue

        # all triple example:
        # {'subject_ori': 'The DownloadManager.Query class', 'relation_ori': 'provides', 'object_ori': 'methods', 'subject': 'DownloadManager.Query_class', 'relation': 'provides', 'object': 'methods', 'subject_stand': 'downloadmanager.query class', 'relation_stand': 'provide', 'object_stand': 'method', 'start_index': 1, 'end_index': 5, 'originalSent_len': 16, 'pos': 'NNP NN VBZ NNS', 'relationType': 'NonTaxo', 'rel_id': '21_78_1'}

        entity1 = one_triple['subject_ori']
        relation = one_triple['relation_ori']
        entity2 = one_triple['object_ori']

        relation_url_id = one_triple['rel_id'].split('_')[0]

        sentence_id = one_triple['rel_id'].rsplit('_', 1)[0]
        sentence_text = dict_allsentence[sentence_id]

        relation_id = one_triple['rel_id']

        EntityOne = entity1
        Relation = relation
        EntityTwo = entity2
        RelationSection = ''
        RelationURL = filenameDict.get(relation_url_id)
        RelationText = sentence_text
        URLid = relation_url_id
        Sentenceid = sentence_id
        Relationid = relation_id
        POSinfo = one_triple['pos']
        SectionType = ''

        print(j, entity1, relation, entity2)

        entitylist = []

        searchingEntity1 = entity1.replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').replace('<',
                                                                                                                   ' ').replace(
            '>', ' ').replace('.', ' ').replace(' ', ',')

        searchingEntity2 = entity2.replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').replace('<',
                                                                                                                   ' ').replace(
            '>', ' ').replace('.', ' ').replace(' ', ',')

        entitylist = list(searching_in_entities_data(searchingEntity1, searchingEntity2))

        # collect id already fetch from entities table
        for enid in range(0, len(entitylist)):
            collectingentityid.add(str(entitylist[enid][0]))

        entitidstringlist = ''
        for ids in collectingentityid:
            entitidstringlist = entitidstringlist + ids + ','

        entitidstringlist = entitidstringlist.strip(',')

        collectingset = set()
        # listtest = []

        if len(entitylist) > 0:
            for entity1i in range(0, len(entitylist)):

                if URLid == entitylist[entity1i][7]:
                    RelationSection = entitylist[entity1i][2]
                    SectionType = entitylist[entity1i][5]
                else:
                    RelationSection = ''
                    SectionType = ''
                # id , ##,EntityOne ,Relation , EntityTwo, RelationSection, RelationURL, RelationText, URLid, Sentenceid, Relationid, POSinfo, SectionType
                collectingset.add((EntityOne, Relation, EntityTwo, RelationSection, RelationURL, RelationText, URLid,Sentenceid, Relationid, POSinfo, SectionType))

            print(" Yes , collected")
        else:
            print(" ==>not collecting item")
            continue

        # convert set to list
        collectinglist = list(collectingset)

        if len(collectinglist) > 0:
            for collectingi in range(0, len(collectinglist)):
                # add it  as a relation
                schema_list.append(collectinglist[collectingi])
            # remove duplicates
            schema_list = list(set(schema_list))
    return schema_list


# operate mysql database
def generate_data(schema_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
    cur.execute("delete from EntitiesRelation")
    # schema_list = triple_selection()
    sqli = "insert into EntitiesRelation values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for i, one_schema in enumerate(schema_list):
        cur.execute(sqli, (i + 1, one_schema[0], one_schema[1], one_schema[2], one_schema[3], one_schema[4], one_schema[5], one_schema[6], one_schema[7], one_schema[8]))
    cur.close()
    conn.commit()
    conn.close()
    return






# === start programer ====

def main():


    # prepare entities_relation data
    schema_list=triple_selection()

    #triple_selection()
    generate_data(schema_list)


if __name__ == '__main__':
    main()