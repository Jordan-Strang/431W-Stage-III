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
-- Table structure for table `studentcontact`
--

DROP TABLE IF EXISTS `studentcontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentcontact` (
  `StudentID` int NOT NULL,
  `PhoneNumber` varchar(12) DEFAULT NULL,
  `EmailAddress` varchar(150) DEFAULT NULL,
  KEY `StudentContact-StudentInformation` (`StudentID`),
  CONSTRAINT `StudentContact-StudentInformation` FOREIGN KEY (`StudentID`) REFERENCES `studentinformation` (`StudentID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentcontact`
--

LOCK TABLES `studentcontact` WRITE;
/*!40000 ALTER TABLE `studentcontact` DISABLE KEYS */;
INSERT INTO `studentcontact` VALUES (111110,'123-456-7890','JohnDoe@psu.edu'),(111111,'248-978-2714','KylaRobins@psu.edu'),(111112,'368-274-8531','RyanGarland@psu.edu'),(111113,'555-234-5678','AvaWilson@psu.edu'),(111114,'789-890-1012','JacobSmith@psu.edu'),(111115,'565-901-2345','OliviaBrown@psu.edu'),(111116,'898-012-2323','MichealDavis@psu.edu'),(111117,'456-567-5656','DanielAnderson@psu.edu'),(111118,'256-898-5698','MiaRobinson@pus.edu'),(111119,'647-798-2541','AlexanderLee@psu.edu');
/*!40000 ALTER TABLE `studentcontact` ENABLE KEYS */;
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
