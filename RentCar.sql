-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rent_cars_br
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `sobrenome` varchar(255) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Pedro','Elorriaga','Alameda Portugal, 205'),(2,'Julia','Matos','Alameda Madeira, 4016'),(3,'Renan','Texeira','Rua Itaípu, 136'),(4,'Luan','Texeira','Rua Itaípu, 188'),(5,'Leonardo','Matagal','Avenida Ibirá, APTO 22');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventarios_carros`
--

DROP TABLE IF EXISTS `inventarios_carros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventarios_carros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modelo` varchar(255) NOT NULL,
  `transmissao` varchar(255) NOT NULL,
  `motor` float NOT NULL,
  `combustivel` varchar(255) NOT NULL,
  `marcas_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `marcas_id` (`marcas_id`),
  CONSTRAINT `inventarios_carros_ibfk_1` FOREIGN KEY (`marcas_id`) REFERENCES `marcas_carros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventarios_carros`
--

LOCK TABLES `inventarios_carros` WRITE;
/*!40000 ALTER TABLE `inventarios_carros` DISABLE KEYS */;
INSERT INTO `inventarios_carros` VALUES (1,'Sport','Automatico',2,'Diesel',1),(2,'Evoque','Automatico',1.8,'Gasolina',1),(3,'320i','Semi-automatico',1.6,'Gasolina',4),(4,'A3','Automatico',1.8,'Gasolina',3),(5,'Voyage','Manual',1,'Gasolina',2);
/*!40000 ALTER TABLE `inventarios_carros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas_carros`
--

DROP TABLE IF EXISTS `marcas_carros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marcas_carros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(255) NOT NULL,
  `origem` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas_carros`
--

LOCK TABLES `marcas_carros` WRITE;
/*!40000 ALTER TABLE `marcas_carros` DISABLE KEYS */;
INSERT INTO `marcas_carros` VALUES (1,'Range Rover','Inglaterra'),(2,'Volkswagen','Alemanha'),(3,'Audi','Alemanha'),(4,'BMW','Alemanha'),(5,'Peugeot','França');
/*!40000 ALTER TABLE `marcas_carros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagamentos`
--

DROP TABLE IF EXISTS `pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagamentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `valor` float NOT NULL,
  `periodo` varchar(255) NOT NULL,
  `carro_id` int NOT NULL,
  `cliente_id` int NOT NULL,
  `data_do_pagamento` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `carro_id` (`carro_id`),
  KEY `cliente_id` (`cliente_id`),
  CONSTRAINT `pagamentos_ibfk_1` FOREIGN KEY (`carro_id`) REFERENCES `inventarios_carros` (`id`),
  CONSTRAINT `pagamentos_ibfk_2` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagamentos`
--

LOCK TABLES `pagamentos` WRITE;
/*!40000 ALTER TABLE `pagamentos` DISABLE KEYS */;
INSERT INTO `pagamentos` VALUES (1,225.8,'2 dias',5,4,'2024-02-20'),(2,1.48,'1 semana',1,1,'2024-02-20'),(3,1.158,'1 semana',4,3,'2024-02-20'),(4,1.282,'1 semana',2,1,'2024-02-20');
/*!40000 ALTER TABLE `pagamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'rent_cars_br'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-20 21:46:37
