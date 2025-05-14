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

const query2 = `
ALTER TABLE users
ADD CONSTRAINT fk_users_fav_driver_1 FOREIGN KEY (fav_driver_1)
REFERENCES drivers(driver_id);
`;

const query3 = `
ALTER TABLE users
ADD CONSTRAINT fk_users_fav_driver_2 FOREIGN KEY (fav_driver_2)
REFERENCES drivers(driver_id);
`;

const query4 = `
ALTER TABLE users
ADD CONSTRAINT fk_users_fav_team FOREIGN KEY (fav_team)
REFERENCES teams(team_id);
`;

const query5 = `
ALTER TABLE drivers
ADD CONSTRAINT fk_drivers_team FOREIGN KEY (team_id)
REFERENCES teams(team_id);
`;

const query6 = `
ALTER TABLE driver_standings
ADD CONSTRAINT fk_driver_standings_driver FOREIGN KEY (driver_id)
REFERENCES drivers(driver_id);
`;

const query7 = `
ALTER TABLE team_standings
ADD CONSTRAINT fk_team_standings_team FOREIGN KEY (team_id)
REFERENCES teams(team_id);
`;
conn.query(query7, (err, results) => {
    if (err) {
        console.error('Error creating tables:', err);
        return;
    }
    console.log('Tables created successfully:', results);
});