-- A script that creates a table called first_table in the current database in your MySQL server.
-- Create table first_table, if it already exists with fields id integer and name character.
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);

