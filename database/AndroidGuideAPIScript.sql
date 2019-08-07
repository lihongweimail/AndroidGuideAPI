/*
 Navicat Premium Data Transfer

 Source Server         : 本地MySQL
 Source Server Type    : MySQL
 Source Server Version : 50712
 Source Host           : localhost:3306
 Source Schema         : AndroidGuideAPI

 Target Server Type    : MySQL
 Target Server Version : 50712
 File Encoding         : 65001

 Date: 17/10/2017 07:46:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Entities
-- ----------------------------
DROP TABLE IF EXISTS `Entities`;
CREATE TABLE `Entities` (
  `id` int(11) NOT NULL,
  `EntityName` varchar(1000) DEFAULT NULL,
  `EntitySection` varchar(1000) DEFAULT NULL,
  `EntityURL` varchar(1000) DEFAULT NULL,
  `EntityParent` varchar(1000) DEFAULT NULL,
  `EntityType` varchar(200) DEFAULT NULL,
  `EntityOriginal` varchar(1000) DEFAULT NULL,
  `URLid` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='1.entities / API list';

-- ----------------------------
-- Table structure for EntitiesRelation
-- ----------------------------
DROP TABLE IF EXISTS `EntitiesRelation`;
CREATE TABLE `EntitiesRelation` (
  `id` int(11) NOT NULL,
  `EntityOne` varchar(1000) DEFAULT NULL,
  `Relation` varchar(1000) DEFAULT NULL,
  `EntityTwo` varchar(1000) DEFAULT NULL,
  `RelationSection` varchar(1000) DEFAULT NULL,
  `RelationURL` varchar(1000) DEFAULT NULL,
  `RelationText` varchar(3000) DEFAULT NULL,
  `URLid` varchar(200) DEFAULT NULL,
  `Sentenceid` varchar(200) DEFAULT NULL,
  `Relationid` varchar(200) DEFAULT NULL,
  `POSinfo` varchar(1000) DEFAULT NULL,
  `SectionType` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='2.textToTriples or other Relation expression';

-- ----------------------------
-- Table structure for RecommandWarning
-- ----------------------------
DROP TABLE IF EXISTS `RecommandWarning`;
CREATE TABLE `RecommandWarning` (
  `id` int(11) NOT NULL,
  `WarningIndex` int(11) DEFAULT NULL,
  `EntitiesIndex` int(11) DEFAULT NULL,
  `RelationIndex` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='4. Warnings / rules and API entities relation';

-- ----------------------------
-- Table structure for Warning
-- ----------------------------
DROP TABLE IF EXISTS `Warning`;
CREATE TABLE `Warning` (
  `id` int(11) NOT NULL,
  `WarningTag` varchar(200) DEFAULT NULL,
  `WarningSection` varchar(1000) DEFAULT NULL,
  `WarningText` varchar(3000) DEFAULT NULL,
  `WarningType` varchar(200) DEFAULT NULL,
  `WarningURL` varchar(1000) DEFAULT NULL,
  `WarningSentenceId` varchar(200) DEFAULT NULL,
  `Relationid` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='3.Warning or rules';

-- ----------------------------
-- Table structure for api_class
-- ----------------------------
DROP TABLE IF EXISTS `api_class`;
CREATE TABLE `api_class` (
  `api_class_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `description` text,
  `comment` varchar(255) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  `extend_class` int(11) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `package_id` int(11) DEFAULT NULL,
  `doc_website` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`api_class_id`),
  KEY `package` (`package_id`),
  KEY `name` (`name`,`package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=83024 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for api_library
-- ----------------------------
DROP TABLE IF EXISTS `api_library`;
CREATE TABLE `api_library` (
  `library_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `orgnization` varchar(255) DEFAULT NULL,
  `introduction` varchar(255) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `jdk_version` varchar(45) DEFAULT NULL,
  `pom_file` varchar(45) DEFAULT NULL,
  `license` varchar(255) DEFAULT NULL,
  `doc_website` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`library_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for api_method
-- ----------------------------
DROP TABLE IF EXISTS `api_method`;
CREATE TABLE `api_method` (
  `api_method_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `annotation` varchar(255) DEFAULT NULL,
  `return_class` int(11) DEFAULT NULL,
  `return_string` varchar(255) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  `is_static` tinyint(1) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`api_method_id`),
  KEY `methodName` (`name`),
  KEY `classId` (`class_id`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=616736 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for api_package
-- ----------------------------
DROP TABLE IF EXISTS `api_package`;
CREATE TABLE `api_package` (
  `api_package_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  `description` text,
  `doc_website` varchar(255) DEFAULT NULL,
  `library_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`api_package_id`),
  KEY `package` (`api_package_id`,`library_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4563 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for api_package_list
-- ----------------------------
DROP TABLE IF EXISTS `api_package_list`;
CREATE TABLE `api_package_list` (
  `package_name` varchar(255) NOT NULL,
  `package_url` varchar(255) DEFAULT NULL,
  `api_level` varchar(255) DEFAULT NULL,
  `package_des` varchar(1024) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=289 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for api_parameter
-- ----------------------------
DROP TABLE IF EXISTS `api_parameter`;
CREATE TABLE `api_parameter` (
  `parameter_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `method_id` int(11) DEFAULT NULL,
  `type_class` int(11) DEFAULT NULL,
  `type_string` varchar(255) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`parameter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1072974 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for entity
-- ----------------------------
DROP TABLE IF EXISTS `entity`;
CREATE TABLE `entity` (
  `id` int(11) NOT NULL,
  `entity_one` varchar(200) DEFAULT NULL,
  `relation` varchar(200) DEFAULT NULL,
  `entity_two` varchar(200) DEFAULT NULL,
  `section` varchar(200) DEFAULT NULL,
  `URL` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_class
-- ----------------------------
DROP TABLE IF EXISTS `jdk_class`;
CREATE TABLE `jdk_class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `description` text,
  `comment` varchar(255) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  `extend_class` int(11) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `doc_website` varchar(255) DEFAULT NULL,
  `package_id` int(11) DEFAULT NULL,
  `handled_description` text,
  `conf_description` text,
  `detail_description` longtext,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12990 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_class_see_also
-- ----------------------------
DROP TABLE IF EXISTS `jdk_class_see_also`;
CREATE TABLE `jdk_class_see_also` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `see_also_title` text,
  `see_also_website` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4570 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_exception
-- ----------------------------
DROP TABLE IF EXISTS `jdk_exception`;
CREATE TABLE `jdk_exception` (
  `exception_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `method_id` int(11) DEFAULT NULL,
  `description` text,
  `handled_description` text,
  `conf_description` text,
  PRIMARY KEY (`exception_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19573 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_library
-- ----------------------------
DROP TABLE IF EXISTS `jdk_library`;
CREATE TABLE `jdk_library` (
  `library_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `organization` varchar(255) DEFAULT NULL,
  `jdk_version` varchar(45) DEFAULT NULL,
  `doc_website` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`library_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_method
-- ----------------------------
DROP TABLE IF EXISTS `jdk_method`;
CREATE TABLE `jdk_method` (
  `method_id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `name` text,
  `full_declaration` text,
  `return_type` varchar(255) DEFAULT NULL,
  `return_string` text,
  `description` text,
  `first_version` varchar(45) DEFAULT NULL,
  `is_static` tinyint(1) DEFAULT NULL,
  `override` text,
  `specified_by` text,
  `class_id` int(11) DEFAULT NULL,
  `handled_description` text,
  `handled_return_string` text,
  `handled_full_declaration` text,
  `conf_description` text,
  PRIMARY KEY (`method_id`),
  KEY `class_id_index` (`class_id`),
  FULLTEXT KEY `name_index` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=89398 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_method_see_also
-- ----------------------------
DROP TABLE IF EXISTS `jdk_method_see_also`;
CREATE TABLE `jdk_method_see_also` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `see_also_title` text,
  `see_also_website` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `method_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22104 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_package
-- ----------------------------
DROP TABLE IF EXISTS `jdk_package`;
CREATE TABLE `jdk_package` (
  `package_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `first_version` varchar(45) DEFAULT NULL,
  `description` text,
  `doc_website` varchar(255) DEFAULT NULL,
  `library_id` int(11) DEFAULT NULL,
  `handled_description` text,
  `conf_description` text,
  `detail_description` longtext,
  PRIMARY KEY (`package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=796 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jdk_parameter
-- ----------------------------
DROP TABLE IF EXISTS `jdk_parameter`;
CREATE TABLE `jdk_parameter` (
  `parameter_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `method_id` int(11) DEFAULT NULL,
  `type_class` int(11) DEFAULT NULL,
  `type_string` varchar(255) DEFAULT NULL,
  `description` text,
  `handled_description` text,
  `conf_description` text,
  PRIMARY KEY (`parameter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34913 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
