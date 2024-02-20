CREATE DATABASE Stori;

USE Stori;

CREATE TABLE summary(
  id INT AUTO_INCREMENT PRIMARY KEY,
  credit FLOAT,
  debit FLOAT,
  balance FLOAT,
  month_resume varchar(500)
);
  
CREATE TABLE transactions(
  id INT PRIMARY KEY,
  fecha DATE,
  amount FLOAT
);
