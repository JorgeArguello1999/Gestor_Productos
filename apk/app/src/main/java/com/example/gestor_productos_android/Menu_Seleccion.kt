package com.example.gestor_productos_android

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView

class Menu_Seleccion : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_menu_seleccion)

        /***
         * Esta es el menu de seleccion (guiarse en los bocetos de la agenda) aqui se trabajar mas
         * que todo en el menu de elección, por ejemplo:
         * - Creacion, Edición y Borrar Usuaarios (Para esto existira un conjunto de botones)
         * - Creación, Edición y Borrar Productos (Igual existira un conjunto de botones)
         *
         * Lo que queremos lograr es tener todo de una forma separada y simple de tal forma que
         * se pueda usar con facilidad, no queremos llenar al usuario de muchas opciones, solo las
         * fundamentales.
         */

        // Obtenemos los datos del menu->MainActivity
        var nombre= findViewById<TextView>(R.id.menu_usuario)
        var usuario:String?= intent.getStringExtra("usuario")
        nombre.text= usuario
    }
}