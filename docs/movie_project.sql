-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2021 at 07:07 PM
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
-- Database: `movie_project`
--
CREATE DATABASE IF NOT EXISTS `movie_project` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;
USE `movie_project`;

-- --------------------------------------------------------

--
-- Table structure for table `actors`
--

DROP TABLE IF EXISTS `actors`;
CREATE TABLE `actors` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL,
  `origin` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `birth_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `actors`
--

INSERT INTO `actors` (`id`, `name`, `origin`, `birth_date`) VALUES
(1, 'Tom Hardy', 'United Kingdom', '1977-09-15'),
(2, 'Michelle Williams', 'United States', '1980-09-09'),
(3, 'Riz Ahmed', 'United Kingdom', '1982-12-01'),
(4, 'Scott Haze', 'United States', '1993-06-28'),
(5, 'Woody Harrelson', 'United States', '1961-07-23'),
(6, 'Robert Downey Jr.', 'United States', '1965-04-04'),
(7, 'Chris Evans', 'United States', '1981-06-13'),
(8, 'Mark Ruffalo', 'United States', '1967-11-22'),
(9, 'Chris Hemsworth', 'Australia', '1983-08-11'),
(10, 'Scarlett Johansson', 'United States', '1984-11-22'),
(11, 'Daniel Craig', 'United Kingdom', '1968-03-02'),
(12, 'Eva Green', 'France', '1980-06-06'),
(13, 'Judi Dench', 'United Kingdom', '1934-12-09'),
(14, 'Jeffrey Wright', 'United States', '1965-12-07'),
(15, 'Mads Mikkelsen', 'Denmark', '1965-11-22'),
(16, 'Ben Barnes', 'United Kingdom', '1981-08-20'),
(17, 'Skandar Keynes', 'United Kingdom', '1991-09-05'),
(18, 'Georgie Henley', 'United Kingdom', '1995-07-09'),
(19, 'William Moseley', 'United Kingdom', '1987-04-27'),
(20, 'Anna Popplewell', 'United Kingdom', '1988-12-16'),
(21, 'Timothée Chalamet', 'United States', '1995-12-27'),
(22, 'Rebecca Ferguson', 'Sweden', '1983-10-19'),
(23, 'Zendaya', 'United States', '1996-09-01'),
(24, 'Oscar Isaac', 'Guatemala', '1979-03-09'),
(25, 'Jason Momoa', 'United States', '1979-08-01'),
(26, 'Mel Gibson', 'United States', '1956-01-03'),
(27, 'Joanne Samuel', 'Australia', '1957-08-05'),
(28, 'Hugh Keays-Byrne', 'Australia', '1947-05-18'),
(29, 'Steve Bisley', 'Australia', '1951-12-26'),
(30, 'Tim Burns', 'Australia', '1953-03-14'),
(31, 'Adam Sandler', 'United States', '1966-09-09'),
(32, 'Kevin James', 'United States', '1965-04-26'),
(33, 'Andy Samberg', 'United States', '1978-08-18'),
(34, 'Selena Gomez', 'United States', '1992-07-22'),
(35, 'Fran Drescher', 'United States', '1957-09-30'),
(36, 'Carrie Coon', 'United States', '1981-01-24'),
(37, 'Paul Rudd', 'United States', '1969-04-06'),
(38, 'Finn Wolfhard', 'Canada', '2002-12-23'),
(39, 'Mckenna Grace', 'United States', '2006-06-25'),
(40, 'Bill Murray', 'United States', '1950-09-21'),
(41, 'Vivianne Bánovits', 'Sweden', '1990-08-29'),
(42, 'András Mózes', 'Hungary', '1990-06-04'),
(43, 'Barna Bokor', 'Romania', '1980-10-04'),
(44, 'Gabriella Gubás', 'Hungary', '1974-04-07'),
(45, 'Szabolcs Bede Fazekas', 'Hungary', '1966-10-22'),
(46, 'Lady Gaga', 'United States', '1986-03-28'),
(47, 'Adam Driver', 'United States', '1983-11-19'),
(48, 'Al Pacino', 'United States', '1940-04-25'),
(49, 'Jeremy Irons', 'United Kingdom', '1948-09-19'),
(50, 'Jared Leto', 'United States', '1971-12-26'),
(51, 'Seth MacFarlane', 'United States', '1973-10-26'),
(52, 'Charlize Theron', 'South Africa', '1975-08-07'),
(53, 'Liam Neeson', 'United Kingdom', '1952-06-07'),
(54, 'Amanda Seyfried', 'United States', '1985-12-03'),
(55, 'Giovanni Ribisi', 'United States', '1974-12-17');

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Animation'),
(4, 'Comedy'),
(5, 'Crime'),
(6, 'Drama'),
(7, 'Family'),
(8, 'Fantasy'),
(9, 'History'),
(10, 'Horror'),
(11, 'Sci-Fi'),
(12, 'Thriller'),
(13, 'Western');

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL,
  `logo` text COLLATE utf8_hungarian_ci NOT NULL,
  `length` int(11) NOT NULL,
  `certificate` int(11) NOT NULL,
  `release_date` date NOT NULL,
  `writer_id` int(11) NOT NULL,
  `producer_id` int(11) NOT NULL,
  `studio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`id`, `name`, `logo`, `length`, `certificate`, `release_date`, `writer_id`, `producer_id`, `studio_id`) VALUES
(1, 'Venom', '../static/images/Venom.jpg', 140, 15, '2018-10-04', 6, 1, 1),
(2, 'Endgame', '../static/images/Endgame.jpeg', 182, 12, '2019-04-25', 1, 9, 2),
(3, 'Casino Royale', '../static/images/Casino Royale.jpeg', 144, 15, '2006-11-16', 7, 5, 3),
(4, 'The Chronicles of Narnia: Prince Caspian', '../static/images/The Chronicles of Narnia.jpeg', 150, 12, '2008-06-12', 2, 10, 4),
(5, 'Dune', '../static/images/Dune.jpeg', 135, 16, '2021-10-21', 8, 6, 5),
(6, 'Mad Max', '../static/images/Mad Max.jpeg', 95, 16, '1980-05-09', 3, 7, 6),
(7, 'Hotel Transylvania', '../static/images/Hotel Transylvania.jpeg', 91, 6, '2012-10-04', 9, 8, 9),
(8, 'Ghostbusters: Afterlife', '../static/images/Ghostbusters Afterlife.jpeg', 124, 12, '2021-11-18', 4, 11, 7),
(9, 'A hazugság ára', '../static/images/A hazugság ára.jpeg', 125, 16, '2021-10-21', 10, 4, 8),
(10, 'House of Gucci', '../static/images/House of Gucci.jpeg', 158, 12, '2021-11-25', 5, 3, 3),
(11, 'A Million Ways to Die in the West', '../static/images/A million ways to die in the west.jpeg', 116, 16, '2014-06-12', 11, 2, 10);

-- --------------------------------------------------------

--
-- Table structure for table `movie_actors`
--

DROP TABLE IF EXISTS `movie_actors`;
CREATE TABLE `movie_actors` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `actor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `movie_actors`
--

INSERT INTO `movie_actors` (`id`, `movie_id`, `actor_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 2, 1),
(7, 2, 2),
(8, 2, 3),
(9, 2, 4),
(10, 2, 5),
(11, 3, 1),
(12, 3, 2),
(13, 3, 3),
(14, 3, 4),
(15, 3, 5),
(16, 4, 1),
(17, 4, 2),
(18, 4, 3),
(19, 4, 4),
(20, 4, 5),
(21, 5, 1),
(22, 5, 2),
(23, 5, 3),
(24, 5, 4),
(25, 5, 5),
(26, 6, 1),
(27, 6, 2),
(28, 6, 3),
(29, 6, 4),
(30, 6, 5),
(31, 7, 1),
(32, 7, 2),
(33, 7, 3),
(34, 7, 4),
(35, 7, 5),
(36, 8, 1),
(37, 8, 2),
(38, 8, 3),
(39, 8, 4),
(40, 8, 5),
(41, 9, 1),
(42, 9, 2),
(43, 9, 3),
(44, 9, 4),
(45, 9, 5),
(46, 10, 1),
(47, 10, 2),
(48, 10, 3),
(49, 10, 4),
(50, 10, 5),
(51, 11, 1),
(52, 11, 2),
(53, 11, 3),
(54, 11, 4),
(55, 11, 5);

-- --------------------------------------------------------

--
-- Table structure for table `movie_genres`
--

DROP TABLE IF EXISTS `movie_genres`;
CREATE TABLE `movie_genres` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `movie_genres`
--

INSERT INTO `movie_genres` (`id`, `movie_id`, `genre_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 11),
(4, 2, 1),
(5, 2, 2),
(6, 2, 6),
(7, 2, 11),
(8, 3, 1),
(9, 3, 2),
(10, 3, 12),
(11, 4, 1),
(12, 4, 2),
(13, 4, 7),
(14, 4, 8),
(15, 5, 1),
(16, 5, 2),
(17, 5, 6),
(18, 5, 11),
(19, 6, 1),
(20, 6, 2),
(21, 6, 11),
(22, 6, 12),
(23, 7, 2),
(24, 7, 3),
(25, 7, 4),
(26, 7, 7),
(27, 7, 10),
(28, 8, 2),
(29, 8, 4),
(30, 8, 8),
(31, 9, 5),
(32, 9, 6),
(33, 9, 9),
(34, 9, 12),
(35, 10, 5),
(36, 10, 6),
(37, 11, 4),
(38, 11, 13);

-- --------------------------------------------------------

--
-- Table structure for table `producers`
--

DROP TABLE IF EXISTS `producers`;
CREATE TABLE `producers` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL,
  `origin` varchar(20) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `producers`
--

INSERT INTO `producers` (`id`, `name`, `origin`) VALUES
(1, 'Ruben Fleischer', 'United States'),
(2, 'Seth MacFarlane', 'United States'),
(3, 'Ridley Scott', 'United  Kingdom'),
(4, 'Helmeczy Dorottya', 'Hungary'),
(5, 'Martin Campbell', 'New Zealand'),
(6, 'Denis Villeneuve', 'Canada'),
(7, 'George Miller', 'Australia'),
(8, 'Genndy Tartakovsky', 'Russia'),
(9, 'Kevin Feige', 'United States'),
(10, 'Andrew Adamson', 'New Zealand'),
(11, 'Jason Reitman', 'Canada');

-- --------------------------------------------------------

--
-- Table structure for table `studios`
--

DROP TABLE IF EXISTS `studios`;
CREATE TABLE `studios` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL,
  `origin` varchar(20) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `studios`
--

INSERT INTO `studios` (`id`, `name`, `origin`) VALUES
(1, 'Sony Pictures Entertainment', 'United States'),
(2, 'Marvel Studios', 'United States'),
(3, 'Metro-Goldwyn-Mayer', 'United States'),
(4, 'Walt Disney Pictures', 'United States'),
(5, 'Legendary Pictures', 'United States'),
(6, 'Kennedy Miller Productions', 'Australia'),
(7, 'Columbia Pictures', 'United States'),
(8, 'Megafilm Kft', 'Hungary'),
(9, 'Sony Pictures Animation', 'United States'),
(10, 'Fuzzy Door Productions', 'United States');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `email` varchar(30) COLLATE utf8_hungarian_ci NOT NULL,
  `password_hash` text COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password_hash`) VALUES
(1, 'proba', 'proba@gmail.com', '$2b$12$KTQmqyh0h8feC7AfENLJJOWBoIkZAEU.GMS7Iz0je0FSbjW1p3mQm'),
(2, 'proba2', 'proba2@gmail.com', '$2b$12$QVH6qtoGEUeNmfb94LsNleb3N5IHAiwEHEoAIlnRGLCVATwlSfZHG'),
(3, 'proba3', 'proba3@gmail.com', '$2b$12$luaRJr9tn.9axBpPJF7GleXe6wjjpecy7cduzX6GCf7AafzzLoiRu');

-- --------------------------------------------------------

--
-- Table structure for table `writers`
--

DROP TABLE IF EXISTS `writers`;
CREATE TABLE `writers` (
  `id` int(11) NOT NULL,
  `name` varchar(40) COLLATE utf8_hungarian_ci NOT NULL,
  `origin` varchar(20) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `writers`
--

INSERT INTO `writers` (`id`, `name`, `origin`) VALUES
(1, 'Christopher Markus', 'United States'),
(2, 'Andrew Adamson', 'New Zealand'),
(3, 'James McCausland', 'United States'),
(4, 'Gil Kenan', 'United Kingdom'),
(5, 'Roberto Bentivegna', 'United Kingdom'),
(6, 'Richard Wenk', 'United States'),
(7, 'Neal Purvis', 'United Kingdom'),
(8, 'Jon Spaihts', 'United States'),
(9, 'Peter Baynham', 'United Kingdom'),
(10, 'Bendi Balázs', 'Hungary'),
(11, 'Wellesley Wild', 'United States');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actors`
--
ALTER TABLE `actors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`),
  ADD KEY `writer_fkey` (`writer_id`),
  ADD KEY `producer_fkey` (`producer_id`),
  ADD KEY `studio_fkey` (`studio_id`);

--
-- Indexes for table `movie_actors`
--
ALTER TABLE `movie_actors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `movie_actor_fkey` (`movie_id`),
  ADD KEY `actor_movie_fkey` (`actor_id`);

--
-- Indexes for table `movie_genres`
--
ALTER TABLE `movie_genres`
  ADD PRIMARY KEY (`id`),
  ADD KEY `movie_genre_fkey` (`movie_id`),
  ADD KEY `genre_movie_fkey` (`genre_id`);

--
-- Indexes for table `producers`
--
ALTER TABLE `producers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studios`
--
ALTER TABLE `studios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `writers`
--
ALTER TABLE `writers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actors`
--
ALTER TABLE `actors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `movie_actors`
--
ALTER TABLE `movie_actors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `movie_genres`
--
ALTER TABLE `movie_genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `producers`
--
ALTER TABLE `producers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `studios`
--
ALTER TABLE `studios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `writers`
--
ALTER TABLE `writers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `movies`
--
ALTER TABLE `movies`
  ADD CONSTRAINT `producer_fkey` FOREIGN KEY (`producer_id`) REFERENCES `producers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `studio_fkey` FOREIGN KEY (`studio_id`) REFERENCES `studios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `writer_fkey` FOREIGN KEY (`writer_id`) REFERENCES `writers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `movie_actors`
--
ALTER TABLE `movie_actors`
  ADD CONSTRAINT `actor_movie_fkey` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `movie_actor_fkey` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `movie_genres`
--
ALTER TABLE `movie_genres`
  ADD CONSTRAINT `genre_movie_fkey` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `movie_genre_fkey` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
