-- create a database and a table inide the database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id AUTO_INCREMENT PRIMARY KEY,
	state_id INT FOREIGN KEY(state_id) REFERENCES(state.id),
	name VARCHAR(256)
) type=InnoDB;
