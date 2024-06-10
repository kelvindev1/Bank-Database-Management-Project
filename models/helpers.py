from account import Account
from customer import Customer
from transaction import Transaction

def exit_program():
    print("Bye!")
    exit()

def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_customer_by_name():
    first_name = input("Enter the customer's First Name: ")
    last_name = input("Enter the customer's last Name: ")
    customer = Customer.find_by_name(first_name, last_name)
    print(customer) if customer else print(f'Customer {first_name, last_name} not in Database')


def find_customer_by_id():
    id_ = input("Enter the customer's ID: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f"Customer {id_} not in Database")


def create_customer():
    first_name = input("Enter the customer's First Name: ")
    last_name = input("Enter the customer's Last Name: ")
    phone_number = input("Enter the customer's Phone Number: ")
    email = input("Enter the customer's email: ")
    try:
        customer = Customer.create(first_name, last_name, phone_number, email)
        print(f"You have Successfully created {customer}")
    except Exception as exc:
        print("There was an error creating customer: ", exc)

def update_customer():
    id_ = input("Enter the customer's ID: ")
    if customer := Customer.find_by_id(id_):
        try:
            first_name = input("Enter customer's First Name: ")
            customer.first_name = first_name
            last_name = input("Enter customer's Last Name: ")
            customer.last_name = last_name
            phone_number = input("Enter customer's Phone Number: ")
            customer.phone_number = phone_number
            email = input("Enter customer's email: ")
            customer.email = email

            customer.update()
            print(f"Success: You have update {customer}")

        except Exception as exc:
            print("There was a Error Updating customer: ", exc)
    else:
        print(f"Customer {id_} not in Database")


def delete_customer():
    id_ = input("Enter the customer's ID: ")
    if customer := Customer.find_by_id(id_):
        customer.delete()
        print(f"Customer {id_} was deleted")
    else:
        print(f"Customer {id_} not in Database")
        


