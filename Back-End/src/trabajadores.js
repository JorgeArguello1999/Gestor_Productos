const express = require('express');
const router = express.Router();

// Conector de la base de datos
const mariadb= require('../src/database');

// Obtener todos los trabajadores
router.get('/', (req, res) => {
  mariadb.query('SELECT * FROM trabajadores', (err, rows, fields) => {
    if(!err) {
      res.json(rows);
      console.log(rows);
    } else {
      console.log(err);
    }
  });  
});

// Consultar trabajadores
router.get('/:id', (req, res) => {
  const { id } = req.params; 
  mariadb.query('SELECT * FROM trabajadores WHERE id = ?', [id], (err, rows, fields) => {
    if (!err) {
      res.json(rows[0]);
    } else {
      console.log(err);
    }
  });
});

// Insertar trabajadores
router.post('/', (req, res) => {
  const { nombres, apellidos, cedula, correo, direccion, telefono, area, foto_trabajador } = req.body;
  const query = `insert into trabajadores (nombres, apellidos, cedula, correo, direccion, telefono, area, foto_trabajador) values (?,?,?,?,?,?,?,?)`;
  mariadb.query(query, [nombres, apellidos, cedula, correo, direccion, telefono, area, foto_trabajador], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Trabajador guardado'});
    } else {
      console.log(err);
    }
  });
});

// Editar trabajador
router.put('/:id', (req, res) => {
  const { nombres, apellidos, cedula, correo, direccion, telefono, area, foto_trabajador } = req.body;
  const query = `update trabajadores set nombres=?, apellidos=?, cedula=?, correo=?, direccion=?, telefono=?, area=?, foto_trabajador=? `;
  mariadb.query(query, [nombres, apellidos, cedula, correo, direccion, telefono, area, foto_trabajador], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Trabajador actualizado'});
    } else {
      console.log(err);
    }
  });
});

// Eliminar trabajador
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  mariadb.query('DELETE FROM trabajadores WHERE id = ?', [id], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Trabajador Eliminado'});
    } else {
      console.log(err);
    }
  });
});

// Login
router.get('/login/:cedula',(req, res) => {
  const { cedula } = req.params;
  console.log('si funciono no preocupacion');
  console.log(cedula)
  mariadb.query('SELECT * FROM trabajadores WHERE cedula=?', [cedula], (err, rows) =>{
    if (!err) {
      res.json(rows[0]);
    } else {
      console.log(err);
    }
  });
});

module.exports = router;
