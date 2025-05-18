//inseerting into the database

const db = require('./dbConnection.js');

async function insertUser(username, passwordHash){
    await db.query('INSERT INTO users (username, passwordHash) VALUES (?, ?)', 
        [username, passwordHash]);

}

async function updateUserFavs(username, fav_driver_1, fav_driver_2, fav_team){
    await db.query('UPDATE users SET fav_driver_1 = ?, fav_driver_2 = ?, fav_team = ? WHERE username = ?', 
        [fav_driver_1, fav_driver_2, fav_team, username]);
        
}
