from helpers import(
    exit_program,
    list_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer
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






def menu():
    print("Select an option below: ")
    print("0. Exit the program")
    print("1. List all Customers")
    print("2. Find Customer by name")
    print("3. Find Customer by id")
    print("4: Create Customer")
    print("5: Update Customer")
    print("6: Delete Customer")



if __name__ == "__main__":
    main()