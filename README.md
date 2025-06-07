PyGame Challenge
----------------

**Matrix Digital Rain**

This challenge focuses on recreating the "raining code" sequence from The Matrix. 

**Challenge**

Recreate the digital rain sequence from The Matrix. 

Full challenge info: https://www.reddit.com/r/pygame/comments/4jg5cf/challenge_matrix_digital_rain/


# 🟢 Matrix Rain Name Reveal

This project is a fullscreen cinematic **"Matrix rain" name reveal application** built with `pygame`. It features interactive animations, sound effects, and real-time text transitions for dramatic presentations—ideal for games, events, and randomized player selection.

---

## 🧩 Features

### 🟩 Matrix Rain Animation
Real-time vertical streams of characters, each forming names from a list, simulate the iconic "Matrix" effect in a fully animated backdrop.

### ⌨️ Typing Animation for Top Banner
A glowing "Choose Your Player" message appears with a typing effect for suspense.

### 🔀 Name Shuffling
After the intro, a **bottom name box** begins shuffling random names from a large name pool. Pressing `Enter` stops the shuffling and reveals a selected name.

### ✨ Glowing Text & Box Effects
UI elements glow softly with layered render passes and opacity effects, styled to resemble digital terminals.

### 🔊 Sound Integration
- Ambient background hum
- Shuffle effect
- Glitch pings
- Dramatic name reveal sound

(All sounds are loaded from `resources/sounds/` and must be provided by the user.)

### 🎉 Name Reveal
Upon pressing `Enter` during shuffling, a name from the predefined `reveal_names` list is revealed with a glowing animation. Pressing `Enter` again continues to the next name in the cycle.

---

## 🕹 Controls

| Key         | Action                                  |
|-------------|------------------------------------------|
| `Enter`     | Start shuffle / Reveal next name         |
| `Esc`       | Exit the program                         |
| `Return` x2 | Moves through all names in `reveal_names`|

---

## ✅ Requirements

- Python 3.7+
- pygame (`pip install pygame`)

---

## 🚀 How to Run

```bash
python matrix_v2.2.py
