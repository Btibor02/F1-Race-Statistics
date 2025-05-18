//retrieve from the Database
const connectdb = require('./dbConnection');

async function getUserByName(username){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM users WHERE username = ?', [username]);
    return rows[0]; }finally{
        await db.end();
    }
} //retunr only one row (username)

async function getUserFavs(username){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT fav_driver_1, fav_driver_2, fav_team FROM users WHERE username = ?', [username]);
    return rows[0];}finally{
await db.end();
    }
}// ex. of a return 
//    {
//     fav_driver_1: 'VER',
//     fav_driver_2: 'LEC',
//     fav_team: 'RBR'
//   }
// ][
//

async function getDriverById(driverId){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM drivers WHERE driver_id = ?', [driverId]);
    return rows[0];}finally{
        await db.end();
    }
}
// {
// driver_id: 'GAS',
// first_name: 'Pierre',
// last_name: 'Gasly',
// dob: '1996-02-07',
// nationality: 'French',
// code: 'GAS',
// team_id: 'ALP'

async function getTeamById(teamId){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM teams WHERE team_id = ?', [teamId]);
    return rows[0];}finally{
        await db.end();
    }

}
//{
// team_id: 'RBR',
// name: 'Red Bull Racing',
// nationality: 'Austrian'
// }

async function getTeamStandings(season){
    const db = await connectdb();
    try{

const [rows] = await db.query('SELECT * FROM team_standings WHERE season = ?', [season]);
return rows;}finally{
    await db.end();
    }
}
// standing per sepecific season
// {
//     season: '2023',
//     round: 1,
//     team_id: 'RBR',
//     points: 709,
//     position: 1,
//     wins: 0,



async function getDriverStandings(season){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM driver_standings WHERE season = ?', [season]);
    return rows;}finally{
        await db.end();
    }
}
//drivers standings per specific season
//     season: '2023',
//     round: 1,
//     driver_id: 'VER',
//     points: 454,
//     position: 1,
//     wins: 0,


async function getAllTeamInfo(){
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM teams');
    return rows;}finally{
        await db.end();
    }
}
//{
// team_id: 'RBR',
// name: 'Red Bull Racing',
// nationality: 'Austrian'
// }

async function getAllDriverInfo(){  
    const db = await connectdb();
    try{
    const [rows] = await db.query('SELECT * FROM drivers');
    return rows;}finally{
        await db.end();
    }
}
//{
// team_id: 'RBR',
// name: 'Red Bull Racing',
// nationality: 'Austrian'
// }