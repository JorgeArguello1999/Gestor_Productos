package com.example.gestor_productos_android

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import com.google.android.material.textfield.TextInputEditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Desde aqui es todo expermiental
        val usuario= findViewById<EditText>(R.id.usuario)
        val password= findViewById<EditText>(R.id.password)

        // Debemos crear el modulo para conectarnos a la base de datos

    }
}