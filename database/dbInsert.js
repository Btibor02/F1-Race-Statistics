//inseerting into the database

const db = require('./dbConnection.js');

async function insertUser(username, passwordHash){
    await db.query('INSERT INTO users (username, passwordHash) VALUES (?, ?)', [username, passwordHash]);

}
