-- MySQL dump 10.13  Distrib 5.6.26, for Linux (x86_64)
--
-- Host: localhost    Database: admin
-- ------------------------------------------------------
-- Server version	5.6.26

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

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
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add search_data',7,'add_search_data'),(20,'Can change search_data',7,'change_search_data'),(21,'Can delete search_data',7,'delete_search_data');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

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
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

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
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

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
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'visualization','search_data');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-10-29 09:21:02.242884'),(2,'auth','0001_initial','2015-10-29 09:21:06.940923'),(3,'admin','0001_initial','2015-10-29 09:21:08.135070'),(4,'contenttypes','0002_remove_content_type_name','2015-10-29 09:21:09.022019'),(5,'auth','0002_alter_permission_name_max_length','2015-10-29 09:21:09.503837'),(6,'auth','0003_alter_user_email_max_length','2015-10-29 09:21:09.992355'),(7,'auth','0004_alter_user_username_opts','2015-10-29 09:21:10.026119'),(8,'auth','0005_alter_user_last_login_null','2015-10-29 09:21:10.443995'),(9,'auth','0006_require_contenttypes_0002','2015-10-29 09:21:10.486601'),(10,'sessions','0001_initial','2015-10-29 09:21:10.921857'),(11,'visualization','0001_initial','2015-10-29 09:21:11.125607'),(12,'visualization','0002_auto_20151030_0455','2015-10-30 04:55:38.033960'),(13,'visualization','0003_auto_20151030_0500','2015-10-30 05:00:59.107211'),(14,'visualization','0004_search_data_pic_type','2015-11-02 10:56:30.549594'),(15,'visualization','0005_search_data_id_in_dashboard','2015-11-03 06:36:31.876519'),(16,'visualization','0006_auto_20151103_1743','2015-11-03 09:43:35.790633');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visualization_search_data`
--

DROP TABLE IF EXISTS `visualization_search_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `visualization_search_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monitor_name` varchar(50) NOT NULL,
  `index` varchar(50) NOT NULL,
  `query` varchar(50) DEFAULT NULL,
  `fields` varchar(500) DEFAULT NULL,
  `field` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `sub_fields` varchar(500) DEFAULT NULL,
  `mothod_type` varchar(20) DEFAULT NULL,
  `pic_type` varchar(20),
  `num_dashboard` varchar(2),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visualization_search_data`
--

LOCK TABLES `visualization_search_data` WRITE;
/*!40000 ALTER TABLE `visualization_search_data` DISABLE KEYS */;
INSERT INTO `visualization_search_data` VALUES (1,'haproxy backend流量','haproxy',NULL,NULL,'byte',NULL,NULL,'backend2:haproxy2;backend2:haproxy3;backend2:haproxy4;backend2:haproxy5','sub_query','line',NULL),(2,'haproxy http发送字节数','haproxy',NULL,NULL,'byte','flow',NULL,NULL,'per_sum','line',NULL),(3,'haproxy http状态码统计','haproxy',NULL,NULL,'http_status',NULL,15,NULL,'some_top','line',NULL),(4,'haproxy pv','haproxy','NOT request_uri:png|gif|jpeg|jpg|media|static|css',NULL,NULL,'pv',NULL,NULL,'count','line',NULL),(5,'haproxy uv','haproxy',NULL,NULL,'src_ip','uv',NULL,NULL,'cardinality','line',NULL),(6,'haproxy 模块1的访问概率','haproxy',NULL,NULL,'request_uri_1',NULL,10,NULL,'some_top','column',NULL),(7,'haproxy 模块2的访问概率','haproxy',NULL,NULL,'request_uri_2',NULL,10,NULL,'some_top','column',NULL),(8,'haproxy 流量','haproxy',NULL,NULL,'byte',NULL,NULL,NULL,'sum','line',NULL),(9,'mysql erp-172.16.1.34:3306 qps','mysql','type:qps AND type:172.16.1.34','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(11,'mysql erp-172.16.1.34:3306 slowquerytime','mysql','type:172.16.1.34','query_time',NULL,NULL,NULL,NULL,'gen','line',NULL),(12,'mysql erp-172.16.1.45:3306 qps','mysql','type:qps AND type:172.16.1.45','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(13,'mysql erp-172.16.1.45:3306 slowquerytime','mysql','type:172.16.1.45','query_time',NULL,NULL,NULL,NULL,'gen','line',NULL),(14,'mysql erp-172.16.1.62:3306 qps','mysql','type:qps AND type:172.16.1.62','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line','22'),(15,'mysql erp-172.16.1.62:3306 slowquerytime','mysql','type:172.16.1.62','query_time',NULL,NULL,NULL,NULL,'gen','line','21'),(16,'mysql qy-172.16.1.41:3306 qps','mysql','type:qps AND type:172.16.1.41','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(17,'mysql qy-172.16.1.41:3306 slowquerytime','mysql','type:172.16.1.41','query_time',NULL,NULL,NULL,NULL,'gen','line',NULL),(18,'mysql qy-172.16.1.51:3306 qps','mysql','type:qps AND type:172.16.1.51','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(19,'mysql zp-172.16.1.22:3306 qps','mysql','type:qps AND type:172.16.1.22','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(20,'mysql zp-172.16.1.32:3306 qps','mysql','type:qps AND type:172.16.1.32','insert;delete;update;select',NULL,NULL,NULL,NULL,'sub_sum','line',NULL),(21,'nginx http发送字节数统计','nginx',NULL,NULL,'sent_bytes','flow',NULL,NULL,'per_sum','line','23'),(22,'nginx http响应时间统计','nginx','NOT request_uri:png|gif|jpeg|jpg|media|static|css','request_time',NULL,NULL,NULL,NULL,'gen','line','11'),(23,'nginx http状态码统计','nginx',NULL,NULL,'http_status',NULL,15,NULL,'some_top','column',NULL),(24,'nginx pv统计','nginx','NOT request_uri:png|gif|jpeg|jpg|media|static|css',NULL,NULL,'pv',NULL,NULL,'count','line',NULL),(25,'nginx uv统计','nginx',NULL,NULL,'clientip','uv',NULL,NULL,'cardinality','line','12'),(26,'rabbitmq erp-172.16.1.33','rabbitmq','type:172.16.1.33','rate',NULL,NULL,NULL,NULL,'gen','line','13'),(27,'rabbitmq qy-172.16.1.14','rabbitmq','type:172.16.1.14','rate',NULL,NULL,NULL,NULL,'gen','line','14'),(29,'商品总数','testindex','testquery','count',NULL,NULL,NULL,NULL,'gen','line',NULL),(30,'订单数','testindex','testquery','count',NULL,NULL,NULL,NULL,'gen','line',NULL),(31,'总成交金额','testindex','testquery','count',NULL,NULL,NULL,NULL,'gen','column',NULL),(32,'DAU/MAU/PV','testindex','testquery','DAU;MAU;PV',NULL,NULL,NULL,NULL,'gen','line',NULL),(33,'某业务信息','testindex','testquery','bussnis_data;',NULL,NULL,NULL,NULL,'gen','column',NULL);
/*!40000 ALTER TABLE `visualization_search_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-10 10:16:13
