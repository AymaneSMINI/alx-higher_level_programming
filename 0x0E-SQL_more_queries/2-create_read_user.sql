-- create a user with all privileges and a password
Create USER IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO user_0d_2@hbtn_0d_2;
