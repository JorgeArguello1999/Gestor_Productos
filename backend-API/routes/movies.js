const { Router } = require('express');
const router= Router(); 

// Importamos libreria Underscore utilizada para manejar JSON
const __ = require("underscore");

const movies = require('../sample.json');
console.log(movies);

// Rutas
router.get('/', (req, res) => { 
	res.json(movies);
});

router.post('/', (req, res) => {
	const { title, year }= req.body;
	if(title && year){
		const id= movies.length + 1;
		const newMovies= {...req.body, id};
		console.log(newMovies);
		movies.push(newMovies);
		res.json(movies);
	}else{
		res.send("Wrong in Request");
	}
});

router.delete('/:id', (req, res) => {
	const { id }= req.params;
	__.each(movies, (movie, i) => {
		if(movie.id == id){
			movies.splice(i, 1);
		}
	});
	res.send(movies);
});

router.put('/', (req, res) => {
	const { id } = req.params;
	const {title, year}= req.params;

	
});

module.exports= router;
