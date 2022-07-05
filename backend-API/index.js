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

app.get('/', (req, res) => {
	res.send("Hola");
});

app.listen(app.get('port'),() => {
	console.log(`listen on port: ${app.get('port')}`);
});
