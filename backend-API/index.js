const express= require("express");
const app= express();

// Importamos un Middleware llamado morgan
const morgan= require('morgan');
app.use(morgan('dev'));
app.use(express.json());

// Configuración de Express
app.set("view engine", 'ejs');

// Usamos la home /
app.get('/', (req, res) => {
	const datos= [{Usuario : "Jorge"}, {Usuario : "Joe"}, {Usuario: "Cris"}];
	// Enviamos datos a la vista a traves de la variable personas paso el valor datos
	res.render('index.ejs', {personas: datos});
});

// Esto funciona como punto de control
app.all('/user/', (req, res, next) => {
	console.log("Por aquí paso");
	next();
});

// Enviamos una consulta get y nos devuelve un JSON
app.get('/user', (req, res) => {
	res.json({
		"username": "Jorge",
		"password": "contraseña"
	});
});

/**
 * Enviamos una consulta post y debemos recivir un JSON 
 * Se puede usar la ruta /user ya que son funciones diferentes
 * por lo tanto no generan conflicto entre ambas funciones
*/
app.post('/user', (req, res) => {
	console.log(req.body);
	res.send('<h1>Se a Recivido</h1>');
});

// Obteniendo una variable por url 
// localhost:3000/id/43 -> Esto puede cambiar
app.post('/id/:id', (req, res) => {
	res.send('<h2>ID recivido</h2>');
	console.log(req.params);
});

app.delete('/eliminar/:id_usuario', (req, res) => {
	res.send(`Usuario: ${req.params.id_usuario} ha sido eliminado`);
});

app.use(express.static('public'));

app.listen(3000,() => {
	console.log("listen on port: 3000");
});
