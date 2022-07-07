const express = require('express');
const router = express.Router();

// Conector de la base de datos
const mariadb= require('../src/database');

// Obtener todos los clientes 
router.get('/', (req, res) => {
  mariadb.query('SELECT * FROM clientes', (err, rows, fields) => {
    if(!err) {
      res.json(rows);
      console.log(rows);
    } else {
      console.log(err);
    }
  });  
});

// Consultar clientes 
router.get('/:id', (req, res) => {
  const { id } = req.params; 
  mariadb.query('SELECT * FROM clientes WHERE id = ?', [id], (err, rows, fields) => {
    if (!err) {
      res.json(rows[0]);
    } else {
      console.log(err);
    }
  });
});

// Insertar clientes 
router.post('/', (req, res) => {
  const { nombres, apellidos, cedula, correo, direccion, telefono } = req.body;
  const query = `insert into clientes (nombres, apellidos, cedula, correo, direccion, telefono) values (?,?,?,?,?,?)`;
  mariadb.query(query, [nombres, apellidos, cedula, correo, direccion, telefono], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Cliente guardado'});
    } else {
      console.log(err);
    }
  });
});

// Editar cliente
router.put('/:id', (req, res) => {
  const { nombres, apellidos, cedula, correo, direccion, telefono } = req.body;
  const query = `update clientes set nombres=?, apellidos=?, cedula=?, correo=?, direccion=?, telefono=?`;
  mariadb.query(query, [nombres, apellidos, cedula, correo, direccion, telefono], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Cliente actualizado'});
    } else {
      console.log(err);
    }
  });
});

// Eliminar cliente 
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  mariadb.query('DELETE FROM clientes WHERE id = ?', [id], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Cliente Eliminado'});
    } else {
      console.log(err);
    }
  });
});

module.exports = router;
