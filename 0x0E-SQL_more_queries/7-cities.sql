-- Creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to database
USE hbtn_0d_usa;
-- Creates a table within the database
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	)
