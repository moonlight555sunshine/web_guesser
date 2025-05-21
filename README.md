# 🧠 Web Number Guesser (Flask App)

This is a simple web application where the computer tries to guess the number you're thinking of between 0 and 1000. It uses a **binary search algorithm** to find the number in 10 or fewer attempts.

Built with Flask, it runs in your browser and provides an interactive guessing experience.

---

## 🚀 How It Works

1. You think of a number between **0 and 1000**.
2. The computer makes a guess.
3. You respond with one of:
   - `Too small`
   - `Too big`
   - `Correct`
4. Based on your feedback, the app adjusts its guessing range and tries again.
5. The game continues until the computer wins.

---

## 🛠 Technologies

- Python 3
- Flask
- HTML

---

## ▶️ Running the App

### 1. Install Flask (if you haven't):

```bash
  pip install -r requirements.txt
```
### 2. Run the app
```bash
    python main.py
```

### 3. Open in browser:
Go to: http://127.0.0.1:5000/web_guesser

## 📁 Project Structure
```bash
project/
│
├── main.py              # Main Flask app
├── templates/
│   ├── welcome.html    # Start screen
│   └── main.html       # Game interaction screen
└── README.md           # This file
```

## 💡 Notes
- All user input is through buttons (no typing required).
- The app uses hidden form fields to keep track of the current min/max range between requests.
- The guessing logic uses binary search to optimize the number of attempts.