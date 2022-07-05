// Importamos Express
const express= require("express");
const app= express();

// Importamos un Middleware llamado morgan
const morgan= require('morgan');
app.use(morgan('dev'));

// Intregramos el modulo de Express que entiende JSON
app.use(express.json());

// Entendemos las peticiones que vienen de URL
app.use(express.urlencoded({extended: false}));

// Seteamos configuraciones de Express
app.set('port', 3000); 

// Para la pagina principal
app.use('',require('./routes/index'));

// Para la parte de la API
app.use('/api/movies', require('./routes/movies'));

app.listen(app.get('port'),() => {
	console.log(`listen on port: ${app.get('port')}`);
});
