import db_connect

db= db_connect.usuarios()
db.insertar(2, 'Jorge', 'contrasena', 'admin')
# db.verificador('Juan', 'Pilancho')
db.eliminar(1, 'Juan', 'Pilancho', 'admin')
# db.editar(1, 'Juan', 'Pilancho', 'admin')
