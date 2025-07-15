# 💳 ATM System Simulator (Python)

This project is a simple **ATM system simulator** built in Python using **object-oriented programming (OOP)**. It replicates core banking operations such as user login, balance management, and transaction history in a console-based environment.

## 🚀 Features

* ✅ User authentication with **User ID** and **PIN**
* 💰 Deposit, Withdraw, and Transfer functionalities
* 📜 Transaction history tracking for each user
* 🧱 Clean OOP structure using classes (`UserAccount`, `ATM`)
* 🧪 Sample user accounts preloaded for quick testing

## 🛠️ How It Works

1. The program starts by initializing a few sample user accounts.
2. Users log in using their User ID and PIN.
3. After successful login, users can:

   * Deposit money
   * Withdraw funds
   * Transfer to another user
   * View transaction history
   * Quit the session
4. All transactions are logged in memory.

> **Note:** This is a basic simulation. No real banking systems or databases are connected. All account information is stored in memory during runtime.

## 📁 Project Structure

```
ATM-System/
│
├── atm.py              # Main script with ATM logic
├── README.md           # Project documentation
```

## 👨‍💻 Technologies Used

* Programming Language: **Python 3**
* Concepts: **OOP**, **File Structure**, **Input Validation**

## 🧪 Sample Accounts

| User ID   | PIN  | Balance   |
| --------- | ---- | --------- |
| `me`      | 2004 | ₹10,000   |
| `octanet` | 2024 | ₹1,00,000 |
| `intern`  | 2023 | ₹1,000    |

## 🧠 Learning Outcome

* Implemented Python classes and methods to simulate real-world systems
* Gained hands-on experience in structuring user interaction flow
* Learned to handle basic validation and user feedback in CLI-based programs

## 📌 Run the Project

```bash
# Clone the repository
git clone https://github.com/Shafrinnisha/atm.git

# Change directory
cd atm

# Run the script
python atm.py
```

## 🤝 Acknowledgment

This project was built as part of my internship at **OctaNet** under the **Python Development** domain.
