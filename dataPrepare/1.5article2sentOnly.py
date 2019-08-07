#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

import os
import re
import string

from pycorenlp import *
import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import codecs
import chardet
######################data preprocess#####################
def id_tag_dict():
	data_path = os.pardir + '/data'

	id_tag = data_path+'/androidAPI_id_tag.csv'

	#
	# make id_tag dictionary
	#
	file = open(id_tag,'r',encoding='utf-8')
	id_tag_dict = {}
	for i, line in enumerate(file):
		id = line.split(',')[0]
		tag = line.split(',')[1].strip()

		#
		# make dictionary
		#
		id_tag_dict[int(id)] = tag
	return id_tag_dict

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



# down vote
# Here's a safe way for any iterable of delimiters, using regular expressions:
#
# >>> import re
# >>> delimiters = "a", "...", "(c)"
# >>> example = "stackoverflow (c) is awesome... isn't it?"
# >>> regexPattern = '|'.join(map(re.escape, delimiters))
# >>> regexPattern
# 'a|\\.\\.\\.|\\(c\\)'
# >>> re.split(regexPattern, example)
# ['st', 'ckoverflow ', ' is ', 'wesome', " isn't it?"]

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

def main():
	data_path = '/Users/Grand/Downloads/AndroidAPIKG/HDSKG/tempdata'
	allSent = []
	# file_name_list=get_filenamelistWithID()
	file_w = open(data_path+'/androidAPIallSentICSME.txt','w',encoding='utf-8')
	wiki = data_path+'/AndroidAPI_Doc_out_ascii.txt'
	all_Doc_file = open(wiki,'r',encoding='utf-8')

	for i, line in enumerate(all_Doc_file):

		line=line.strip('\n')
		idstr=line.split('\t')[0]
		otherstr=line.split('\t')[1:]
		id = int(idstr)

		listdot=[]



		listdot=(' '.join(otherstr)).strip().split('. ')

		listq = []
		listexclaim = []

		for dotsentence in listdot:
			if '? ' in dotsentence:
				questionlist=dotsentence.split('? ')
				qj=0
				for qsent in questionlist:
					if qj==len(questionlist)-1:
						listq.append(qsent)
					else :
						listq.append(qsent+'? ')
					qj=qj+1
			else:
				listq.append(dotsentence)

		for questionsentece in listq:
			if '! ' in questionsentece:
				excllist = questionsentece.split('! ')
				exj=0
				for exqsent in excllist:
					if exj == len(excllist) - 1:
						listexclaim.append(exqsent)
					else:
						listexclaim.append(exqsent + '! ')
					exj=exj+1
			else:
				listexclaim.append(questionsentece)

		onewiki=[]
		for oneS in listexclaim:
			if ('? ' in oneS) or ('! ') in oneS :
				onewiki.append(oneS)
			else:
				onewiki.append(oneS+'. ')

		# if sentence lower than 3 word, delete it
		#
		for j, oneSent in enumerate(onewiki):
			# print oneSent
			# print len(oneSent)

			if len(oneSent.replace('  ',' ').strip().split(' ')) < 3 or len(oneSent) < 3:
				# print oneSent
				del onewiki[j]
			#


			temptext=oneSent
			if type(oneSent) is bytes:
				temptext="".join(map(chr,oneSent))


			temptext=temptext.strip()
			if temptext is "":
				continue

			#清除非ASCII符号
			temptext=''.join([i if ord(i) < 128 else ' ' for i in temptext])
			dirty=temptext

			temptext=re.sub(r'[\0\200-\377]','',dirty)
			temptext=str(temptext)


			# print(type(temptext))


			temptext = ('%d_%d\t%s') % (id, j, temptext.strip())
			a1re=re.compile(r'\.+')
			temptext=a1re.sub('.',temptext)

			oneSent=temptext
			# print oneSent + '    after bbbbbbbbbbbbbb'
			# allSent.append(oneSent)
			file_w.write(oneSent + ' \n')
		print("constructing document index: "+str(i))
	file_w.close()
	all_Doc_file.close()



main()