-- Write a script that creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL
    PRIMARY KEY(id)
);