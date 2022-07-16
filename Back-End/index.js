const morgan = require('morgan');
const express = require('express');
const app = express();

// Configuraciones del server
app.set('port', 3000);

// Añadimos el entendimiento JSON
app.use(express.json());

// Morgan para tener colores en la consola :3
app.use(morgan('dev'));

// Rutas para la API
// Tabla trabajadores
app.use('/api/trabajadores/', require('./src/trabajadores'));

// Tabla clientes
app.use('/api/clientes/', require('./src/clientes'));

// Tabla de productos
app.use('/api/productos/', require('./src/productos'));

// Tabla de facturas
app.use('/api/factura/', require('./src/factura'));

app.listen(app.get('port'),() => {
	console.log(`Server en puerto: ${app.get('port')}`);
	console.log("Conected");
});
