CREATE DATABASE  IF NOT EXISTS `pathology`;
USE `pathology`;

DROP TABLE IF EXISTS `contains`;
CREATE TABLE `contains` (
  `orderId` varchar(45) NOT NULL,
  `testId` varchar(45) NOT NULL,
  PRIMARY KEY (`orderId`,`testId`),
  KEY `test` (`testId`),
  CONSTRAINT `order` FOREIGN KEY (`orderId`) REFERENCES `order` (`orderId`),
  CONSTRAINT `test` FOREIGN KEY (`testId`) REFERENCES `test` (`testId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `givesorder`;
CREATE TABLE `givesorder` (
  `orderId` varchar(45) NOT NULL,
  `patientId` varchar(45) NOT NULL,
  PRIMARY KEY (`orderId`),
  KEY `patientId` (`patientId`),
  CONSTRAINT `orderId` FOREIGN KEY (`orderId`) REFERENCES `order` (`orderId`),
  CONSTRAINT `patientId` FOREIGN KEY (`patientId`) REFERENCES `patient` (`patientId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `orderId` varchar(45) NOT NULL,
  `date` varchar(45) NOT NULL,
  `amount` varchar(45) NOT NULL,
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient` (
  `patientId` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `age` int NOT NULL,
  `mobileNumber` varchar(10) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`patientId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `testId` varchar(45) NOT NULL,
  `testName` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`testId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;