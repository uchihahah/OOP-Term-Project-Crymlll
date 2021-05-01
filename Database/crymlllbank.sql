-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2021 at 08:05 AM
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
-- Database: `crymlllbank`
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
(1, 1, 'Saving', 5000000),
(2, 2, 'Loan', 10000000),
(3, 2, 'Checking Account', 7000000),
(4, 1, 'Loan', 6000000);

-- --------------------------------------------------------

--
-- Table structure for table `accounttransactions`
--

CREATE TABLE `accounttransactions` (
  `accountid` int(15) NOT NULL,
  `datetime` date DEFAULT NULL,
  `withdraw` varchar(50) NOT NULL,
  `ammount` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounttransactions`
--

INSERT INTO `accounttransactions` (`accountid`, `datetime`, `withdraw`, `ammount`) VALUES
(1, '2013-09-01', 'Withdraw', 200000),
(2, '2013-08-05', 'Deposit', 500000);

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
  `phone` int(15) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customerid`, `name`, `address`, `phone`, `email`) VALUES
(1, 'Mohammed', 'Jakarta', 2147483647, 'mohammed@gmail.com'),
(2, 'Mustopa', 'Bekasi', 2147483647, 'mustopa@gmail.com'),
(3, 'Ali', 'Cibinong', 2147483647, 'ali@gmail.com');

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
