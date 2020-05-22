-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主机： 100.67.90.31:8597
-- 生成日期： 2020-05-22 19:23:01
-- 服务器版本： 5.6.28-cdb2016-log
-- PHP 版本： 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `yxb`
--

-- --------------------------------------------------------

--
-- 表的结构 `items`
--

DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `uuid` varchar(32) NOT NULL COMMENT '题目UUID号',
  `desp` text COMMENT '题目内容',
  `selections` text COMMENT '题目选项',
  `answer` varchar(4) DEFAULT NULL COMMENT '题目答案'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转储表的索引
--

--
-- 表的索引 `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`uuid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
