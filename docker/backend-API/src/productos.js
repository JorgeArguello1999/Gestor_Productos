const express = require('express');
const router = express.Router();

// Conector de la base de datos
const mariadb = require('../src/database');

// Obtenemos todos los productos
router.get('/', (req, res) => {
  mariadb.query('SELECT * FROM productos', (err, rows, fields) => {
    if(!err) {
      res.json(rows);
      console.log(rows);
    } else {
      console.log(err);
    }
  }); 
});

// Consultar un productos
router.get('/:id', (req, res) => {
  const { id } = req.params;
  mariadb.query('SELECT * FROM productos WHERE id = ?', [id], (err, rows, fields) => {
    if(!err){
      res.json(rows);
      console.log(rows);
    }else{
      console.log(err);
    }
  });
});

// Insertar productos
/**
 * Aquí una observación en la inserción del valor total, tener cuidado ya que es una operacion 
 * matematica y no debe ser ingresado manualmente, tener en cuenta para la GUI sea desktop o 
 * WEB
*/
router.post('/', (req, res) => {
  const { nombre, cantidad, precio, valor_total, foto_producto } = req.body;
  const query = `insert into productos (nombre, cantidad, precio, valor_total, foto_producto) values (?, ?, ?, ?; ?)`;
  mariadb.query(query, [nombre, cantidad, precio, valor_total, foto_producto], (err, rows, fields) =>{
    if(!err){
      res.json('Producto Guardado');
    }else{
      console.log(err);
    }
  });
});

// Editar producto
router.put('/:id', (req, res) => {
  const { nombre, cantidad, precio, valor_total, foto_producto } = req.body;
  const query =`update productos set nombre=?, cantidad=?, precio=?, valor_total=?, foto_producto=?`;
  mariadb.query(query, [nombre, cantidad, precio, valor_total, foto_producto], (err, rows, fields) => {
    if(!err){
      res.json('Producto Editado');
    }else{
      console.log(err);
    }
  });
});

// Eliminar producto
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  mariadb.query(`DELETE FROM productos WHERE id = ?`, [id], (err, rows, fiels) => {
    if(!err){
      res.json('Producto Eliminado');
    }else{
      console.log(err);
    }
  });
});

module.exports = router;
