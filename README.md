# 🧻 Toilet Paper Tracker

A completely unnecessary command-line tool that lets you log every time you use toilet paper. Tracks squares used, logs sessions with timestamps and locations, and gives you totally unhelpful statistics like average squares used, most wasteful sessions, and usage trends over time.

Yes, it's ridiculous. Yes, it's real.

## 💡 Why?

Because I **could**. And that’s reason enough.

Plus:

- Learn basic file logging and parsing
- Practice CLI interaction and simple data analytics
- Gain totally useless insight into your... habits

## 🚀 Features

- Log each toilet paper usage session with:
  - Timestamp (date and time)
  - Number of squares used
  - Location
  - Optional notes

- View useful-but-not-really stats:
  - Total and average squares used
  - Most wasteful single session
  - Count and ranking of usage locations

- See your usage plotted over time in your terminal

- Raw stats output to see the plain CSV data

## ⚙️ Installation

Make sure Python 3.6+ is installed.

Install dependencies with:

```bash
pip install plotext
```

### 🐍 Optional: Set up a Virtual Environment and Install Dependencies

To keep your Python environment clean and isolated, you can create a virtual environment and install dependencies as follows.

1. **Create the virtual environment** (one-time setup):

```bash
python3 -m venv .venv
```

2. **Activate the virtual environment**:

- On macOS/Linux:

```bash
source .venv/bin/activate
```

- On Windows:

```bash
.venv\Scripts\activate
```

3. **Install dependencies from `requirements.txt`**:

```bash
pip install -r requirements.txt
```

4. **Run the application inside the virtual environment**:

```bash
python tpt.py --add
```

5. **Deactivate the environment when done**:

```bash
deactivate
```

## 📖 Usage

Run the script with one of these commands:

```bash
# Add a new toilet paper usage entry
python tpt.py --add

# Display formatted usage statistics
python tpt.py --stats

# Display raw CSV stats
python tpt.py --stats raw

# Plot toilet paper usage graph over time in terminal
python tpt.py --graph
```

### Examples

```
$ python3 tpt.py --add
How many square did you use? : 20
Where did you do your business? : Home
Do you want to take any notes about IT? : Post-spicy dinner
🧻Logged: 20 squares, at Home. Notes: 'Post-spicy dinner'

$ python3 tpt.py --stats
🧻 Toilet Paper Stats
---------------------------------
Total entries: 5
Total squares used until now: 135
Average squares used: 27.0
Most wasteful session: 40 squares on 01/Aug/2025 08:15
Number of place where you did it: 2
Top three location where you did it:
  🥇 Home: 3 times
  🥈 Office: 2 times

$ python tpt.py --graph
```

## 🔧 How it works

- Data is stored in a CSV file named `testData.csv` in the same directory as the script.
- If the file or database doesn’t exist, it will be created automatically when logging an entry.
- The CSV columns are `timestamp,squares,location,notes`.
- Statistics and graphing are generated directly from this file.
- Uses `plotext` to render usage graphs right in your terminal.

## 🏗️ Development Notes

- Written in Python 3
- Uses `argparse` for CLI interaction
- Uses `csv` module for CSV handling
- Uses `collections.Counter` for counting locations
- Uses `plotext` for terminal plots

## 📦 requirements.txt

```bash
plotext
```

## 🐚 Optional Setup Script (macOS/Linux)

You can create a helper shell script `setup_env.sh` to automate venv creation and dependency installation:

```bash
#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Virtual environment created and dependencies installed."
echo "Activate with: source .venv/bin/activate"
```

Make it executable:

```bash
chmod +x setup_env.sh
```

and run with:

```bash
./setup_env.sh
```

---

## License

This project is absurd but free to use, copy, and modify. If you want to fork it to track any other usage stats, go wild!
