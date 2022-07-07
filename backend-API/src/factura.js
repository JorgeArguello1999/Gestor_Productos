const express = require('express');
const router = express.Router();

// Conector de la base de datos
const mariadb = require('../src/database');

// Obtenemos todas las facturas
/**
 * Esta tabla o funcion de la base de datos tiene como funcion mostar el estado del negocio
 * no es tanto para modificarse continuamente, es como un registro, tambien va a tener otras 
 * funcionalidades como la siguientes:
 * - Mostar Ingresos que tiene el negocio (Total de las ventas)
 * - Llevar registros y tener la funcion de usarse para crear estadisticas
 * - Los clientes van a poder ver en que gastaron o compraron.
 */
router.get('/', (req, res) => {
  mariadb.query('SELECT * FROM factura', (err, rows, fields) => {
    if(!err) {
      res.json(rows);
      console.log(rows);
    } else {
      console.log(err);
    }
  });  
});

// Consultar facutura 
router.get('/:id', (req, res) => {
  const { id } = req.params; 
  mariadb.query('SELECT * FROM factura WHERE id = ?', [id], (err, rows, fields) => {
    if (!err) {
      res.json(rows[0]);
    } else {
      console.log(err);
    }
  });
});

// Configurar
// Insertar factura 
router.post('/', (req, res) => {
  const { clientes, fecha, ciudad, compras, subtotal, descuento, iva, total } = req.body;
  const query = `insert into factura (clientes, fecha, ciudad, compras, subtotal, descuento, iva, total) values (?,?,?,?,?,?)`;
  mariadb.query(query, [clientes, fecha, ciudad, compras, subtotal, descuento, iva, total], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Factura guardada'});
    } else {
      console.log(err);
    }
  });
});

// Editar factura 
router.put('/:id', (req, res) => {
  const { clientes, fecha, ciudad, compras, subtotal, descuento, iva, total } = req.body;
  const query = `update factura set clientes=?, fecha=?, ciudad=?, compras=?, subtotal=?, descuento=?, iva=?, total=?`;
  mariadb.query(query, [clientes, fecha, ciudad, compras, subtotal, descuento, iva, total], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Factura actualizado'});
    } else {
      console.log(err);
    }
  });
});

// Eliminar factura 
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  mariadb.query('DELETE FROM factura WHERE id = ?', [id], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Factura Eliminado'});
    } else {
      console.log(err);
    }
  });
});

module.exports = router;
