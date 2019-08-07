Android API related claw database:



database Name: AndroidGuideAPI

tables:
(entities, )

1. Entities:

CREATE TABLE `entities`  (
  `id` int(11) NOT NULL,
  `EntityName` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntitySection` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntityURL` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntityParent` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntityType` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntityOriginal` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `URLid` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `QualifiedName` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `Entities_id_index`(`id`) USING BTREE,
  INDEX `Entities_EntityName_index`(`EntityName`) USING BTREE,
  INDEX `Entities_EntityType_index`(`EntityType`) USING BTREE,
  INDEX `Entities_EntityURL_index`(`EntityURL`) USING BTREE,
  INDEX `Entities_QualifiedName_index`(`QualifiedName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '1.entities / API list' ROW_FORMAT = Dynamic;


  `id` : API entities id ,
  `EntityName`     :  API entities's name ,
  `EntitySection`  : the position where the entity is located in a section of the web page file  ,
  `EntityURL`      :  the reference web page URL of this API entity (may with the anchor of this entity) ,
  `EntityParent`   :  the parent of API entity if it is exist or directly up level knot locating in the hierarchical,
  `EntityType`     : the name of programming element which is naming for this API entity, like: package , class , method, parameter, field and so on ,
  `EntityOriginal` :  original information when the tool had done on clawing or locating this API entity in the website ,
  `URLid`          : this current web page's URL which contains this API entity,
  `QualifiedName`  : this API entity's qualified name .


2. entitiesrelation

  CREATE TABLE `entitiesrelation`  (
  `id` int(11) NOT NULL,
  `EntityOne` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Relation` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EntityTwo` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RelationSection` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RelationURL` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RelationText` varchar(3000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `URLid` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Sentenceid` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Relationid` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `POSinfo` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SectionType` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `EntitiesRelation_EntityTwo_index`(`EntityTwo`) USING BTREE,
  INDEX `EntitiesRelation_Sentenceid_index`(`Sentenceid`) USING BTREE,
  INDEX `EntitiesRelation_id_index`(`id`) USING BTREE,
  INDEX `EntitiesRelation_EntityOne_index`(`EntityOne`) USING BTREE,
  INDEX `EntitiesRelation_URLid_index`(`URLid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '2.textToTriples or other Relation expression' ROW_FORMAT = Dynamic;





3.Warning

CREATE TABLE `warning`  (
  `id` int(11) NOT NULL,
  `WarningTag` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `WarningSection` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `WarningText` varchar(3000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `WarningType` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `WarningURL` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `WarningSentenceId` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Relationid` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `Warning_id_index`(`id`) USING BTREE,
  INDEX `Warning_Relationid_index`(`Relationid`) USING BTREE,
  INDEX `Warning_WarningSentenceId_index`(`WarningSentenceId`) USING BTREE,
  INDEX `Warning_WarningTag_index`(`WarningTag`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '3.Warning or rules' ROW_FORMAT = Dynamic;


4.  linkentitysnew
CREATE TABLE `linkentitysnew`  (
  `id` int(11) NOT NULL,
  `entityid` int(11) NULL DEFAULT NULL,
  `relationid` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `linkEntitys_entityid_index`(`entityid`) USING BTREE,
  INDEX `linkEntitys_id_index`(`id`) USING BTREE,
  INDEX `linkEntitys_relationid_index`(`relationid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;



5. recommandwarningx
（原本使用 recommendwarning  但是单词敲错了，所以被定义为recommandwarningx）

CREATE TABLE `recommandwarningx`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `WarningIndex` int(11) NULL DEFAULT NULL,
  `EntitiesIndex` int(11) NULL DEFAULT NULL,
  `RelationIndex` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `RecommandWarningx_EntitiesIndex_index`(`EntitiesIndex`) USING BTREE,
  INDEX `RecommandWarningx_RelationIndex_index`(`RelationIndex`) USING BTREE,
  INDEX `RecommandWarningx_WarningIndex_index`(`WarningIndex`) USING BTREE,
  INDEX `RecommandWarningx_id_index`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3126103 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '4. Warnings / rules and API entities relation' ROW_FORMAT = Dynamic;


