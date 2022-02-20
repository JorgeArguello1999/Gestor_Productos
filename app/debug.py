import db_connect

db= db_connect.usuarios()
#db.insertar(1, 'Juan', 'Pilancho', 'admin')
# db.verificador('Juan', 'Pilancho')
# db.eliminar(1, 'Juan', 'Pilancho', 'admin')
# db.editar(1, 'Juan', 'Pilancho', 'admin')
# db.detector(2, 'Jorge', 'contrasena', 'admin')

dbc= db_connect.conexion()
admin= dbc.admin('Jorge', 'contrasena')
print(admin)
