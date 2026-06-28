# 🏦 Bank Management System

A menu-driven Bank Management System developed using **Python** and **MySQL**. This project allows users to create bank accounts, view account details, deposit money, and withdraw money through a simple command-line interface.

---

## 📌 Features

* Create a new bank account
* View customer account details
* Deposit money into an account
* Withdraw money with balance validation
* Automatic account number generation
* MySQL database integration
* Menu-driven user interface

---

## 🛠️ Tech Stack

* Python 3.x
* MySQL
* mysql-connector-python

---

## 📂 Project Structure

```
Bank-Management-System/
│── main.py
│── bank_system.sql
│── requirements.txt
│── README.md
```

---

## 🗄️ Database Schema

### Database

```
bank_system
```

### Customers Table

| Column      | Data Type         |
| ----------- | ----------------- |
| customer_id | INT (Primary Key) |
| account_no  | BIGINT (Unique)   |
| name        | VARCHAR(100)      |
| phone       | VARCHAR(15)       |
| balance     | DECIMAL(10,2)     |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Bank-Management-System.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create the database

```sql
CREATE DATABASE bank_system;
```

Run the SQL script:

```sql
SOURCE bank_system.sql;
```

### Run the application

```bash
python main.py
```

---

## 📷 Sample Output

```
========== BANK MANAGEMENT SYSTEM ==========
1. Create Account
2. View Account
3. Deposit Money
4. Withdraw Money
5. Exit

Enter your choice:
```

---

## 📚 Concepts Used

* Python Programming
* MySQL Database
* CRUD Operations
* SQL Queries
* Loops
* Conditional Statements
* Functions
* User Input Handling

---

## 🚀 Future Improvements

* Admin Login
* Transaction History
* Fund Transfer
* Customer Login
* PIN Authentication
* GUI using Tkinter
* Export Reports to Excel/PDF

---

## 👨‍💻 Author

**Tejas Jamnare**

Computer Science Engineer | Data Analyst | Python & SQL Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.

