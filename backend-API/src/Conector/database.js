const mariadb = require('mariadb');

const conn = mariadb.createConnection({
		host: '192.168.1.13',
		user: 'root',
		password: 'root',
		port: 3306,
		database: 'aplicacion'
});

conn.connect( function (err) {
	if(err){
		console.error(err);
		return;
	}else{
		console.log('Database is connect');
	}
});

module.exports = conn;
