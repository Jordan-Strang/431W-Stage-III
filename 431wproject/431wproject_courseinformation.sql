-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: 431wproject
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courseinformation`
--

DROP TABLE IF EXISTS `courseinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courseinformation` (
  `CourseID` int NOT NULL,
  `CourseName` varchar(50) NOT NULL,
  `CourseCode` int NOT NULL,
  `DepartmentID` int NOT NULL,
  `CreditHours` int NOT NULL,
  `InstructorID` int DEFAULT NULL,
  PRIMARY KEY (`CourseID`),
  KEY `courseinformation-department` (`DepartmentID`),
  KEY `courseinformation-instructorinformation` (`InstructorID`),
  CONSTRAINT `courseinformation-department` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`),
  CONSTRAINT `courseinformation-instructorinformation` FOREIGN KEY (`InstructorID`) REFERENCES `instructorinformation` (`InstructorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courseinformation`
--

LOCK TABLES `courseinformation` WRITE;
/*!40000 ALTER TABLE `courseinformation` DISABLE KEYS */;
INSERT INTO `courseinformation` VALUES (123450,'CMPSC',431,1210,3,21300),(123451,'IST',320,1211,3,21300),(123452,'GEOSC',220,1212,3,21311),(123453,'MATSE',262,1213,3,21312),(123454,'HIST',345,1214,3,21313),(123455,'SOC',221,1215,4,21314),(123456,'NURS',464,1216,4,21315),(123457,'KINES',120,1217,3,21316),(123458,'CHEM',202,1218,4,21317),(123459,'STAT',319,1219,3,21318);
/*!40000 ALTER TABLE `courseinformation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 18:36:50
