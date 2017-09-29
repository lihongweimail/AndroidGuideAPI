# # 清除非ASCII符号
# text="an item—you should explicitly show"
#
# for i in text :
#     if ord(i) > 150 or  ord(i)< 151 or ord(i)<128:
#         print(i)
#

# def takeListSecond(elem):
#     return elem[1]
#
# header_list=[]
#
# header_list.append(("hellosdjfkf", 0, 'h1'))
# header_list.append(("hello", 2, 'h2'))
# header_list.append(("hello", 1, 'h1'))
# header_list.append(("hellosdfaad", 1, 'h2'))
# header_list.append(("hellsfsfo", 0, 'h3'))
#
# header_list.sort(key=takeListSecond)
#
# print(header_list)

#remove non ascii char
import re

#
# def remove_file_non_ascii_char():
#     fileSent=open('/Users/Grand/Downloads/HDSKG/tempdata/AndroidAPI_allSent.txt')
#     fileNewSent=open('/Users/Grand/Downloads/HDSKG/tempdata/AndroidAPI_allSent_ascii.txt','w')
#
#     for i,oneSent in enumerate(fileSent) :
#
#         oneSent=''.join([i if (ord(i) < 128) and (i is not '\n') else ' ' for i in oneSent])
#
#         fileNewSent.write(oneSent.strip(' '))
#         fileNewSent.write('\n')
#
#
#     fileSent.close()
#     fileNewSent.close()
#     return
#
#
#
#
# #check file content at line
# def find_line_content_by_debug():
#     # fileopen=open('/Users/Grand/Downloads/HDSKG/tempdata/AndroidAPI_allSent_forClaseIE.txt')
#     fileopen = open('/Users/Grand/Downloads/HDSKG/tempdata/seRelFeatures_idRel.csv')
#
#     for i,oneSent in enumerate(fileopen) :
#         linecontents=oneSent.split(',')
#
#         print(linecontents[37])
#         print(linecontents[38])
#
#
#     fileopen.close()
#     return

#
# #check file content at line
# def collect_training_triple_file():
#
#    filefilenameid = open('/Users/Grand/Downloads/HDSKG/tempdata/filenamelist.csv')
#    fileallSent= open('/Users/Grand/Downloads/HDSKG/tempdata/AndroidAPI_allSent_ascii.txt')
#    fileallRelation = open('/Users/Grand/Downloads/HDSKG/tempdata/androidAPIallCand5.txt')
#
#    dict_filenameid = {}
#
#    for line in filefilenameid:
#       data = line.lstrip(',',1)
#
#       if len(data) == 2:
#          key, value = data[0], data[1]
#          dict_filenameid[key] = value.rstrip('\n')
#
#    dict_allsentence = {}
#
#    for line in fileallSent:
#       data = line.lstrip('\t', 1)
#       if len(data) == 2:
#          key, value = data[0], data[1]
#          dict_allsentence[key] = value.rstrip('\n')
#
#    phrase_list = []
#    for one_phrase in file_key_phrase:
#       phrase_u_id = one_phrase.split(', ')[0]
#       pure_phrase = one_phrase.split(', ')[1].split('(')[0]
#       pure_phrase = pure_phrase.replace('$', r'\$').replace('*', r'\*').replace('+', r'\+').replace('.', r'\.').replace('[', r'\[').replace(']', r'\]').replace('?', r'\?').replace('|', r'\|').replace('\'', r'\'').replace('\"', r'\"')
#       p_uid_list.append(phrase_u_id)
#       pure_section = one_phrase.split(', ')[2]
#       pure_url = one_phrase.strip('\r\n').split(', ')[3]
#       phrase_list.append(pure_phrase)
#       section_list.append(pure_section)
#       url_list.append(pure_url)
#
#    allRelation_list = []
#
#    for j,one_triple in enumerate(fileallRelation):
#             # all triple example:
#             # {'subject_ori': 'administrators', 'relation_ori': 'configure', 'object_ori': 'app', 'subject': 'administrators', 'relation': 'configure', 'object': 'app', 'subject_stand': 'administrator', 'relation_stand': 'configure', 'object_stand': 'app', 'start_index': 14, 'end_index': 21, 'originalSent_len': 27, 'pos': 'NNS VB NN', 'relationType': 'NonTaxo', 'rel_id': '11352_27_1'}
#
#       entity1 = one_triple['subject_ori']
#       relation = one_triple['relation_ori']
#       entity2 = one_triple['object_ori']
#       entity_url_id = one_triple['rel_id'].split('_')[0]
#       sentence_id = one_triple['rel_id'].rsplit('_', 1)[0]
#       sentence_text = dict_allsentence[sentence_id]
#       relation_id = one_triple['rel_id']
#       section=''
#       for i, one_phrase in enumerate(phrase_list):
#          if entity_url_id == p_uid_list[i]  and (re.search('\\b' + one_phrase + '\\b', entity1) or re.search('\\b' + one_phrase + '\\b',entity2)):
#             section = section_list[i]
#
#       url=dict_filenameid[entity_url_id]
#       if ('/training/' in url) :
#          allRelation_list.append((entity1, relation, entity2, section, url, sentence_text,entity_url_id,sentence_id,relation_id))
#
#
#    fileallRelation.close()
#    fileallSent.close()
#    filefilenameid.close()
#    return


#
# a = next(x for x in A if y in x)
#
# if a is not None:
#     print(a)
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print("####")




def compare_exact_string(checkword, checkString):
    str1list=checkword.split()
    str2list=checkString.split()
    flag=True
    for word in str1list:
        if word not in str2list :
            flag=False
            break;
    return flag


str2 = "ifaward-winnin ifx one  blueberries awardx awar"
test ="ifx one"

print(compare_exact_string(test,str2))
