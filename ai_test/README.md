# ai_test

A collection of Python utility programs and tools.

## Projects

### Login Portal (`login_app.py`)
A user registration and management system.

**Features:**
- Register users with name, surname, age, country, province, and password
- Denies access to users under 18
- Saves registered users to `users.json` with hashed passwords
- View, edit, and delete registered users

**Run:**
```bash
python3 login_app.py
```

---

### Quiz Game (`quiz_game.py`)
A multiple choice quiz game with 25 questions.

**Features:**
- Questions covering geography, science, math, history, art, sports, and technology
- Questions are shuffled every game
- Tracks score and displays a performance message at the end

**Run:**
```bash
python3 quiz_game.py
```

---

### Pizza Recipe Maker (`pizza.py`)
An interactive pizza recipe builder.

**Features:**
- Choose from 5 sizes, 4 crusts, 5 bases, 5 cheeses, 12 toppings, and a finishing drizzle
- Generates a step-by-step recipe based on your selections

**Run:**
```bash
python3 pizza.py
```

---

### Weather App (`weather_app.py`)
Real-time weather and 5-day forecast for any city.

**Features:**
- Current temperature, humidity, wind speed, and conditions
- 5-day forecast with daily high/low and rainfall
- No API key required (uses Open-Meteo)

**Run:**
```bash
python3 weather_app.py
```

---

### Calculator (`calculator.py`)
Basic and scientific calculator.

**Features:**
- Basic operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Scientific: `sqrt`, `sin`, `cos`, `tan`, `log`, `log10`

**Run:**
```bash
python3 calculator.py
```

---

### To-Do List (`todo_list.py`)
Task manager that saves tasks to a file.

**Features:**
- Add, view, complete, and delete tasks
- Tasks saved to `tasks.json`

**Run:**
```bash
python3 todo_list.py
```

---

### Currency Converter (`currency_converter.py`)
Live currency conversion using real-time exchange rates.

**Features:**
- Supports all major world currencies
- Fetches live rates from open.er-api.com

**Run:**
```bash
python3 currency_converter.py
```

---

### Password Generator (`password_generator.py`)
Generate strong random passwords.

**Features:**
- Customise length, uppercase, numbers, and symbols
- Generate up to 10 passwords at once
- Displays password strength rating

**Run:**
```bash
python3 password_generator.py
```

---

### Countdown Timer (`countdown_timer.py`)
Set a countdown timer by hours, minutes, and seconds.

**Features:**
- Live countdown display
- Alert when time is up

**Run:**
```bash
python3 countdown_timer.py
```

---

### BMI Calculator (`bmi_calculator.py`)
Calculate Body Mass Index in metric or imperial units.

**Features:**
- Supports kg/cm and lbs/inches
- Displays BMI category (Underweight, Normal, Overweight, Obese)

**Run:**
```bash
python3 bmi_calculator.py
```

---

### Unit Converter (`unit_converter.py`)
Convert between common units of measurement.

**Features:**
- Length: km/miles, metres/feet
- Weight: kg/lbs, grams/ounces
- Temperature: Celsius, Fahrenheit, Kelvin
- Speed: km/h, mph, m/s

**Run:**
```bash
python3 unit_converter.py
```

---

## Setup

### Requirements
- Python 3.x

### Atlassian Integration
Copy the environment template and fill in your credentials:
```bash
cp services/atlassian/.env.example services/atlassian/.env
```

Edit `services/atlassian/.env` with your details:
```
ATLASSIAN_URL=https://your-company.atlassian.net
ATLASSIAN_EMAIL=your-email@company.com
ATLASSIAN_API_TOKEN=your_api_token_here
```
