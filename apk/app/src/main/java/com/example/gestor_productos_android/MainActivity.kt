package com.example.gestor_productos_android

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import com.google.android.material.textfield.TextInputEditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Desde aqui es todo expermiental

        // Obtenemos la entrada del EditText
        val usuario= findViewById<EditText>(R.id.usuario)
        val password= findViewById<EditText>(R.id.password)

        // Debemos crear el modulo para conectarnos a la base de datos
        /***
         * Para este proyecot el sistema de verificacion con baase de datos es en texto plano
         * no se va a usar un cifrado especial de parte del codigo, se piensa hacerlo desde
         * la parte de SQL
         *
         * El modulo de conexión, verificara los usuarios en el MainActivity y luego devolvera
         * un 1 o un 0 según corresponda, esto sera enviado a la siguiente activity
         * */

        // Pasamos a la Siguiente Activity
        // Obtenemos el Id del boton
        val boton= findViewById<Button>(R.id.boton_ingresar)
        // Programamos el evento del click
        boton.setOnClickListener{
            // Cuando el boton sea presionado se ejecutara lo sigueinte
            // Usar intent como nombre de la variable, es una palabra reservada
            val intent= Intent(this, Menu_Seleccion::class.java)

            // Enviamos el contenido a la otra Activity
            // Usamos el .text.toString() -> Para enviar solo texto
            intent.putExtra("usuario", usuario.text.toString())

            // Iniciamos el Activity
            startActivity(intent)
        }


    }
}