-- create a database hbtn_0d_usa
CREATE  DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates the table states
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT  UNIQUE,
    name VARCHAR(256) NOT NULL
);
