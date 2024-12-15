-- MySQL dump 10.13  Distrib 9.1.0, for macos14 (arm64)
--
-- Host: localhost    Database: FastFood
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `combos`
--

DROP TABLE IF EXISTS `combos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `combos` (
  `comboID` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `cost` float NOT NULL,
  `calories` float DEFAULT NULL,
  `restrauntID` int NOT NULL,
  PRIMARY KEY (`comboID`),
  KEY `restrauntID` (`restrauntID`),
  CONSTRAINT `combos_ibfk_1` FOREIGN KEY (`restrauntID`) REFERENCES `restraunts` (`restrauntID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `combos`
--

LOCK TABLES `combos` WRITE;
/*!40000 ALTER TABLE `combos` DISABLE KEYS */;
INSERT INTO `combos` VALUES (1,'number 1',5.5,600,1),(2,'number 2',6,650,1),(3,'number 3',7,700,1),(4,'happy meal',5,400,1),(5,'number 1',6,650,2),(6,'number 2',7,700,2),(7,'number 3',8,750,2),(8,'munchie meal',9,850,2),(9,'number 1',5,600,3),(10,'number 2',5.5,650,3),(11,'the box',9,1050,4);
/*!40000 ALTER TABLE `combos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customerID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` text NOT NULL,
  `firstName` text NOT NULL,
  `lastName` text NOT NULL,
  `points` int DEFAULT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'jSnow','ghost','John','Snow',2),(2,'wizard1','hedwig','Harry','Potter',1),(3,'reaper','virginia','Darrow','O-Lykos',0),(4,'barrelz4lyfe','zurfing','Chicken','Joe',0);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_combo`
--

DROP TABLE IF EXISTS `item_combo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_combo` (
  `comboID` int NOT NULL,
  `itemID` int NOT NULL,
  KEY `comboID` (`comboID`),
  KEY `itemID` (`itemID`),
  CONSTRAINT `item_combo_ibfk_1` FOREIGN KEY (`comboID`) REFERENCES `combos` (`comboID`),
  CONSTRAINT `item_combo_ibfk_2` FOREIGN KEY (`itemID`) REFERENCES `items` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_combo`
--

LOCK TABLES `item_combo` WRITE;
/*!40000 ALTER TABLE `item_combo` DISABLE KEYS */;
INSERT INTO `item_combo` VALUES (1,2),(1,3),(1,8),(2,1),(2,3),(2,8),(3,5),(3,3),(3,8),(4,4),(4,3),(5,10),(5,12),(5,16),(6,9),(6,12),(6,16),(7,11),(7,12),(7,16),(8,10),(8,12),(8,16),(8,14),(8,14),(9,18),(9,19),(9,20),(10,17),(10,19),(10,20),(11,22),(11,23),(11,24),(11,26),(11,27);
/*!40000 ALTER TABLE `item_combo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `itemID` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `cost` float NOT NULL,
  `calories` float NOT NULL,
  `restrauntID` int NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `restrauntID` (`restrauntID`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`restrauntID`) REFERENCES `restraunts` (`restrauntID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'cheeseburger',3.5,300,1),(2,'hamburger',3,250,1),(3,'fries',1.5,200,1),(4,'chicken nuggets',4,200,1),(5,'chicken sandwich',4.5,350,1),(6,'ice cream cone',1.5,100,1),(7,'milkshake',2.5,300,1),(8,'soda',1,150,1),(9,'cheeseburger',4.5,350,2),(10,'hamburger',4,300,2),(11,'chicken sandwich',4.5,400,2),(12,'fries',2.5,200,2),(13,'curly fries',3,250,2),(14,'taco',0.5,100,2),(15,'milkshake',3,250,2),(16,'soda',1,150,2),(17,'cheeseburger',2.5,300,3),(18,'hamburger',2,250,3),(19,'fries',2,200,3),(20,'soda',1.5,150,3),(21,'milkshake',2,200,3),(22,'taco',1.5,150,4),(23,'burrito',4,350,4),(24,'chips and queso',2,200,4),(25,'ice cream cone',0.5,100,4),(26,'loco taco',2,200,4),(27,'soda',1,150,4);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `managers`
--

DROP TABLE IF EXISTS `managers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `managers` (
  `managerID` int NOT NULL AUTO_INCREMENT,
  `password` text NOT NULL,
  `restrauntID` int NOT NULL,
  PRIMARY KEY (`managerID`),
  KEY `restrauntID` (`restrauntID`),
  CONSTRAINT `managers_ibfk_1` FOREIGN KEY (`restrauntID`) REFERENCES `restraunts` (`restrauntID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managers`
--

LOCK TABLES `managers` WRITE;
/*!40000 ALTER TABLE `managers` DISABLE KEYS */;
INSERT INTO `managers` VALUES (1,'mcds',1),(2,'jbox',2),(3,'inout',3),(4,'tbell',4);
/*!40000 ALTER TABLE `managers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_menu`
--

DROP TABLE IF EXISTS `order_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_menu` (
  `orderID` int NOT NULL,
  `comboID` int DEFAULT NULL,
  `itemID` int DEFAULT NULL,
  KEY `orderID` (`orderID`),
  KEY `comboID` (`comboID`),
  KEY `itemID` (`itemID`),
  CONSTRAINT `order_menu_ibfk_1` FOREIGN KEY (`orderID`) REFERENCES `orders` (`orderID`),
  CONSTRAINT `order_menu_ibfk_2` FOREIGN KEY (`comboID`) REFERENCES `combos` (`comboID`),
  CONSTRAINT `order_menu_ibfk_3` FOREIGN KEY (`itemID`) REFERENCES `items` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_menu`
--

LOCK TABLES `order_menu` WRITE;
/*!40000 ALTER TABLE `order_menu` DISABLE KEYS */;
INSERT INTO `order_menu` VALUES (1,1,NULL),(1,4,NULL),(2,8,NULL),(2,NULL,15),(3,9,NULL),(4,11,NULL);
/*!40000 ALTER TABLE `order_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderID` int NOT NULL AUTO_INCREMENT,
  `cost` float DEFAULT NULL,
  `calories` float DEFAULT NULL,
  `customerID` int NOT NULL,
  `restrauntID` int NOT NULL,
  PRIMARY KEY (`orderID`),
  KEY `customerID` (`customerID`),
  KEY `restrauntID` (`restrauntID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customers` (`customerID`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`restrauntID`) REFERENCES `restraunts` (`restrauntID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,10.5,1000,1,1),(2,12,1100,1,2),(3,5,600,2,3),(4,9,1050,2,4),(5,0,0,3,1),(6,0,0,3,2),(7,0,0,4,3),(8,0,0,4,4);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restraunts`
--

DROP TABLE IF EXISTS `restraunts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restraunts` (
  `restrauntID` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `rating` float DEFAULT NULL,
  `location` text,
  PRIMARY KEY (`restrauntID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restraunts`
--

LOCK TABLES `restraunts` WRITE;
/*!40000 ALTER TABLE `restraunts` DISABLE KEYS */;
INSERT INTO `restraunts` VALUES (1,'McDonalds',3,'123 Main St'),(2,'Jack in the Box',3.5,'101 Parkway Ave'),(3,'In-n-Out',5,'555 Circle Way'),(4,'Taco Bell',4,'90 Jackson Blvd');
/*!40000 ALTER TABLE `restraunts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-12 17:28:10
