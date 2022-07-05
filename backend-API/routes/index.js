// Sirve para traer el modulo principal o anidarlo
const { Router }= require('express');
const router= Router(); 

// Rutas
router.get('/', (req, res) => {
	res.json('Hola');
});

module.exports= router;
