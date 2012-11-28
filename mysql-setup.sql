n SQL Dump
-- version 2.9.1.1-Debian-8
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Oct 25, 2008 at 11:30 AM
-- Server version: 5.0.32
-- PHP Version: 5.2.0-8+etch11
-- 
-- Database: `electricity`
-- 
CREATE DATABASE `electricity` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `electricity`;

-- --------------------------------------------------------

-- 
-- Table structure for table `consumption`
-- 

CREATE TABLE `consumption` (
  `time` datetime NOT NULL,
  `power` int(5) NOT NULL,
  `temp` float NOT NULL,
  `id` int(11) NOT NULL auto_increment,
  `joules` float NOT NULL,
  KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=74720 ;
ww
