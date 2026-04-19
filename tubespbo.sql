-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 04:34 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tubespbo`
--

-- --------------------------------------------------------

--
-- Table structure for table `listtugas`
--

CREATE TABLE `listtugas` (
  `Id` int(11) NOT NULL,
  `Mata_kuliah` varchar(50) NOT NULL,
  `Judul_tugas` varchar(100) NOT NULL,
  `Deadline` date NOT NULL,
  `Keterangan` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `listtugas`
--

INSERT INTO `listtugas` (`Id`, `Mata_kuliah`, `Judul_tugas`, `Deadline`, `Keterangan`) VALUES
(28, 'Pemrograman Berorientasi Objek', 'Praktikum menghubungkan ke database', '2022-11-06', 'menghubungkan dari mysql ke python'),
(29, 'Sistem Operasi', 'Praktikum 6', '2022-11-10', 'Tugas pendahuluan tidak usah dikerjakan'),
(30, 'Deasin Proses Bisnis', 'Merangkum materi', '2022-11-06', ''),
(31, 'UI UX', 'Tubes', '2022-11-14', 'BAB 2'),
(32, 'UI UX', 'Tugas 8', '2022-11-07', ''),
(33, 'Basis Data', 'Tugas kelompok', '2022-11-28', 'Membuat PPT materi group by');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listtugas`
--
ALTER TABLE `listtugas`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listtugas`
--
ALTER TABLE `listtugas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
