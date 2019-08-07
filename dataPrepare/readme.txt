1. collecting html file to filenamelist  \ content to doc

    1.1 gethtmlcontent.py

    1.2 1.5article2sentOnly.py  sentences with deliminator like : '.' '?' '!'

2. collecting Entities two way:

    first, collecting from file :
        pureIDTag.py (SANER2018)
        dataPrepare/generateSentencesTable.py(ICSME)
        dataPrepare/generateRelationRawTable.py(ICSME)

    second, use fudan api_class/api_library/api_method/api_parameter :

        /dataPrepare/collectEntities.py (ICSME2018)

3. coreference and pos and get relation( three POS tuples )
   3.1 run coreNLP (timeout must long enough) in the command line :

   java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 50000

    3.2 run coreference and chunking and selecting POS relation
    NPVPNP_chunking/sentence_chunking_dep_for_tempdata.py

4. select relation with Entities
   write into database:
   /dataPrepare/P2GetEntitiesRelationICSME.py

5. select warnings sentences with define patterns:
   dataPrepare/P3GenRelatedWarningICSME.py

6. generate the recommending relation / entities / warnings
  P4GenRecommandWarningICSME_multi.py




