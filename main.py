import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",      
    database="bank_system"
)

cursor = conn.cursor()

while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")

        account_no = random.randint(10000000, 99999999)
        balance = 0.00

        query = """
        INSERT INTO customers(account_no, name, phone, balance)
        VALUES(%s, %s, %s, %s)
        """

        values = (account_no, name, phone, balance)

        cursor.execute(query, values)
        conn.commit()

        print("\n✅ Account Created Successfully")
        print("Account Number:", account_no)

    elif choice == "2":

        account_no = input("Enter Account Number: ")

        query = "SELECT * FROM customers WHERE account_no = %s"

        cursor.execute(query, (account_no,))
        customer = cursor.fetchone()

        if customer:

            print("\n------ CUSTOMER DETAILS ------")
            print("Customer ID :", customer[0])
            print("Account No  :", customer[1])
            print("Name        :", customer[2])
            print("Phone       :", customer[3])
            print("Balance     :", customer[4])

        else:

            print("❌ Account Not Found")

    elif choice == "3":

        account_no = input("Enter Account Number: ")
        amount = float(input("Enter Deposit Amount: "))

        query = """
        UPDATE customers
        SET balance = balance + %s
        WHERE account_no = %s
        """

        cursor.execute(query, (amount, account_no))
        conn.commit()

        print("✅ Amount Deposited Successfully")

    elif choice == "4":

        account_no = input("Enter Account Number: ")
        amount = float(input("Enter Withdraw Amount: "))

        query = "SELECT balance FROM customers WHERE account_no = %s"

        cursor.execute(query, (account_no,))
        result = cursor.fetchone()

        if result:

            balance = float(result[0])

            if balance >= amount:

                query = """
                UPDATE customers
                SET balance = balance - %s
                WHERE account_no = %s
                """

                cursor.execute(query, (amount, account_no))
                conn.commit()

                print("✅ Withdrawal Successful")
                print("Remaining Balance:", balance - amount)

            else:

                print("❌ Insufficient Balance")

        else:

            print("❌ Account Not Found")

    elif choice == "5":

        print("Thank You for using Bank Management System!")
        break

    else:

        print("❌ Invalid Choice")

conn.close()
