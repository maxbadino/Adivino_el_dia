package com.example.levelgame

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private var level = 1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val levelText: TextView = findViewById(R.id.levelText)
        val nextLevelButton: Button = findViewById(R.id.nextLevelButton)

        updateLevelText(levelText)

        nextLevelButton.setOnClickListener {
            level += 1
            updateLevelText(levelText)
        }
    }

    private fun updateLevelText(view: TextView) {
        view.text = "Nivel actual: $level"
    }
}
