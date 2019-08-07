#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

import json
import operator
import os
import re
import sys
import codecs
import chardet

# reload(sys)
# sys.setdefaultencoding("utf-8")

import nltk
from pycorenlp import *
import collections

import math
from textblob import TextBlob as tb
from nltk import word_tokenize, pos_tag


from stanfordcorenlp import StanfordCoreNLP


# nlp = StanfordCoreNLP("http://localhost:9000/")
nlp = StanfordCoreNLP('http://127.0.0.1', port=9000)




def read():
    data_path = os.pardir + '/tempdata'
    wiki = data_path + '/androidAPIallSentICSME.txt'
    file = open(wiki)
    wiki = []
    allSent = []
    id = []
    for i, line in enumerate(file):
        #
        # separate id and tagwiki
        #
        id.append(line.split('\t')[0])
        allSent.append(''.join(line.split('\t')[1:]))
    wiki.append(id)
    wiki.append(allSent)
    return wiki


def write(all_relCand):
    data_path = os.pardir + '/tempdata'
    file_w = open(data_path + '/androidAPIallCand5ICSME.txt', 'w')
    for i, line in enumerate(all_relCand):
        file_w.write(str(line).strip(',') + '\n')
    print('Finished to generate allCand')


def writeCorefenence(id,allSent):
    data_path = os.pardir + '/tempdata'
    file_w = open(data_path + '/androidAPICoreferenceSentenceICSME.txt', 'w')
    for i in range(0,len(allSent)):
        file_w.write(id[i]+'\t'+allSent[i])
    print('Finished to generate coreference')

######################coreNLP#####################

def coreNLP(sent):

    try:
        output = nlp.annotate(sent, properties={"annotators": "tokenize,ssplit,pos,depparse,natlog", "outputFormat": "json","triple.strict": "true"})
    except:
        pass
        # check next sentence
        return "bad"

    if isinstance(output,str):
        output=eval(output)
    # print output
    tokens = output['sentences'][0]['tokens']
    dep = output['sentences'][0]['enhancedPlusPlusDependencies']
    # print posCont
    # print '------------------------------------------------'
    # print tokens

    pos_list = []
    for j, onepos in enumerate(tokens):
        pos_list.append(onepos['pos'])
    # print pos_list

    lemmas_list = []
    for j, onelemma in enumerate(tokens):
        lemmas_list.append(onelemma['lemma'].lower())
    # print lemmas_list

    pos_index_list = []
    for j, onepos in enumerate(tokens):
        pos_index_list.append((onepos['originalText'], onepos['pos'], onepos['index']))
    # print pos_index_list

    dep_list = []
    for j, onedep in enumerate(dep):
        if onedep['dep'][:5] == 'nsubj':
            dep_list.append(('nsubj', onedep['dependent'], onedep['governor']))
        elif onedep['dep'][:4] == 'nmod':
            dep_list.append(('nmod', onedep['governor'], onedep['dependent'], onedep['dep'][5:]))
        elif onedep['dep'][:3] == 'cop':
            dep_list.append(('cop', onedep['dependent'], onedep['governor']))
        elif onedep['dep'][:4] == 'dobj':
            dep_list.append(('dobj', onedep['governor'], onedep['dependent']))
        elif onedep['dep'][:5] == 'xcomp':
            dep_list.append(('xcomp', onedep['governor'], onedep['dependent']))
    # print dep_list
    return (pos_list, pos_index_list, lemmas_list, dep_list)


######################NPVPchunking#####################
def NPVPchunking(pos_index_list):
    # grammar = """	VP: {<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<NN|NP>?<TO*>+}
    # 				VP: {<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<NN|NP>?<IN*>+<VBG>+}
    # 				VP: {<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<NN|NP>?<IN*>+}
    # 				VP: {<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>+}
    # 				NP: {<CD>*<DT>?<CD>*<JJ>*<CD>*<VBD|VBG>*<NN.*>*<POS>*<CD>*<NN.*>+<POS>*<CD>*<NN.*>*}
    # 				VP: {<VB.*>}
    # 				"""
    grammar = """	VVP: {<MD>*<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<TO*>+<VB>+}
                    VVP: {<MD>*<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<IN*>+<VBG>+}
                    VP: {<MD>*<VB.*>+<CD>*<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<IN*|TO*>+}
                    VP: {<MD>*<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>?<DT>?<IN*|TO*>+}
                    VP: {<MD>*<VB.*>+<JJ>*<RB>*<JJ>*<VB.*>+}
                    NP: {<CD>*<DT>?<CD>*<JJ>*<CD>*<VBD|VBG>*<NN.*>*<POS>*<CD>*<VBD|VBG>*<NN.*>*<VBD|VBG>*<NN.*>*<POS>*<CD>*<NN.*>+}
                    VP: {<MD>*<VB.*>+}
                    """
    triplePar = nltk.RegexpParser(grammar)
    # print pos_index_list
    tripleTree = triplePar.parse(pos_index_list)

    npvp_list = []
    for j, subtree in enumerate(tripleTree.subtrees()):
        # print subtree.label()
        # print '--------------------------'
        # print subtree.leaves()
        if subtree.label() == 'NP' or subtree.label() == 'VP' or subtree.label() == 'VVP':
            # print 'find'
            npvp_list.append(subtree)
        # print len(npvp_list)
    return npvp_list


def rel_index(dep_list):
    # change used to's subj
    for j, one_dep in enumerate(dep_list):
        if one_dep[0] == 'xcomp':
            for k, one_dep_k in enumerate(dep_list):
                if one_dep_k[0] == 'nsubj' and one_dep_k[2] == one_dep[1]:
                    dep_list.append(('nsubj', one_dep_k[1], one_dep[2]))

    # delete nmod if obj
    for j, one_dep in enumerate(dep_list):
        if one_dep[0] == 'dobj':
            for k, one_dep_k in enumerate(dep_list):
                if one_dep_k[0] == 'nmod' and one_dep_k[1] == one_dep[1]:
                    del dep_list[k]

    # find is relation
    relation_index = []
    for j, one_dep in enumerate(dep_list):
        if one_dep[0] == 'cop':
            for k, one_dep_k in enumerate(dep_list):
                if one_dep_k[0] == 'nsubj' and one_dep_k[2] == one_dep[2]:
                    relation_index.append(('txno', one_dep_k[1], one_dep[1], one_dep_k[2]))

    # find other relation
    for j, one_dep in enumerate(dep_list):
        if one_dep[0] == 'dobj':
            for k, one_dep_k in enumerate(dep_list):
                if one_dep_k[0] == 'nsubj' and one_dep_k[2] == one_dep[1]:
                    relation_index.append(('non-txno', one_dep_k[1], one_dep[1], one_dep[2]))

    # find other relation
    for j, one_dep in enumerate(dep_list):
        if one_dep[0] == 'nmod':
            for k, one_dep_k in enumerate(dep_list):
                if one_dep_k[0] == 'nsubj' and one_dep_k[2] == one_dep[1]:
                    relation_index.append(('non-txno', one_dep_k[1], one_dep[1], one_dep[2], one_dep[3]))

    return relation_index


def gen_rel():


    oneRel = {}
    allRelCand = []
    for i, oneSent in enumerate(allSent):
        countlist = oneSent.strip().strip('.').strip().split(' ')

        if len(countlist) < 3:
            continue

        # debug for 30 sentence
        # if i == 20:
        #     break
        # oneSent='[ L ("no"), C ("NO"), V ("NY")] [ L ("no"), C ("NO")] [ L ("no")] Locale.ROOT. '

        print(i)

        # print oneSent
        taggedOneSent = coreNLP(str(oneSent))
        if taggedOneSent =="bad":
            continue
        pos_index_list = taggedOneSent[1]
        lemmas_list = taggedOneSent[2]
        dep_list = taggedOneSent[3]

        myrel_index = rel_index(dep_list)
        # print pos_index_list
        # print lemmas_list
        npvp_list = NPVPchunking(pos_index_list)
        # print len(npvp_list)
        # print myrel_index
        numCandRel = 0
        for j, oneRelIndex in enumerate(myrel_index):

            subject_ori = ''
            relation_ori = ''
            object_ori = ''

            subject = ''
            relation = ''
            object = ''

            subject_stand = ''
            relation_stand = ''
            object_stand = ''

            pos_subj = ''
            pos_rel = ''
            pos_obj = ''

            start_index = 0
            end_index = 0

            oneRel = {}
            for k, one_npvp in enumerate(npvp_list):
                # print one_npvp.leaves()
                # print one_npvp.label()
                # print 'above is leaves'
                if one_npvp.label() == 'NP':
                    for u, one_leaves in enumerate(one_npvp.leaves()):
                        if one_leaves[2] == oneRelIndex[1]:  # subj in np, generate subj
                            for h, y in enumerate(one_npvp.leaves()):
                                subject_ori += y[0] + ' '
                                if y[1] != 'DT':
                                    subject += y[0] + '_'
                                    subject_stand += lemmas_list[y[2] - 1] + ' '
                                    pos_subj += pos_index_list[y[2] - 1][1] + ' '
                                if h == 0:
                                    start_index = y[2]
                            subject_ori = subject_ori.strip(' ')
                            subject = subject.strip('_')
                            subject_stand = subject_stand.strip(' ')
                            pos_subj = pos_subj.strip(' ')

                        elif one_leaves[2] == oneRelIndex[3]:  # obj in np, generate obj
                            for h, y in enumerate(one_npvp.leaves()):
                                object_ori += y[0] + ' '
                                if y[1] != 'DT':
                                    object += y[0] + '_'
                                    # print pos_index_list[y[2] - 1][1]
                                    object_stand += lemmas_list[y[2] - 1] + ' '
                                    pos_obj += pos_index_list[y[2] - 1][1] + ' '
                                if h == len(one_npvp.leaves()) - 1:
                                    end_index = y[2]
                            object_ori = object_ori.strip(' ')
                            object = object.strip('_')
                            object_stand = object_stand.strip(' ')
                            pos_obj = pos_obj.strip(' ')
                elif one_npvp.label() == 'VP':
                    if len(oneRelIndex) == 5:
                        for u, one_leaves in enumerate(one_npvp.leaves()):
                            if one_leaves[2] == oneRelIndex[2]:
                                for h, y in enumerate(one_npvp.leaves()):
                                    if h == (len(one_npvp.leaves()) - 1) and oneRelIndex[4] != 'agent' and (
                                            pos_index_list[y[2] - 1][1] == 'IN' or pos_index_list[y[2] - 1][1] == 'TO'):
                                        relation_ori += oneRelIndex[4] + ' '
                                        relation += oneRelIndex[4] + '_'
                                        # print oneRelIndex[4]
                                        relation_stand += oneRelIndex[4].lower() + ' '
                                        pos_rel += pos_index_list[y[2] - 1][1] + ' '
                                    else:
                                        relation_ori += y[0] + ' '
                                        relation += y[0] + '_'
                                        relation_stand += lemmas_list[y[2] - 1] + ' '
                                        pos_rel += pos_index_list[y[2] - 1][1] + ' '
                    else:
                        for u, one_leaves in enumerate(one_npvp.leaves()):
                            if one_leaves[2] == oneRelIndex[2]:
                                for h, y in enumerate(one_npvp.leaves()):
                                    # print y
                                    relation_ori += y[0] + ' '
                                    relation += y[0] + '_'
                                    relation_stand += lemmas_list[y[2] - 1] + ' '
                                    pos_rel += pos_index_list[y[2] - 1][1] + ' '
                elif one_npvp.label() == 'VVP':
                    # print len(oneRelIndex)
                    if len(oneRelIndex) == 5:
                        for u, one_leaves in enumerate(one_npvp.leaves()):
                            if one_leaves[2] == oneRelIndex[2]:
                                for h, y in enumerate(one_npvp.leaves()):
                                    # print y
                                    if h == (len(one_npvp.leaves()) - 2) and oneRelIndex[4] != 'agent' and \
                                            (pos_index_list[y[2] - 2][1] == 'IN' or pos_index_list[y[2] - 1][
                                                1] == 'TO'):
                                        relation_ori += oneRelIndex[4] + ' '
                                        relation += oneRelIndex[4] + '_'
                                        # print oneRelIndex[4]
                                        relation_stand += oneRelIndex[4].lower() + ' '
                                        pos_rel += pos_index_list[y[2] - 1][1] + ' '
                                    elif h <= (len(one_npvp.leaves()) - 2):
                                        relation_ori += y[0] + ' '
                                        relation += y[0] + '_'
                                        relation_stand += lemmas_list[y[2] - 1] + ' '
                                        pos_rel += pos_index_list[y[2] - 1][1] + ' '
                    else:
                        for u, one_leaves in enumerate(one_npvp.leaves()):
                            if one_leaves[2] == oneRelIndex[2]:
                                for h, y in enumerate(one_npvp.leaves()):
                                    relation_ori += y[0] + ' '
                                    relation += y[0] + '_'
                                    relation_stand += lemmas_list[y[2] - 1] + ' '
                                    pos_rel += pos_index_list[y[2] - 1][1] + ' '
                relation_ori = relation_ori.strip(' ')
                relation = relation.strip('_')
                relation_stand = relation_stand.strip(' ')
                pos_rel = pos_rel.strip(' ')

            if subject_ori != '' and relation_ori != '' and object_ori != '':
                numCandRel += 1

                oneRel['subject_ori'] = subject_ori
                oneRel['relation_ori'] = relation_ori
                oneRel['object_ori'] = object_ori

                oneRel['subject'] = subject
                oneRel['relation'] = relation
                oneRel['object'] = object

                oneRel['subject_stand'] = subject_stand
                oneRel['relation_stand'] = relation_stand
                oneRel['object_stand'] = object_stand

                oneRel['start_index'] = start_index
                oneRel['end_index'] = end_index
                oneRel['originalSent_len'] = pos_index_list[-1][2]

                oneRel['pos'] = (pos_subj + ' ' + pos_rel + ' ' + pos_obj)

                if relation_ori == 'is a kind of' or relation_ori == 'is' or relation_ori == 'including':
                    oneRel['relationType'] = 'Taxo'
                else:
                    oneRel['relationType'] = 'NonTaxo'
                oneRel['rel_id'] = ('%s_%s') % (id[i], str(numCandRel))
                print('-------------------')
                print(str(oneRel['subject'] + ';     ' + oneRel['relation'] + ';    ' + oneRel['object']).replace('_',
                                                                                                                  ' '))
                print('-------------------')
                print(oneRel)
                print(type(oneRel))
                allRelCand.append(oneRel)
        # print '----------------------------------------------------------------------------------------------'
    write(allRelCand)






def doCoreferenceWork():
    # begin

    data_path = os.pardir + '/tempdata'
    fileback_w = open(data_path + '/androidAPICoreferenceSentenceICSME_back.txt', 'w')


    cur_doc_id = id[0].split('_')[0]
    sentenceID = id[0].split('_')[1]
    constuctlength = 0
    sent_index_list = []
    sentencestring = ''
    countSentlist=[]

    for sentenceID in range(0, len(id)):

        # too short less then 3 words , dispose it
        cur_sent_text=allSent[sentenceID].strip('\n')
        countlist = cur_sent_text.strip().strip('. ').strip('? ').strip('! ').strip().split(' ')
        if len(countlist) < 3:
            fileback_w.write(id[sentenceID]+'\t'+allSent[sentenceID])
            continue

        # debug for 30 sentence
        # if sentenceID == 30:
        #     break
        # debug for the 23 document:



        try_doc_id = id[sentenceID].split('_')[0]
        try_sent_id=id[sentenceID].split('_')[1]

        # #debug for ....
        # if int(try_doc_id) < 5857:
        #     print("debug.....")
        #     continue


        cur_sent_len = len(cur_sent_text)
        if (cur_sent_len>maxWordssectionlen):
            fileback_w.write(id[sentenceID] + '\t' + allSent[sentenceID])
            continue


        # cur_sent_len = len(cur_sent_text.strip().strip('.').strip().split(' '))
        if (try_doc_id == cur_doc_id) and (constuctlength + cur_sent_len < maxWordssectionlen):


            sent_index_list.append(sentenceID)
            constuctlength = constuctlength + cur_sent_len
            sentencestring = sentencestring + cur_sent_text
            continue
        else:
            backup_index_list = sent_index_list
            backup_sentencestring = sentencestring
            sent_index_list = []
            sentencestring = ''
            if (try_doc_id != cur_doc_id):
                cur_doc_id = try_doc_id

            # record and prepare next batch

            # # debug settting:
            # backup_sentencestring="Fix the problem Best Practices Wakeups are a mechanism in the AlarmManager[] API that lets developers set an alarm to wake up a device at a specified time. Developer\'s app sets a wakeup alarm by calling one of the set (test examples) methods in AlarmManager[] with either the RTC_WAKEUP or ELAPSED_REALTIME_WAKEUP flag! When a wakeup alarm is triggered, the device comes out of low-power mode and holds a partial wake lock while executing the alarm\'s onReceive() or onAlarm() method. "
            #
            # # end debug setting

            backup_sentencestring = backup_sentencestring.replace(' (', '+(').replace(' [', '+[')

            sent_index_list.append(sentenceID)
            constuctlength = cur_sent_len
            sentencestring = sentencestring + cur_sent_text

            print("\n********************************************")
            print("the process sentences:")
            print("the doc id is :" + str(cur_doc_id))
            print("the sentence is : "+str(try_sent_id))
            print(backup_sentencestring)

            # do corference work
            Asentence = nlp.word_tokenize(backup_sentencestring)
            try:
                output = nlp.annotate(backup_sentencestring, properties={'timeout': '50000','annotators': 'dcoref', 'pipelineLanguage': 'en'})
            except :
                for ijx in range(0,len(backup_index_list)):
                    fileback_w.write(id[backup_index_list[ijx]] + '\t' + allSent[backup_index_list[ijx]])
                pass
                continue
            # print('CoReference :', output)
            # nlp.close()
            # print(output)
            if (output is None):
                for ijx in range(0,len(backup_index_list)):
                    fileback_w.write(id[backup_index_list[ijx]] + '\t' + allSent[backup_index_list[ijx]])
                continue

            try:
                newoutput = json.loads(output, strict=False)
            except :
                for ijx in range(0,len(backup_index_list)):
                    fileback_w.write(id[backup_index_list[ijx]] + '\t' + allSent[backup_index_list[ijx]])
                continue

            coreferencelist = newoutput.get("corefs")
            #
            # print(len(coreferencelist))
            # # print(coreferencelist.items())
            # print(coreferencelist.keys())
            # # print(coreferencelist.values())
            newsentence = Asentence



            dotindex = [i for i, x in enumerate(newsentence) if x == '.']
            exclaimindex=[i for i, x in enumerate(newsentence) if x == '!']
            questionindex = [i for i, x in enumerate(newsentence) if x == '?']

            sentenceIndex=dotindex+exclaimindex+questionindex
            sentenceIndex.sort()

            # print(indices[0])
            indexposition=0
            #the . position at the sentences
            # for m in re.finditer(r'\. ', backup_sentencestring):
            #     indexposition = m.start()
            #     listposition.append(indexposition)
            #
            # for m in re.finditer(r'\? ', backup_sentencestring):
            #     indexposition = m.start()
            #     listposition.append(indexposition)
            #
            # for m in re.finditer(r'\! ', backup_sentencestring):
            #     indexposition = m.start()
            #     listposition.append(indexposition)


            # print(newsentence)
            for key in coreferencelist.keys():
                coreferenceitem = coreferencelist.get(key)
                print(len(coreferenceitem))
                if len(coreferenceitem) > 1:
                    for itemindex in range(0, len(coreferenceitem)):
                        if coreferenceitem[itemindex].get("isRepresentativeMention") is True:
                            text1 = coreferenceitem[itemindex].get("text")

                    for itemindex in range(0, len(coreferenceitem)):
                        if coreferenceitem[itemindex].get("isRepresentativeMention") is False:
                            startindex = int(coreferenceitem[itemindex].get("startIndex"))
                            endindex = int(coreferenceitem[itemindex].get("endIndex"))
                            headindex = int(coreferenceitem[itemindex].get("headIndex"))
                            sentnum = int(coreferenceitem[itemindex].get("sentNum"))
                            text2 = coreferenceitem[itemindex].get("text")
                            beginindex = 0
                            if len(text2) < len(text1):

                                if (sentnum-1) <0 or (sentnum-1)>=len(sentenceIndex):
                                    continue
                                beginindex = sentenceIndex[sentnum - 1] + 1

                                changeflage=False

                                for i in range(beginindex + startindex - 1, beginindex + endindex - 1):
                                    if (i>=0 and i<len(newsentence)):
                                        changeflage=True
                                        newsentence[i] = ""
                                if changeflage:
                                    newsentence[beginindex + startindex - 1] = text1

            wholenewsentence = ' '.join(newsentence)
            wholenewsentence = wholenewsentence.replace(' + -LRB-', ' (').replace(' + -LSB-', ' [') \
                .replace(' -LRB-', '(').replace(' -LSB-', '[').replace('-LRB-', '(').replace('-LSB-', '[').replace('-RRB-', ')').replace('-RSB-', ']').replace('`` ','"').replace(' \'\'','"').replace(' \'s', '\'s') \
                .replace(' .', '. ').replace(' !', '! ').replace(' ?', '? ').replace('  ', ' ')


            wholenewsentence=wholenewsentence.replace('( )','()').replace('( ','(').replace(' )',')')
            wholenewsentence = wholenewsentence.replace('[ ]', '[]').replace('[ ', '[').replace(' ]', ']')
            print(wholenewsentence)

            # assign new sentence back
            # wholenewsentencelist = wholenewsentence.split('. ')
            listposition=[]
            for m in re.finditer(r'\. ', wholenewsentence):
                position = m.start()
                listposition.append((position,'. '))

            for m in re.finditer(r'\? ', wholenewsentence):
                position = m.start()
                listposition.append((position,'? '))

            for m in re.finditer(r'\! ', wholenewsentence):
                position = m.start()
                listposition.append((position,'! '))
            # sort it
            listposition.sort(key=operator.itemgetter(0))
            # print(listposition)

            myi=0
            oneNewSen=[]
            startp=0
            endp=0
            for myi in range(0,len(backup_index_list)):
                if (myi>=len(listposition)):
                    continue
                print(listposition[myi])
                endp=listposition[myi][0]+2
                # print(listposition)
                # print(len(wholenewsentence))
                # print(startp, endp)


                allSent[backup_index_list[myi]] = wholenewsentence[startp:endp]+'\n'
                fileback_w.write(id[backup_index_list[myi]] + '\t' + wholenewsentence[startp:endp]+'\n')
                startp = endp


    # #   debug  100 sentences
    #     if (sentenceID > 100):
    #         break

    fileback_w.close()
    return allSent






# def main():
    # first you must running the stanford coreNLP programe at system termimal :
    # first, for unlimited core dump run: ulimit -c unlimited
    # second, run: java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000




# nlp = StanfordCoreNLP('http://127.0.0.1', port=9000)
my_allSent = read()
id = my_allSent[0]
allSent = my_allSent[1]
print(len(id))
print(len(allSent))
maxWordssectionlen = 400


# do coreference work
allSent=doCoreferenceWork()

writeCorefenence(id,allSent)

# # makeup all entities to qualifiedname (just for one time )
# allSent=makeupallqualifiedname(allSent,id)

# do extract relation work
gen_rel()


# if __name__ == '__main__':
#     nlp = StanfordCoreNLP('http://127.0.0.1', port=9000)
#     my_allSent = read()
#     id = my_allSent[0]
#     allSent = my_allSent[1]
#     print(len(id))
#     print(len(allSent))
#     maxWordssectionlen = 100
#     main()
