# # # # # import threading
# # # # # import time
# # # # # def haha(max_num):
# # # # #     for i in range(max_num):
# # # # #         time.sleep(1)
# # # # #         print(i)
# # # # #
# # # # #     recommand_list = []
# # # # #     print("processing ...")
# # # # #     fulllen = len(all_warning_list) * len(all_Entities_list)
# # # # #
# # # # #     count = 1
# # # # #     for warning in all_warning_list:
# # # # #
# # # # #         wrelationid = warning[7]
# # # # #
# # # # #         for entity in all_Entities_list:
# # # # #             print("realtion No. :" + str(count) + " / " + str(fulllen))
# # # # #             count = count + 1
# # # # #
# # # # #             if c_e_s(entity[1].lower(), warning[3].lower()) and (c_e_s(entity[1].lower(), all_Relation_list[wrelationid][1].lower()) or c_e_s(entity[1].lower(),all_Relation_list[wrelationid][3].lower())):
# # # # #                 recommand_list.append((warning[0], entity[0], all_Relation_list[wrelationid][0]))
# # # # #
# # # # #     recommand_list = list(set(recommand_list))
# # # # # """
# # # # # 创建一个列表，用于存储要启动多线程的实例
# # # # # """
# # # # # threads=[]
# # # # # for x in range(3):
# # # # #     t=threading.Thread(target=haha,args=(5,))
# # # # #     #把多线程的实例追加入列表，要启动几个线程就追加几个实例
# # # # #     threads.append(t)
# # # # # for thr in threads:
# # # # #     #把列表中的实例遍历出来后，调用start()方法以线程启动运行
# # # # #     thr.start()
# # # # # for thr in threads:
# # # # #     """
# # # # #     isAlive()方法可以返回True或False，用来判断是否还有没有运行结束
# # # # #     的线程。如果有的话就让主线程等待线程结束之后最后再结束。
# # # # #     """
# # # # #     if thr.isAlive():
# # # # #         thr.join()
# # # # #
# # # # #
# # # # import multiprocessing
# # # # from multiprocessing import Pool
# # # # import os, time, random
# # # #
# # # # from numpy import iterable
# # # #
# # # #
# # # # def long_time_task(name,p,list):
# # # #     print('Run task %s (%s)...' % (name, os.getpid()))
# # # #     start = time.time()
# # # #     time.sleep(random.random() * 3)
# # # #     end = time.time()
# # # #     mystring='Task %s runs %0.2f seconds.' % (name, (end - start))
# # # #     print(mystring)
# # # #     for x in p:
# # # #         list.append(str(x)+"task%s" % (name))
# # # #
# # # #     return list
# # # #
# # # #
# # # #
# # # # if __name__=='__main__':
# # # #     print('Parent process %s.' % os.getpid())
# # # #     multiprocessing.freeze_support()
# # # #     cpus = multiprocessing.cpu_count()
# # # #     pool=multiprocessing.Pool()
# # # #     # p = Pool(4)
# # # #     p=((11,12,13,14,15,16),(21,22,23,24,25,26), (31, 32, 33, 34, 35, 36),(41, 42, 43, 44, 45, 56))
# # # #     list = []
# # # #     results=[]
# # # #     for i in range(0,cpus):
# # # #         result=pool.apply_async(long_time_task, args=(i,p[i],list,),callback=list.append)
# # # #         results.append(result)
# # # #     print('Waiting for all subprocesses done...')
# # # #     pool.close()
# # # #     pool.join()
# # # #
# # # #     for x in list:
# # # #         for y in x:
# # # #             print(y)
# # # #
# # # #     print(cpus)
# # # #     for result in results:
# # # #         print(result)
# # # #
# # # #     print('All subprocesses done.')
# # # #
# # # #
# # # # #
# # # # # def chunkIt(seq, num):
# # # # #     avg = len(seq) / float(num)
# # # # #     out = []
# # # # #     last = 0.0
# # # # #
# # # # #     while last < len(seq):
# # # # #         out.append(seq[int(last):int(last + avg)])
# # # # #         last += avg
# # # # #
# # # # #     return out
# # # # #
# # # # #
# # # # # mylist=((1,2,3,4,5),(11,22,33,44,55),(31,32,33,34,35))
# # # # #
# # # # # my=chunkIt(mylist,3)
# # # # # print(len(my))
# # # # # pt=my[2]
# # # # # for x in pt:
# # # # #     print(x)
# # # #
# # # # # def task(pid):
# # # # #     # do something
# # # # #     return result
# # # # # def main():
# # # # #     multiprocessing.freeze_support()
# # # # #     pool = multiprocessing.Pool()
# # # # #     cpus = multiprocessing.cpu_count()
# # # # #     results = []
# # # # #     for i in xrange(0, cpus):
# # # # #         result = pool.apply_async(task, args=(i,))
# # # # #         results.append(result)
# # # # #     pool.close()
# # # # #     pool.join()
# # # # #     for result in results:
# # # # #         print(result.get())
# # # #
# # #
# # # #
# # # # # get the filename URL and ID
# # # # def get_filenamelistWithID():
# # # #     file_filelist= open('/Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata/filenamelist_copy.csv')
# # # #     filename_list={}
# # # #     for filenameline in file_filelist:
# # # #         filenames=filenameline.split(',',1)
# # # #         if len(filenames)==2 :
# # # #             key,value=filenames[1].strip('\n'),filenames[0]
# # # #             filename_list[key]=value
# # # #
# # # #     return filename_list
# # # #
# # # #
# # # #
# # # # a='https://developer.android.com/reference/android/R.attr.html'
# # # # filenamelist=get_filenamelistWithID()
# # # #
# # # # d = {'key':'value',}
# # # #
# # # # # how you might write a test to pull out
# # # # # the value of key from d
# # # #
# # # #
# # # # # a much simpler syntax
# # # # print(d.get('key', 'not found'))
# # # # print(d.get('foo', 'not found'))
# # # #
# # # # id=filenamelist.get(a)
# # #
# # # # get the android api package full information into an dictionary
# # # import json
# # # import os
# # # import pymysql
# # #
# # #
# # # from stanfordcorenlp import StanfordCoreNLP
# # #
# # #
# # # # get the android api package full information into an array
# # # def get_api_package_list():
# # #     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
# # #     cur = conn.cursor()
# # #
# # #     all_api_package_list = []
# # #
# # #     try:
# # #         cur.execute("select  api_package_id, name, doc_website, library_id from api_package order by api_package_id ")
# # #
# # #         results = cur.fetchall()
# # #
# # #         cur.close()
# # #
# # #         for row in results:
# # #             api_package_id=row[0];
# # #             name=row[1];
# # #             doc_website=row[2];
# # #             library_id=row[3];
# # #
# # #             all_api_package_list.insert(api_package_id,(api_package_id, name, doc_website, library_id))
# # #
# # #     except:
# # #         print("Error: unable read data from table")
# # #
# # #     conn.close()
# # #
# # #     return all_api_package_list
# # #
# # #
# # # # get the android api package full information into an array
# # # def get_api_parameter_list():
# # #     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
# # #     cur = conn.cursor()
# # #
# # #     all_api_parameter_list = []
# # #
# # #     try:
# # #         cur.execute("select  parameter_id, name, class_id, method_id, type_class, type_string from api_parameter order by method_id, parameter_id")
# # #
# # #         results = cur.fetchall()
# # #
# # #         cur.close()
# # #
# # #         for row in results:
# # #             parameter_id=row[0];
# # #             name=row[1];
# # #             class_id=row[2];
# # #             method_id=row[3];
# # #             type_class=row[4];
# # #             type_string=row[5];
# # #
# # #             all_api_parameter_list.insert(parameter_id,(parameter_id,name, class_id, method_id, type_class, type_string))
# # #
# # #     except:
# # #         print("Error: unable read data from table")
# # #
# # #     conn.close()
# # #
# # #     return all_api_parameter_list
# # #
# # # def rreplace(s, old, new, occurrence):
# # #     li = s.rsplit(old, occurrence)
# # #     return new.join(li)
# # #
# # #
# # # # package=get_api_package_list()
# # # # print(package[1])
# # # # print(package[1][0])
# # # # print(package[1][1])
# # # #
# # # # paralist=get_api_parameter_list()
# # # #
# # # # parameter_id=46
# # # #
# # # # startid=parameter_id
# # # #
# # # # print(startid)
# # # # print(paralist[startid])
# # # #
# # # # orginalStrings= "("
# # # # qualifedStr="("
# # # #
# # # # while paralist[startid][3]==method_id :
# # # #     orginalStrings= orginalStrings + paralist[startid][5] + ' ' + paralist[startid][1] + ', '
# # # #     qualifedStr=qualifedStr+paralist[startid][5]+', '
# # # #     startid=startid+1
# # # #
# # # # orginalStrings= orginalStrings[:orginalStrings.rfind(", ")] + ")"
# # # # qualifedStr=qualifedStr[:qualifedStr.rfind(", ")]+")"
# # # #
# # # # print(orginalStrings)
# # # # print(qualifedStr)
# # # #
# # # # a=[[2,3],[1,2]]
# # # # b=[1,2]
# # # #
# # # # if b in a :
# # # #     print(b)
# # # #
# # # # if [2,2] in a :
# # # #     print("ok")
# # # #
# # # # print(os.pardir)
# # # # print(os.getcwd()+'/'+'..'+'/data/filenamelist_training.csv')
# # #
# # # #
# # # # oneSent='If wakeup alarms are triggered excessively, they can drain a device\'s battery. To help Developers improve app quality, Android automatically monitors apps for excessive wakeup alarms and displays the information in Android Vitals<>. For information on how the data is collected, see "Play Console" docs . If Developer\'s app is waking up the device excessively, Developers can use the guidance in this page to diagnose and fix the problem. Fix the problem . '
# # # #
# # # # sentences=oneSent
# # # # lenth=len(oneSent.split(' '))
# # # # print(lenth)
# # # # if lenth>100 :
# # # #     sentenceslist=sentences.split('. ')
# # # #
# # # #     for i in range(0,len(sentenceslist)):
# # # #         str=sentenceslist[i]+'. '
# # # #         sentenceslist[i]=str
# # # #     for sent in sentenceslist:
# # # #         print(len(sent.split(' ')))
# # # #     print(sentenceslist)
# # # #
# # # #
# # # # lenth=len("this is .   ".strip().strip('.').strip().split(' '))
# # # # print(lenth)
# # # # i=10
# # # # print("collecting: "+str(i))
# # # #
# # # #
# # # # try_doc_id = "109_34".split('_')[0]
# # # # print(try_doc_id)
# # # #
# # #
# # #
# # # def read():
# # #     data_path = '/Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata/AndroidAPI_allSent_ascii.txt'
# # #
# # #     file = open(data_path)
# # #     wiki = []
# # #     allSent = []
# # #     id = []
# # #     for i, line in enumerate(file):
# # #         #
# # #         # separate id and tagwiki
# # #         #
# # #         id.append(line.split('\t')[0])
# # #         allSent.append(''.join(line.split('\t')[1:]))
# # #     wiki.append(id)
# # #     wiki.append(allSent)
# # #     return wiki
# # #
# # #
# # #
# # # #begin
# # # nlp = StanfordCoreNLP('http://127.0.0.1', port=9000)
# # # my_allSent = read()
# # # id = my_allSent[0]
# # # allSent = my_allSent[1]
# # # print(len(id))
# # # print(len(allSent))
# # # maxWordssectionlen = 100
# # #
# # # cur_doc_id = id[0].split('_')[0]
# # # sentenceID = id[0].split('_')[1]
# # # constuctlength = 0
# # # sent_index_list = []
# # # sentencestring = ""
# # #
# # # for sentenceID in range(0, len(id)):
# # #
# # #     # too short less then 3 words , dispose it
# # #     countlist = allSent[sentenceID].strip().strip('.').strip().split(' ')
# # #     if len(countlist) < 3:
# # #         continue
# # #
# # #     # debug for 30 sentence
# # #     if sentenceID == 100:
# # #         break
# # #
# # #     try_doc_id = id[sentenceID].split('_')[0]
# # #
# # #     cur_sent_text = allSent[sentenceID].strip('\n')
# # #     cur_sent_len = len(cur_sent_text.strip().strip('.').strip().split(' '))
# # #     if (try_doc_id == cur_doc_id) and (constuctlength + cur_sent_len < maxWordssectionlen-6):
# # #
# # #         sent_index_list.append(sentenceID)
# # #         constuctlength = constuctlength + cur_sent_len
# # #         sentencestring = sentencestring + cur_sent_text
# # #         continue
# # #     else:
# # #         backup_index_list = sent_index_list
# # #         backup_sentencestring = sentencestring
# # #         sent_index_list = []
# # #         sentencestring = ""
# # #         if (try_doc_id != cur_doc_id) :
# # #             cur_doc_id=try_doc_id
# # #
# # #         # record and prepare next batch
# # #
# # #         sent_index_list.append(sentenceID)
# # #         constuctlength = cur_sent_len
# # #         sentencestring = sentencestring  + cur_sent_text
# # #
# # #         print("\n********************************************")
# # #         print("the process sentences:")
# # #         print("the doc id is :"+ str(cur_doc_id))
# # #         print(backup_sentencestring)
# # #
# # #
# # #         # do corference work
# # #         Asentence = nlp.word_tokenize(backup_sentencestring)
# # #         output = nlp.annotate(backup_sentencestring, properties={'annotators': 'dcoref', 'pipelineLanguage': 'en'})
# # #         # print('CoReference :', output)
# # #         # nlp.close()
# # #         newoutput = json.loads(output, strict=False)
# # #
# # #         coreferencelist = newoutput.get("corefs")
# # #         #
# # #         # print(len(coreferencelist))
# # #         # # print(coreferencelist.items())
# # #         # print(coreferencelist.keys())
# # #         # # print(coreferencelist.values())
# # #         newsentence = Asentence
# # #
# # #         indices = [i for i, x in enumerate(newsentence) if x == '.']
# # #         # print(indices[0])
# # #
# # #         print(newsentence)
# # #         for key in coreferencelist.keys():
# # #             coreferenceitem = coreferencelist.get(key)
# # #             print(len(coreferenceitem))
# # #             if len(coreferenceitem) > 1:
# # #                 for itemindex in range(0, len(coreferenceitem)):
# # #                     if coreferenceitem[itemindex].get("isRepresentativeMention") is True:
# # #                         text1 = coreferenceitem[itemindex].get("text")
# # #
# # #                 for itemindex in range(0, len(coreferenceitem)):
# # #                     if coreferenceitem[itemindex].get("isRepresentativeMention") is False:
# # #                         startindex = int(coreferenceitem[itemindex].get("startIndex"))
# # #                         endindex = int(coreferenceitem[itemindex].get("endIndex"))
# # #                         headindex = int(coreferenceitem[itemindex].get("headIndex"))
# # #                         sentnum = int(coreferenceitem[itemindex].get("sentNum"))
# # #                         text2 = coreferenceitem[itemindex].get("text")
# # #                         beginindex = 0
# # #                         if len(text2) < len(text1):
# # #                             if sentnum > 1:
# # #                                 beginindex = indices[sentnum - 2] + 1
# # #
# # #                             for i in range(beginindex + startindex - 1, beginindex + endindex - 1):
# # #                                 newsentence[i] = ""
# # #                             newsentence[beginindex + startindex - 1] = text1
# # #
# # #         wholenewsentence = ' '.join(newsentence)
# # #         wholenewsentence = wholenewsentence.replace(' -LRB- ', '(') \
# # #             .replace('-RRB- ', ') ').replace(' -LSB- ', '[') \
# # #             .replace('-RSB- ', '] ').replace(' \'s', '\'s') \
# # #             .replace(' .', '. ').replace('  ', ' ')
# # #
# # #         print(wholenewsentence)
# # #
# # #         # assign new sentence back
# # #         wholenewsentencelist = wholenewsentence.split('. ')
# # #         for nidex in range(0, len(backup_index_list)):
# # #             allSent[backup_index_list[nidex]] = wholenewsentencelist[nidex]+'. '
# # #
# # #
# # import operator
# # import re
# #
# # # a=set()
# # # a.add(('34','kdfjk',98))
# # # a.add(('67','we',98))
# # # a.add(('34','kdfjk',98))
# # # a.add(('35','kdfjk',98))
# # #
# # # b=list(a)
# # # print(type(a))
# # # print(len(a))
# # # for j in a:
# # #     print(j)
# # #
# # # print(type(b))
# # # print(b)
# # # for i in b:
# # #     print(i)
# #
# # def tsplit(string, delimiters):
# #     """Behaves str.split but supports multiple delimiters."""
# #
# #     delimiters = tuple(delimiters)
# #     stack = [string, ]
# #
# #     for delimiter in delimiters:
# #         for i, substring in enumerate(stack):
# #             substack = substring.split(delimiter)
# #             stack.pop(i)
# #             for j, _substring in enumerate(substack):
# #                 stack.insert(i + j, _substring)
# #
# #     return stack
# #
# #
# #
# #
# #
# # text=''
# # listposition=[]
# # position=0
# # s='this is. good thing ! sdfkjlsdfj .  sdkfjsladf? '
# # for m in re.finditer(r'\. ',s):
# #     position = m.start()
# #     print('.:', m.start(), m.end())
# #     listposition.append(position)
# #
# # for m in re.finditer(r'\?',s):
# #     position = m.start()
# #     print('?:', m.start(), m.end())
# #     listposition.append(position)
# #
# # for m in re.finditer(r'\!',s):
# #     position = m.start()
# #     print('!:', m.start(), m.end())
# #     listposition.append(position)
# #
# # print(listposition)
# #
# # listposition.sort()
# # print(listposition)
# #
# # for item in listposition:
# #     print(item)
# #
# #
# #
# # newlist=tsplit(s,('. ','? ','! '))
# #
# # print(newlist)
# #
# # id=[]
# # allSent=[]
# # id.append('1_3')
# # id.append('1_4')
# # allSent.append('sfsdflksdfl .sf sdkfjls fad. \n')
# # allSent.append('dfkj sldfkj .sdfjksdf. sdfjksdf! \n')
# #
# # for i in range(0, len(allSent)):
# #     print(id[i] + '\t' + allSent[i])
# # print('Finished to generate coreference')
# import pymysql
#
#
# def searching_in_entities_data(keywords):
#     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
#     cur = conn.cursor()
#
#     all_Entities_list = []
#
#     try:
#         # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))
#
#         # select * from t1 where 'ABCDEFG'  LIKE CONCAT('%', column1, '%');
#         #     SELECT * FROM table WHERE Contains(Column, '"*test*"') > 0
#
#         cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s or entities.QualifiedName LIKE %s",(keywords,keywords))
#
#         results = cur.fetchall()
#
#         cur.close()
#
#         for row in results:
#             id = row[0]
#             EntityName = row[1]
#             EntitySection = row[2]
#             EntityURL = row[3]
#             EntityParent = row[4]
#             EntityType = row[5]
#             EntityOriginal = row[6]
#             URLid = row[7]
#             QualifiedName=row[8]
#
#             all_Entities_list.append((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
#     except:
#         print("Error: unable read data from table")
#
#     conn.close()
#
#     return all_Entities_list
#
#
# # find the just current name from qualified name
# def getKeywordsonly(keywords):
#     if '(' in keywords:
#         keywords = keywords.rsplit('(')[0]
#
#     if '[' in keywords:
#         keywords = keywords.rsplit('[')[0]
#
#     if '.' in keywords:
#         keywords = keywords.rsplit('.', 1)[1]
#
#     return keywords
#
#
#
# # start ...
# keywords='the DownloadManager Query'
# # oringinalkeywords='Query'
# # if '(' in keywords:
# #     keywords=keywords.rsplit('(')[0]
# # print(keywords)
# #
# # if '[' in keywords:
# #     keywords=keywords.rsplit('[')[0]
# # print(keywords)
# #
# # if '.' in keywords:
# #     keywords=keywords.rsplit('.',1)[1]
# # print(keywords)
#
#
# schema_list=[]
#
# entity1 = keywords
# relation = keywords
# entity2 = keywords
# entity_url_id = "626"
#
# sentence_id = "626_1"
# sentence_text = "keywords keywords keywords"
#
# relation_id = "626_1_1"
#
# doc_id = "626"
#
# print(entity1, relation, entity2)
# # entity1 = getKeywordsonly(entity1)
# # entity2 = getKeywordsonly(entity2)
# listtest=[]
# a=keywords.split(' ')
# for i in range (0,len(a)-1):
#     listest1=(searching_in_entities_data(a[i]))
#     for j in range(0,len(listest1)-1):
#         listtest.append(listest1[j])
# print(listtest)
#
# entity1list = searching_in_entities_data(entity1)
# entity2list = searching_in_entities_data(entity2)
# print(entity1list)
# # print(entity2list)
# # print(searching_in_entities_data('Query',oringinalkeywords.replace(' ',' or ')))
#
#
#
# collectingset = set()
#
# if len(entity1list) > 0 or len(entity2list) > 0:
#     if len(entity1list) > 0:
#         for entity1i in range(0, len(entity1list)):
#             section = entity1list[entity1i][2]
#             url = entity1list[entity1i][3]
#             collectingset.add(
#                 (entity1, relation, entity2, section, url, sentence_text, entity_url_id, sentence_id, relation_id))
#     if len(entity2list) > 0:
#         for entity2i in range(0, len(entity2list)):
#             section = entity2list[entity2i][2]
#             url = entity2list[entity2i][3]
#             collectingset.add(
#                 (entity1, relation, entity2, section, url, sentence_text, entity_url_id, sentence_id, relation_id))
#
# # convert set to list
# collectinglist = list(collectingset)
#
# if len(collectinglist) > 0:
#     for collectingi in range(0, len(collectinglist)):
#         # add it  as a relation
#         schema_list.append(collectinglist[collectingi])
#
# print(schema_list)

#
# s="An a the goodthe the"
# item_list=s.split(' ')
# # item_list = ['item', 5, 'foo', 3.14, True]
# new_list = []
# for e in item_list:
#     if e not in ('the', 'The','a','A','an','An'):
#         new_list.append(e)
# item_list = new_list
#
# print(item_list)

# def searching_in_entities_data(keywords,urlid):
import re

import pymysql


def searchingWarningPatterninSentence(keywords):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Sentences_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute(
            "select id, sentenceId,sentenceText  from allSentences where sentenceText like %s ", ('%'+keywords+'%'))

        # or FIND_IN_SET(sentenceText, %s)!=0
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

# =====get relation ids
def get_all_relation_id_data(sentence_id):
    all_relation_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root',passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()
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

# print(len(get_all_relation_id_data('101_5')))
# print(get_all_relation_id_data('101_5'))

# def searching_in_entities_data(keywords,urlid):
def searching_in_entities_data2(keywords1, keywords2):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = set()

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute(
            "select DISTINCT  id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where FIND_IN_SET(EntityName,%s)!=0 or FIND_IN_SET(EntityName,%s)!=0 ",
            (keywords1, keywords2))

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where match(%s) against(EntityName in natural LANGUAGE mode) ",(keywords))
        # SELECT COUNT(*) FROM articles WHERE MATCH (title,body) AGAINST ('database' IN NATURAL LANGUAGE MODE);

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

            # print("entity name:"+EntityName)
            # print("search word is :"+keywords1)

            all_Entities_list.add((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return list(all_Entities_list)


# def searching_in_entities_data(keywords,urlid):
def searching_in_entities_data1(keywords1,idliststr):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = set()

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select DISTINCT  id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where (FIND_IN_SET(EntityName,%s)!=0) and FIND_IN_SET(id , %s)=0 ",(keywords1, idliststr))

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where match(%s) against(EntityName in natural LANGUAGE mode) ",(keywords))
        # SELECT COUNT(*) FROM articles WHERE MATCH (title,body) AGAINST ('database' IN NATURAL LANGUAGE MODE);

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

            # print("entity name:"+EntityName)
            # print("search word is :"+keywords1)

            all_Entities_list.add((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return list(all_Entities_list)



def searching_in_entities_data3(keywords1):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = set()

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select DISTINCT  id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where FIND_IN_SET(EntityName,%s)!=0 ",(keywords1))

        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where match(%s) against(EntityName in natural LANGUAGE mode) ",(keywords))
        # SELECT COUNT(*) FROM articles WHERE MATCH (title,body) AGAINST ('database' IN NATURAL LANGUAGE MODE);

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

            # print("entity name:"+EntityName)
            # print("search word is :"+keywords1)

            all_Entities_list.add((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return list(all_Entities_list)



def searching_in_entities_data(keywords1, keywords2,idstr):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='AndroidGuideAPI')
    cur = conn.cursor()

    all_Entities_list = []

    try:
        # cur.execute("select id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where Entities.EntityName LIKE %s and URLid = %s",(keywords,urlid))

        cur.execute("select DISTINCT  id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName from Entities where (FIND_IN_SET(EntityName,%s)!=0 or FIND_IN_SET(EntityName,%s)!=0) and FIND_IN_SET(id , %s)=0  ",(keywords1, keywords2, idstr))

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

            print("entity name:"+EntityName)
            print("search word is 1 :"+keywords1 )
            print("search word is 2 :"+ keywords2)

            all_Entities_list.append((id, EntityName, EntitySection, EntityURL, EntityParent, EntityType, EntityOriginal, URLid, QualifiedName))
    except:
        print("Error: unable read data from table")

    conn.close()

    return all_Entities_list


print(len(searching_in_entities_data2('The Android Robot logo'.replace(' ',','),'Calculator Camcorder Camera Contacts Custom Locale version'.replace(' ',','))))

# print(len(searching_in_entities_data1('The Android Robot logo'.replace(' ',','))))
# print(len(searching_in_entities_data1('Calculator Camcorder Camera Contacts Custom Locale version'.replace(' ',','))))
#
#
#
# print(len(searching_in_entities_data3('Calculator Camcorder Camera Contacts Custom Locale version'.replace(' ',','))))
# liststr=[152343,73179,113115,116070]
# strs=''
# for i in range(0,len(liststr)):
#     strs=strs+str(liststr[i])+','
#
#
# strs=strs.strip(',')
# print(strs)
# strs=''
#
# print(searching_in_entities_data1('Calculator Camcorder Camera Contacts Custom Locale version'.replace(' ',','),strs))


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

sentencetext="This is good"

print(str.lower(sentencetext))
print(c_e_s('this',str.lower(sentencetext)))
print(c_e_s('This',sentencetext))