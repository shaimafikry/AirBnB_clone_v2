-- create a data base for our storage

CREATE DATABASE IF NOT EXISTs hbnb_dev_db;

-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd

CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
USE hbnb_dev_db;
GRANT ALL ON hbnb_dev_db.*
TO hbnb_dev@localhost;

-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
USE performance_schema;
GRANT SELECT
ON performance_schema.*
TO hbnb_dev@localhost;

FLUSH PRIVILEGES;
