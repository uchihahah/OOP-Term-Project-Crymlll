-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freesqldatabase.com
-- Generation Time: May 12, 2021 at 10:09 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql6410595`
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
(1, 1, 'Loan', 1000000),
(2, 2, 'Loan', 3333332),
(3, 1, 'Saving', 1091400),
(4, 1, 'Checking Account', 800000),
(5, 4, 'Saving', 1248480),
(7, 2, 'Checking Account', 200000);

-- --------------------------------------------------------

--
-- Table structure for table `accounttransactions`
--

CREATE TABLE `accounttransactions` (
  `accountid` int(15) NOT NULL,
  `datetime` date DEFAULT NULL,
  `withdraw` varchar(50) NOT NULL,
  `amount` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounttransactions`
--

INSERT INTO `accounttransactions` (`accountid`, `datetime`, `withdraw`, `amount`) VALUES
(1, '2021-05-12', 'Pay Loan', 100000),
(1, '2021-05-12', 'Interest', 24000),
(2, '2021-05-12', 'Pay Loan', 333333.3333333333),
(2, '2021-05-12', 'Interest', 80000),
(3, '2021-05-12', 'Interest', 20000),
(3, '2021-05-12', 'Deposit', 50000),
(4, '2021-05-12', 'Deposit', 350000),
(4, '2021-05-12', 'Withdraw', 50000),
(7, '2021-05-12', 'Withdraw', 800000),
(1, '2021-05-12', 'Pay Loan', 100000),
(1, '2021-05-12', 'Interest', 22000),
(2, '2021-05-12', 'Pay Loan', 333333.2727272727),
(2, '2021-05-12', 'Interest', 73333.32),
(3, '2021-05-12', 'Interest', 21400);

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
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customerid`, `name`, `address`, `phone`, `email`) VALUES
(1, 'Mohammed', 'Cibinong', '2147483647', 'mohammed@gmail.com'),
(2, 'Mustopa', 'Bekasi', '0214323421', 'mustopa@gmail.com'),
(3, 'Ali', 'Cibinong', '0843254311', 'alisa@gmail.com'),
(4, 'Ikura Lilas', 'Tokyo', '0213343221', 'yoasobi@gmail.com');

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
