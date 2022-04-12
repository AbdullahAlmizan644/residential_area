-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 04, 2022 at 03:56 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `residential_area`
--

-- --------------------------------------------------------

--
-- Table structure for table `rent_house_post`
--

CREATE TABLE `rent_house_post` (
  `post_id` int(200) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `writer` varchar(200) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rent_house_post`
--

INSERT INTO `rent_house_post` (`post_id`, `name`, `writer`, `content`, `image`, `date`) VALUES
(1, 'this is first post', 'mizan', 'content.....................................', 'post_1.jpg', '2022-03-04 19:11:19'),
(2, 'this is second post', 'sizan', 'content.....................................', 'post_2.jpg', '2022-03-04 19:11:19'),
(4, 'this is third post', 'jubaer', 'content..........................................', 'post_3.jpg', '2022-03-04 19:13:49'),
(5, 'this is fourth post', 'sifat', 'content......................................', 'post_4.jpg', '2022-03-04 19:13:49');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `username`, `email`, `password`, `date`) VALUES
(1, 'admin@gmail.com', 'admin@gmail.com', '12345678', '2022-03-04 16:54:27.855588'),
(2, 'mizan', 'mizan@gmail.com', '12345678', '2022-03-04 17:22:31.951228'),
(3, 'mizan', 'aamizan86@gmail.com', '12345678', '2022-03-04 17:33:31.400383'),
(4, 'admin', 'admin@gmail.com', '12345678', '2022-03-04 17:35:31.877029'),
(5, 'hello', 'hello@gmail.com', '5255452554', '2022-03-04 17:55:53.858719'),
(6, 'SIZAN', 'admin@gmail.com', '12345678', '2022-03-04 17:56:36.968446');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rent_house_post`
--
ALTER TABLE `rent_house_post`
  ADD PRIMARY KEY (`post_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rent_house_post`
--
ALTER TABLE `rent_house_post`
  MODIFY `post_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
