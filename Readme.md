# Simple Finance App

A lightweight personal finance dashboard built with Streamlit. Upload a CSV of your bank transactions and the app splits them into expenses and payments, lets you sort expenses into categories, remembers those categories for next time, and shows where your money goes with a summary table and a pie chart.

## Features

* Upload any bank transaction export in CSV format
* Automatic split into Expenses (debits) and Payments (credits)
* Create your own spending categories
* Assign categories directly inside an editable table
* The app learns: once you categorise a transaction, future transactions with the same details are categorised automatically
* Categories are saved to a local `categories.json` file so they persist between sessions
* Expense summary table sorted from highest to lowest spend
* Interactive pie chart of expenses by category
* Total payments shown as a headline metric

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web interface and interactive widgets |
| Pandas | Reading, cleaning and grouping transaction data |
| Plotly Express | Interactive charts |

## Project Structure

```
simple-finance-app/
├── main.py             # Main Streamlit application
├── requirements.txt    # Python dependencies
├── categories.json     # Saved categories and keywords (created automatically)
└── README.md           # Project documentation
```

## Prerequisites

* Python 3.9 or newer
* pip (comes with Python)
* VS Code (optional, but recommended)

You can check your Python version with:

```bash
python --version
```

## Installation

### 1. Open the project in VS Code

Open the project folder in VS Code, then open a terminal with **Terminal > New Terminal**.

### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your system.

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (Command Prompt or PowerShell):**

```bash
venv\Scripts\activate
```

**macOS or Linux:**

```bash
source venv/bin/activate
```

When it is active, you will see `(venv)` at the start of your terminal line.

### 4. Install the dependencies using requirements.txt

The `requirements.txt` file lists every package the app needs. Install them all in one command:

```bash
pip install -r requirements.txt
```

The `-r` flag tells pip to read package names from the file instead of typing them one by one.

To confirm everything installed correctly:

```bash
pip list
```

You should see `streamlit`, `pandas` and `plotly` in the list.

### Updating requirements.txt

If you add a new package to the project later, install it and then add it to the file so others can install it too. For example:

```bash
pip install numpy
```

Then add this line to `requirements.txt`:

```
numpy>=1.26.0
```

## Running the App

With the virtual environment active, run:

```bash
streamlit run main.py
```

Streamlit will open the app in your browser automatically, usually at `http://localhost:8501`. To stop the app, press `Ctrl + C` in the terminal.

## CSV File Format

The app expects a CSV file with these column headers:

| Column | Description | Example |
|--------|-------------|---------|
| Date | Transaction date in `DD Mon YYYY` format | `05 Jan 2025` |
| Details | Description of the transaction | `CARREFOUR DUBAI` |
| Amount | Transaction amount as text, commas allowed | `"1,250.00"` |
| Debit/Credit | Either `Debit` or `Credit` | `Debit` |

Example file:

```csv
Date,Details,Amount,Debit/Credit
05 Jan 2025,CARREFOUR DUBAI,"1,250.00",Debit
07 Jan 2025,NETFLIX SUBSCRIPTION,39.00,Debit
10 Jan 2025,SALARY JANUARY,"12,000.00",Credit
12 Jan 2025,CARREFOUR DUBAI,845.50,Debit
```

Column names must match exactly, including capital letters and the slash in `Debit/Credit`. Extra spaces around column names are removed automatically.

## How to Use

1. Start the app and click **Browse files** to upload your transaction CSV.
2. Open the **Expenses(Debits)** tab to see all your spending.
3. Type a name into **New Category Name** (for example `Groceries`) and click **Add Category**.
4. In the **Your expenses** table, click a cell in the **Category** column and choose a category from the dropdown.
5. Click **Apply Changes** to save your choices.
6. Scroll down to see the **Expense Summary** table and the pie chart.
7. Open the **Payments(Credits)** tab to see your total payments and all incoming transactions.

## How Automatic Categorisation Works

When you assign a category to a transaction and click **Apply Changes**, the transaction's `Details` text is saved as a keyword for that category in `categories.json`.

The next time you upload a file, any transaction whose `Details` exactly matches a saved keyword (ignoring upper and lower case) is placed in that category automatically. Everything else starts as `Uncategorized`.

For example, after you mark `CARREFOUR DUBAI` as `Groceries` once, every future `CARREFOUR DUBAI` transaction will be categorised as `Groceries` without any extra work.

To reset all categories, delete `categories.json` and restart the app.

## Troubleshooting

### `streamlit` is not recognised as a command

Make sure your virtual environment is activated, then run `pip install -r requirements.txt` again.

### Error processing file

Check that your CSV has the exact column names listed above and that dates follow the `05 Jan 2025` format.

### VS Code is using the wrong Python

Press `Ctrl + Shift + P`, search for **Python: Select Interpreter**, and choose the one inside your `venv` folder.

### Categories are not saved between sessions

Check that the app has permission to create files in the project folder.

## Future Improvements

* Partial keyword matching instead of exact matching
* Monthly and weekly spending trends
* Support for multiple date formats and bank export styles
* Budget limits with alerts per category
* Export categorised data back to CSV

## License

This project is open source and available for personal and educational use.