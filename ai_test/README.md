# ai_test

A collection of Python programs including a login portal, quiz game, and pizza recipe maker.

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
