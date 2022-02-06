import db_connect

db= db_connect.usuarios()
# db.insertar(2, 'Jorge', 'contrasena', 'admin')
# db.verificador('Jorge', 'contrasena')
# db.eliminar(2, 'Jorge', 'contrasena', 'admin')
db.editar(1, 'Juan', 'Pilancho', 'admin')
