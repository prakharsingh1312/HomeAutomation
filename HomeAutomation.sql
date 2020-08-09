-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 09, 2020 at 07:48 PM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HomeAutomation`
--

-- --------------------------------------------------------

--
-- Table structure for table `appliances`
--

CREATE TABLE `appliances` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `pin_number` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliances`
--

INSERT INTO `appliances` (`id`, `name`, `state`, `pin_number`, `user_id`) VALUES
(1, 'Mario', 1, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Automation`
--

CREATE TABLE `Automation` (
  `id` int(11) NOT NULL,
  `parameter_id` int(11) DEFAULT NULL,
  `parameter value` int(11) DEFAULT NULL,
  `state value` int(11) DEFAULT NULL,
  `Automation_paraqmeter_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

CREATE TABLE `budget` (
  `id` int(11) NOT NULL,
  `desc` varchar(1000) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `budget_types_id` int(11) DEFAULT NULL,
  `budget_payment_method_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `budget_payment_method`
--

CREATE TABLE `budget_payment_method` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `budget_types`
--

CREATE TABLE `budget_types` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Parameter`
--

CREATE TABLE `Parameter` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `min value` int(11) DEFAULT NULL,
  `max value` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ReminderAlarm`
--

CREATE TABLE `ReminderAlarm` (
  `id` int(11) NOT NULL,
  `alert_type` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `time` time DEFAULT NULL,
  `day` date DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ReminderAlarm`
--

INSERT INTO `ReminderAlarm` (`id`, `alert_type`, `description`, `frequency`, `time`, `day`, `state`, `user_id`) VALUES
(1, 1, 'Name', 97, '18:52:00', NULL, 1, 1),
(6, 2, 'Jayash Budday', NULL, '19:50:00', '2020-09-09', 1, 1),
(15, 2, 'Rawat Budday', NULL, '23:14:00', '2021-01-14', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `hash` varchar(100) DEFAULT NULL,
  `activated` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `password`, `email`, `hash`, `activated`) VALUES
(1, 'Prakhar Singh', '0b5790096cefb9b29f9b0a16ba786564', 'prakharsingh13@gmail.com', '', 1),
(2, 'Ritik Rawat', '0b5790096cefb9b29f9b0a16ba786564', 'ritikneverback@gmail.com', '', 1),
(3, 'Anshumaan Singh', 'afc30a0510c07da50d009753cbea1abf', 'ronaldoanshuman@gmail.com', '', 1),
(4, 'Prashant', '08bb7c0266235a3c5bd54c6f8f2342a5', 'connectprashant99@gmail.com', '', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appliances`
--
ALTER TABLE `appliances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Automation`
--
ALTER TABLE `Automation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Automation_paraqmeter_id` (`Automation_paraqmeter_id`);

--
-- Indexes for table `budget`
--
ALTER TABLE `budget`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `budget_types_id` (`budget_types_id`),
  ADD KEY `budget_payment_method_id` (`budget_payment_method_id`);

--
-- Indexes for table `budget_payment_method`
--
ALTER TABLE `budget_payment_method`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `budget_types`
--
ALTER TABLE `budget_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Parameter`
--
ALTER TABLE `Parameter`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `ReminderAlarm`
--
ALTER TABLE `ReminderAlarm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appliances`
--
ALTER TABLE `appliances`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Automation`
--
ALTER TABLE `Automation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `budget`
--
ALTER TABLE `budget`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `budget_payment_method`
--
ALTER TABLE `budget_payment_method`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `budget_types`
--
ALTER TABLE `budget_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Parameter`
--
ALTER TABLE `Parameter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `ReminderAlarm`
--
ALTER TABLE `ReminderAlarm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `appliances`
--
ALTER TABLE `appliances`
  ADD CONSTRAINT `appliances_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `Automation`
--
ALTER TABLE `Automation`
  ADD CONSTRAINT `Automation_ibfk_1` FOREIGN KEY (`Automation_paraqmeter_id`) REFERENCES `Parameter` (`id`);

--
-- Constraints for table `budget`
--
ALTER TABLE `budget`
  ADD CONSTRAINT `budget_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `budget_ibfk_2` FOREIGN KEY (`budget_types_id`) REFERENCES `budget_types` (`id`),
  ADD CONSTRAINT `budget_ibfk_3` FOREIGN KEY (`budget_payment_method_id`) REFERENCES `budget_payment_method` (`id`);

--
-- Constraints for table `budget_payment_method`
--
ALTER TABLE `budget_payment_method`
  ADD CONSTRAINT `budget_payment_method_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `budget_types`
--
ALTER TABLE `budget_types`
  ADD CONSTRAINT `budget_types_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `Parameter`
--
ALTER TABLE `Parameter`
  ADD CONSTRAINT `Parameter_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `ReminderAlarm`
--
ALTER TABLE `ReminderAlarm`
  ADD CONSTRAINT `ReminderAlarm_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
