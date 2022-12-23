/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.24-MariaDB : Database - dbdonation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbdonation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbdonation`;

/*Table structure for table `blood_report` */

DROP TABLE IF EXISTS `blood_report`;

CREATE TABLE `blood_report` (
  `distribution_id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `unit_distributed` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`distribution_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `blood_report` */

/*Table structure for table `blood_requests` */

DROP TABLE IF EXISTS `blood_requests`;

CREATE TABLE `blood_requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `unit_request` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `blood_requests` */

insert  into `blood_requests`(`request_id`,`receiver_id`,`group_id`,`date_time`,`unit_request`,`pincode`,`status`) values (1,1,3,'12/5/22','10','682509','pending');

/*Table structure for table `blood_requirement_message` */

DROP TABLE IF EXISTS `blood_requirement_message`;

CREATE TABLE `blood_requirement_message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `organization_id` int(11) DEFAULT NULL,
  `donor_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `unit_required` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `blood_requirement_message` */

insert  into `blood_requirement_message`(`message_id`,`organization_id`,`donor_id`,`group_id`,`unit_required`,`description`,`status`) values (1,4,1,3,'5','ggkkjvbf','pending');

/*Table structure for table `bloodgroups` */

DROP TABLE IF EXISTS `bloodgroups`;

CREATE TABLE `bloodgroups` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(100) DEFAULT NULL,
  `group_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `bloodgroups` */

insert  into `bloodgroups`(`group_id`,`group_name`,`group_description`) values (3,'A+ve','bg group'),(5,'ab+','blood'),(6,'o+','blood grp'),(7,'o-','blood grp'),(8,'b-','blood grp'),(9,'a-','blood grp'),(12,'AB+ve','dfgfdgdfgdf');

/*Table structure for table `collection` */

DROP TABLE IF EXISTS `collection`;

CREATE TABLE `collection` (
  `collection_id` int(11) NOT NULL AUTO_INCREMENT,
  `organization_id` int(11) DEFAULT NULL,
  `donor_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `unit_collected` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`collection_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1502 DEFAULT CHARSET=latin1;

/*Data for the table `collection` */

insert  into `collection`(`collection_id`,`organization_id`,`donor_id`,`group_id`,`date_time`,`unit_collected`) values (1501,4,1,6,'2022-10-07 16:04:32','5');

/*Table structure for table `donation` */

DROP TABLE IF EXISTS `donation`;

CREATE TABLE `donation` (
  `donation_id` int(11) NOT NULL AUTO_INCREMENT,
  `donor_id` int(11) DEFAULT NULL,
  `donation_type` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`donation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `donation` */

insert  into `donation`(`donation_id`,`donor_id`,`donation_type`,`details`) values (1,1,'organ','dfgffhgfh');

/*Table structure for table `donor` */

DROP TABLE IF EXISTS `donor`;

CREATE TABLE `donor` (
  `donor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `group_id` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`donor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `donor` */

insert  into `donor`(`donor_id`,`login_id`,`first_name`,`last_name`,`group_id`,`gender`,`age`,`pincode`,`phone`,`email`) values (1,16,'mmkk','mmmmmm','3','mmmnmm','mmm','1234','jjjj','asdfg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'donor','donor','donor'),(3,'receiver','receiver','receiver'),(11,'rec','rec','receiver'),(10,'rec','rec','receiver'),(9,'org','org','Organization'),(8,'vbnm','xcvb','rejected'),(12,'rec','rec','receiver'),(13,'rec','rec','receiver'),(14,'rec','rec','receiver'),(15,'rec','rec','receiver'),(16,'jjjjj','jjjj','donor'),(17,'123','456','Organization'),(18,'','','pending'),(19,'','','pending');

/*Table structure for table `organ` */

DROP TABLE IF EXISTS `organ`;

CREATE TABLE `organ` (
  `organ_id` int(11) NOT NULL AUTO_INCREMENT,
  `organ_name` varchar(100) DEFAULT NULL,
  `organ_details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`organ_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `organ` */

insert  into `organ`(`organ_id`,`organ_name`,`organ_details`) values (1,'Kidney','left a+'),(2,'Heart','A+  ;'),(4,'Heart','bhgfhfghfghf'),(5,'nnhmj','jmjmk,kj');

/*Table structure for table `organ_request` */

DROP TABLE IF EXISTS `organ_request`;

CREATE TABLE `organ_request` (
  `organ_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver_id` int(11) DEFAULT NULL,
  `organ_id` int(11) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`organ_request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `organ_request` */

insert  into `organ_request`(`organ_request_id`,`receiver_id`,`organ_id`,`date_time`,`status`) values (1,1,1,'12/2/22','confirm');

/*Table structure for table `organization` */

DROP TABLE IF EXISTS `organization`;

CREATE TABLE `organization` (
  `organization_id` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `license_number` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`organization_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `organization` */

insert  into `organization`(`organization_id`,`loginid`,`name`,`place`,`pincode`,`phone`,`license_number`,`email`) values (4,9,'ssss','lll','455','1111111','llll','2255'),(3,8,'jjj','jjjj','6789','2345678','ghj','bnm'),(5,17,'qw','qw','22','222','asdf','123'),(6,18,'fgdfgdgfdg','','','','',''),(7,19,'','','','','','');

/*Table structure for table `receiver` */

DROP TABLE IF EXISTS `receiver`;

CREATE TABLE `receiver` (
  `receiver_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`receiver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `receiver` */

insert  into `receiver`(`receiver_id`,`login_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`phone`,`state`,`email`) values (1,15,'mk','mk','kk','mk','44','455','jjjj','');

/*Table structure for table `status` */

DROP TABLE IF EXISTS `status`;

CREATE TABLE `status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `donor_id` int(11) DEFAULT NULL,
  `donation_availability_status` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `status` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
