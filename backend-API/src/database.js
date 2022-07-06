const mysql = require('mysql2');

const mysqlConnection = mysql.createConnection({
  host: '192.168.1.13',
  user: 'root',
  database: 'aplicacion',
  password: 'root',
  // multipleStatements: true
});
mysqlConnection.connect(function (err) {
  if (err) {
    console.error(err);
    return;
  } else {
    console.log('db is connected');
  }
});
module.exports = mysqlConnection;
