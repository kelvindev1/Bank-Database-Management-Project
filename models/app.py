from helpers import(
    exit_program,
    list_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    list_accounts,
    find_account_by_type,
    find_account_by_id,
    create_account,
    update_account,
    delete_account,
    list_customer_accounts,
    list_transactions,
    find_transaction_by_type,
    find_transaction_by_id,
    create_transaction,
    update_transaction,
    delete_transaction

)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_customers()
        elif choice == "2":
            find_customer_by_name()
        elif choice == "3":
            find_customer_by_id()
        elif choice == "4":
            create_customer()
        elif choice == "5":
            update_customer()
        elif choice == "6":
            delete_customer()
        elif choice == "7":
            list_accounts()
        elif choice == "8":
            find_account_by_type()
        elif choice == "9":
            find_account_by_id()
        elif choice == "10":
            create_account()
        elif choice == "11":
            update_account()
        elif choice == "12":
            delete_account()
        elif choice == "13":
            list_customer_accounts()
        elif choice == "14":
            list_transactions()
        elif choice == "15":
            find_transaction_by_type()
        elif choice == "16":
            find_transaction_by_id()
        elif choice == "17":
            create_transaction()
        elif choice == "18":
            update_transaction()
        elif choice == "19":
            delete_transaction()
        else:
            print("Invalid choice")



def menu():
    print("Select an option : ")
    print("0: Exit the program")
    print("1: List all Customers")
    print("2: Find Customer by name")
    print("3: Find Customer by id")
    print("4: Create Customer")
    print("5: Update Customer")
    print("6: Delete Customer")
    print("7: List all Accounts")
    print("8: Find Account by type")
    print("9: Find Account by id")
    print("10: Create Account")
    print("11: Update Account")
    print("12: Delete Account")
    print("13: List all Accounts for a Customer")
    print("14: List all Transactions")
    print("15: Find Transaction by Type")
    print("16: Find Transaction by id")
    print("17: Create Transaction")
    print("18: Update Transaction")
    print("19: Delete Transaction")

if __name__ == "__main__":
    main()