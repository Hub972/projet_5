-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: project5
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Current Database: `project5`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `project5` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project5`;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `generic_name` varchar(150) DEFAULT NULL,
  `bar_code` bigint(20) DEFAULT NULL,
  `cat` varchar(10) DEFAULT NULL,
  `alter_code` bigint(20) DEFAULT NULL,
  `is_subtitute` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Confiture abricot','Confiture abricot',3324498000746,'2',3760121210661,0),(2,'Confiture pomme au calvados','Confiture pomme au calvados',3324498002542,'2',3396745001110,0),(3,'Yaourt Brassé','Yaourt brassé nature',26065250,'2',3222474051228,0),(4,'Tomates Farcies et Riz Long Blanc','Tomates Farcies et Riz Long Blanc',3258561470641,'1',3248830690214,0),(5,'Crème fraîche légère épaisse','Crème fraîche légère épaisse',3700311861334,'1',3382322220005,0),(6,'Pavé de Saumon ASC','Pavé de Saumon ',40884004,'1',3270160741939,0),(7,'Rillettes de Poulet Rôti en Cocotte','Rillettes de Poulet Rôti',3560070507832,'1',3250391554508,0),(8,'Cidre Brut','Cidre Brut',3186630000973,'3',20466268,0),(9,'Nectar Multifruits','Jus Multifruit',3270190128410,'3',3254691586054,0),(10,'Nuggets de Poulet','Préparation à base de viande de poulet et de dinde traitée en salaison                         reconstituée (60%)',3222472621218,'1',3422210446190,0);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-06 12:49:03
