const mySQL = require('mysql2');
const dotenv = require('dotenv');

dotenv.config();

const{CONNECTION_URL} = process.env;

//make a pool better for webapps

const DBconnection = mySQL.createPool(CONNECTION_URL);

DBconnection.getConnection((err, connection) => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the MySQL database');
    connection.release(); // Release the connection back to the pool
});
module.exports = DBconnection;
