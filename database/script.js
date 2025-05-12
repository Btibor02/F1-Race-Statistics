const mySQL = require('mysql2');

require('dotenv').config();

const conn = mySQL.createConnection({
    uri: process.env.CONNECTION_URL,
    multipleStatements: true, //mult. query
  });
  

const query = `
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  fav_driver_1 VARCHAR(5),
  fav_driver_2 VARCHAR(5),
  fav_team VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS drivers (
  driver_id VARCHAR(5) PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  dob DATE,
  nationality VARCHAR(50),
  code VARCHAR(3),
  team_id VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS teams (
  team_id VARCHAR(5) PRIMARY KEY,
  name VARCHAR(100),
  nationality VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS driver_standings (
  season INT,
  round INT,
  driver_id VARCHAR(5),
  position INT,
  points FLOAT,
  wins INT,
  PRIMARY KEY (season, round, driver_id)
);

CREATE TABLE IF NOT EXISTS team_standings (
  season INT,
  round INT,
  team_id VARCHAR(5),
  position INT,
  points FLOAT,
  wins INT,
  PRIMARY KEY (season, round, team_id)
);

ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;
`;

conn.query(query, (err, results) => {
    if (err) {
        console.error('Error creating tables:', err);
        return;
    }
    console.log('Tables created successfully:', results);
});