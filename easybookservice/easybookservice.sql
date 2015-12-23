-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: easybookservice
-- ------------------------------------------------------
-- Server version	5.7.9-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `advice_advice`
--

DROP TABLE IF EXISTS `advice_advice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `advice_advice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recommend` varchar(10) NOT NULL,
  `treatmentEffect` varchar(10) NOT NULL,
  `disease` varchar(30) NOT NULL,
  `doctor` varchar(10) NOT NULL,
  `docAttitude` varchar(10) NOT NULL,
  `dep` varchar(10) NOT NULL,
  `context` varchar(300) NOT NULL,
  `tel` varchar(50) NOT NULL,
  `hos_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `advice_advice_hos_id_299c781_fk_hospital_hospital_id` (`hos_id`),
  KEY `advice_advice_user_id_53a2a215_fk_users_users_id` (`user_id`),
  CONSTRAINT `advice_advice_hos_id_299c781_fk_hospital_hospital_id` FOREIGN KEY (`hos_id`) REFERENCES `hospital_hospital` (`id`),
  CONSTRAINT `advice_advice_user_id_53a2a215_fk_users_users_id` FOREIGN KEY (`user_id`) REFERENCES `users_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `books_books`
--

DROP TABLE IF EXISTS `books_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hospital` varchar(20) NOT NULL,
  `depart` varchar(10) NOT NULL,
  `docprof` varchar(10) NOT NULL,
  `hosAddr` varchar(40) NOT NULL,
  `time` varchar(10) NOT NULL,
  `patientName` varchar(10) NOT NULL,
  `patientID` varchar(20) NOT NULL,
  `tel` varchar(50) NOT NULL,
  `bookID` varchar(500) NOT NULL,
  `doc_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_books_doc_id_708f5073_fk_doctor_doctor_id` (`doc_id`),
  KEY `books_books_user_id_41fcf56b_fk_users_users_id` (`user_id`),
  CONSTRAINT `books_books_doc_id_708f5073_fk_doctor_doctor_id` FOREIGN KEY (`doc_id`) REFERENCES `doctor_doctor` (`id`),
  CONSTRAINT `books_books_user_id_41fcf56b_fk_users_users_id` FOREIGN KEY (`user_id`) REFERENCES `users_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `depart_depart`
--

DROP TABLE IF EXISTS `depart_depart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `depart_depart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `departid` varchar(10) NOT NULL,
  `departName` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `depart_depart_hos`
--

DROP TABLE IF EXISTS `depart_depart_hos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `depart_depart_hos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `depart_id` int(11) NOT NULL,
  `hospital_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `depart_id` (`depart_id`,`hospital_id`),
  KEY `depart_depart_hos_hospital_id_1ed02c07_fk_hospital_hospital_id` (`hospital_id`),
  CONSTRAINT `depart_depart_hos_depart_id_2f54d51f_fk_depart_depart_id` FOREIGN KEY (`depart_id`) REFERENCES `depart_depart` (`id`),
  CONSTRAINT `depart_depart_hos_hospital_id_1ed02c07_fk_hospital_hospital_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospital_hospital` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `disease_disease`
--

DROP TABLE IF EXISTS `disease_disease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_disease` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `diseaseid` varchar(10) NOT NULL,
  `disename` varchar(50) NOT NULL,
  `disenamel` varchar(100) NOT NULL,
  `diseSym` longtext NOT NULL,
  `godepart` varchar(30) NOT NULL,
  `spread` varchar(30) NOT NULL,
  `position` varchar(50) NOT NULL,
  `highrisk` varchar(50) NOT NULL,
  `method` varchar(50) NOT NULL,
  `intro` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `disease_disease_dep`
--

DROP TABLE IF EXISTS `disease_disease_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_disease_dep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `disease_id` int(11) NOT NULL,
  `depart_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `disease_id` (`disease_id`,`depart_id`),
  KEY `disease_disease_dep_depart_id_31d0652a_fk_depart_depart_id` (`depart_id`),
  CONSTRAINT `disease_disease_dep_depart_id_31d0652a_fk_depart_depart_id` FOREIGN KEY (`depart_id`) REFERENCES `depart_depart` (`id`),
  CONSTRAINT `disease_disease_dep_disease_id_6a5e7b45_fk_disease_disease_id` FOREIGN KEY (`disease_id`) REFERENCES `disease_disease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `doctor_doctor`
--

DROP TABLE IF EXISTS `doctor_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor_doctor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doctorid` varchar(10) NOT NULL,
  `docname` varchar(10) NOT NULL,
  `prof` varchar(20) NOT NULL,
  `hosp` varchar(30) NOT NULL,
  `depa` varchar(20) NOT NULL,
  `goodat` longtext NOT NULL,
  `time` varchar(15) NOT NULL,
  `exp` longtext NOT NULL,
  `dep_id` int(11) NOT NULL,
  `hos_id` int(11) NOT NULL,
  `docmail` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `docmail` (`docmail`),
  KEY `doctor_doctor_dep_id_1cc35bf2_fk_depart_depart_id` (`dep_id`),
  KEY `doctor_doctor_hos_id_68db361b_fk_hospital_hospital_id` (`hos_id`),
  CONSTRAINT `doctor_doctor_dep_id_1cc35bf2_fk_depart_depart_id` FOREIGN KEY (`dep_id`) REFERENCES `depart_depart` (`id`),
  CONSTRAINT `doctor_doctor_hos_id_68db361b_fk_hospital_hospital_id` FOREIGN KEY (`hos_id`) REFERENCES `hospital_hospital` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hosclass_hosclass`
--

DROP TABLE IF EXISTS `hosclass_hosclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosclass_hosclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hosclassid` varchar(10) NOT NULL,
  `hosclass` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hospital_hospital`
--

DROP TABLE IF EXISTS `hospital_hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hospital_hospital` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hospitalid` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `level` varchar(10) NOT NULL,
  `quality` varchar(10) NOT NULL,
  `classes` varchar(10) NOT NULL,
  `insurance` varchar(10) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `address` varchar(200) NOT NULL,
  `service` varchar(60) NOT NULL,
  `summary` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hostype_hostype`
--

DROP TABLE IF EXISTS `hostype_hostype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostype_hostype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostypeid` varchar(10) NOT NULL,
  `hostype` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `issue_issue`
--

DROP TABLE IF EXISTS `issue_issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue_issue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `issueid` varchar(5) NOT NULL,
  `issuename` varchar(10) NOT NULL,
  `issuecontent` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `news_news`
--

DROP TABLE IF EXISTS `news_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `newsid` varchar(10) NOT NULL,
  `title` varchar(30) NOT NULL,
  `subtitle` varchar(50) NOT NULL,
  `article` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prof_prof`
--

DROP TABLE IF EXISTS `prof_prof`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prof_prof` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profid` varchar(10) NOT NULL,
  `profName` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users_users`
--

DROP TABLE IF EXISTS `users_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-21 16:19:10
