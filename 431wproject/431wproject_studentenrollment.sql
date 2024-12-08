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
-- Table structure for table `studentenrollment`
--

DROP TABLE IF EXISTS `studentenrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentenrollment` (
  `StudentID` int NOT NULL,
  `CourseID` int NOT NULL,
  PRIMARY KEY (`StudentID`,`CourseID`),
  KEY `StudentEnrollment-CourseInformation` (`CourseID`),
  CONSTRAINT `StudentEnrollment-CourseInformation` FOREIGN KEY (`CourseID`) REFERENCES `courseinformation` (`CourseID`) ON DELETE CASCADE,
  CONSTRAINT `StudentEnrollment-StudentInformation` FOREIGN KEY (`StudentID`) REFERENCES `studentinformation` (`StudentID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentenrollment`
--

LOCK TABLES `studentenrollment` WRITE;
/*!40000 ALTER TABLE `studentenrollment` DISABLE KEYS */;
INSERT INTO `studentenrollment` VALUES (111110,123450),(111110,123451),(111119,123451),(111115,123452),(111117,123452),(111111,123453),(111112,123453),(111118,123453),(111111,123454),(111114,123454),(111112,123455),(111115,123455),(111117,123455),(111118,123455),(111119,123455),(111113,123456),(111113,123457),(111117,123457),(111119,123457),(111114,123458),(111116,123458),(111114,123459),(111116,123459),(111118,123459);
/*!40000 ALTER TABLE `studentenrollment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 18:36:48
