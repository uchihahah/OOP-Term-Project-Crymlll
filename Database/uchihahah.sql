-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 23, 2021 at 01:35 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uchihahah`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `accountid` int(15) NOT NULL,
  `customerid` int(5) NOT NULL,
  `type` varchar(50) NOT NULL,
  `balance` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`accountid`, `customerid`, `type`, `balance`) VALUES
(1, 1, 'Loan', 600000),
(2, 2, 'Loan', 2999998),
(3, 1, 'Saving', 8850000),
(4, 1, 'Checking Account', 3950000),
(5, 4, 'Saving', 12476000),
(7, 3, 'Saving', 7650000),
(8, 3, 'Checking Account', 1800000),
(9, 4, 'Checking Account', 4950000),
(11, 4, 'Loan', 1000000),
(12, 6, 'Loan', 10000000);

-- --------------------------------------------------------

--
-- Table structure for table `accounttransactions`
--

CREATE TABLE `accounttransactions` (
  `accountid` int(15) NOT NULL,
  `datetime` datetime DEFAULT NULL,
  `withdraw` varchar(50) NOT NULL,
  `amount` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounttransactions`
--

INSERT INTO `accounttransactions` (`accountid`, `datetime`, `withdraw`, `amount`) VALUES
(2, '2021-05-12 00:00:00', 'Pay Loan', 333333.3333333333),
(2, '2021-05-12 00:00:00', 'Interest', 80000),
(2, '2021-05-12 00:00:00', 'Pay Loan', 333333.2727272727),
(2, '2021-05-12 00:00:00', 'Interest', 73333.32),
(7, '2021-05-15 00:00:00', 'Deposit', 500000),
(8, '2021-05-15 00:00:00', 'Withdraw', 1200000),
(5, '2021-05-15 00:00:00', 'Deposit', 51520),
(2, '2021-05-15 00:00:00', 'Pay Loan', 333333.2),
(2, '2021-05-15 00:00:00', 'Interest', 66666.64),
(5, '2021-05-15 00:00:00', 'Interest', 26000),
(1, '2021-05-15 00:00:00', 'Pay Loan', 75000),
(1, '2021-05-15 00:00:00', 'Interest', 18000),
(1, '2021-05-15 00:00:00', 'Pay Loan', 75000),
(1, '2021-05-15 00:00:00', 'Interest', 16500),
(3, '2021-05-15 00:00:00', 'Deposit', 1200000),
(4, '2021-05-15 00:00:00', 'Deposit', 1400000),
(4, '2021-05-15 00:00:00', 'Deposit', 800000),
(3, '2021-05-15 00:00:00', 'Deposit', 686772),
(3, '2021-05-16 00:00:00', 'Deposit', 500000),
(4, '2021-05-16 00:00:00', 'Withdraw', 1200000),
(3, '2021-05-19 00:00:00', 'Deposit', 1200000),
(5, '2021-05-19 00:00:00', 'Deposit', 500000),
(5, '2021-05-19 00:00:00', 'Deposit', 7000000),
(3, '2021-05-19 00:00:00', 'Deposit', 50000),
(9, '2021-05-19 00:00:00', 'Withdraw', 1000000),
(5, '2021-05-19 00:00:00', 'Deposit', 50000),
(5, '2021-05-19 00:00:00', 'Deposit', 50000),
(5, '2021-05-19 00:00:00', 'Deposit', 1000000),
(9, '2021-05-19 00:00:00', 'Withdraw', 50000),
(5, '2021-05-19 00:00:00', 'Deposit', 1200000),
(5, '2021-05-19 00:00:00', 'Deposit', 50000),
(5, '2021-05-19 00:00:00', 'Deposit', 50000),
(5, '2021-05-19 00:00:00', 'Deposit', 50000),
(4, '2021-05-19 00:00:00', 'Withdraw', 50000),
(4, '2021-05-19 00:00:00', 'Deposit', 1200000),
(3, '2021-05-19 23:59:16', 'Deposit', 1200000),
(5, '2021-05-20 00:04:14', 'Deposit', 1200000),
(9, '2021-05-20 00:04:22', 'Withdraw', 1000000),
(9, '2021-05-20 00:04:30', 'Withdraw', 1000000),
(11, '2021-05-20 00:17:48', 'Pay Loan', 100000),
(11, '2021-05-20 00:17:48', 'Interest', 24000),
(11, '2021-05-20 00:18:10', 'Pay Loan', 100000),
(11, '2021-05-20 00:18:10', 'Interest', 22000),
(3, '2021-05-20 11:22:02', 'Deposit', 1200000),
(4, '2021-05-20 12:53:50', 'Deposit', 1000000),
(1, '2021-05-20 18:52:47', 'Pay Loan', 75000),
(1, '2021-05-20 18:52:47', 'Interest', 15000),
(1, '2021-05-20 18:53:35', 'Pay Loan', 75000),
(1, '2021-05-20 18:53:35', 'Interest', 13500),
(3, '2021-05-22 14:21:47', 'Deposit', 1200000),
(3, '2021-05-22 14:27:33', 'Deposit', 500000);

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `nim` varchar(9) NOT NULL,
  `namaAdmin` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`nim`, `namaAdmin`, `password`) VALUES
('119140007', 'Cahya Andy Mareza', '2001-03-04'),
('119140110', 'Aulia Rahman Zulfi', '2001-02-09'),
('119140217', 'Fadhil Azhar Alsani', '2000-10-27');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customerid` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customerid`, `name`, `address`, `phone`, `email`, `password`) VALUES
(1, 'Mohammed', 'Cilebut', '2147483647', 'mohammed@gmail.com', '123456'),
(2, 'Mustopa', 'Bekasi', '0214323421', 'mustopa@gmail.com', '123456'),
(3, 'Ali', 'Jawa Barat', '08434213432', 'alisa@gmail.com', 'aaabbbccc'),
(4, 'Ikura Lilas', 'Tokyo', '0213343221', 'yoasobi@gmail.com', '123456'),
(6, 'dimaskanjeng', 'bandungmaung', '08134123124', 'dimasoji@yahoo.com', 'bangj69');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`accountid`),
  ADD KEY `customerid` (`customerid`);

--
-- Indexes for table `accounttransactions`
--
ALTER TABLE `accounttransactions`
  ADD KEY `accountid` (`accountid`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customerid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customers` (`customerid`) ON UPDATE CASCADE;

--
-- Constraints for table `accounttransactions`
--
ALTER TABLE `accounttransactions`
  ADD CONSTRAINT `accounttransactions_ibfk_1` FOREIGN KEY (`accountid`) REFERENCES `accounts` (`accountid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
