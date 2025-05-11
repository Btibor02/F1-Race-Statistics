const mySQL = require('mysql2');
const dotenv = require('dotenv');

dotenv.config();

const{CONNECTION_URL} = process.env;
const connection = mySQL.createConnection(CONNECTION_URL);
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the MySQL database');
});

const db = mySQL.createPool({CONNECTION_URL});
module.exports = db;
