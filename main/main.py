from LoanManagement.entity.customer import Customer
from LoanManagement.entity.loan import Loan
from LoanManagement.dao.ILoanRepositoryImpl import LoanRepositoryImpl
from LoanManagement.util.db_conn_util import DBConnUtil
from LoanManagement.exceptions.invalid_loan_exception import InvalidLoanException

def main():
    repo = LoanRepositoryImpl()
    db = DBConnUtil()

    while True:
        print("\n1. Apply for Loan")
        print("2. Get All Loans")
        print("3. Get Loan by ID")
        print("4. Loan Repayment")
        print("5. Calculate Interest")
        print("6. Calculate EMI")
        print("7. Loan Status")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            # Check if customer exists
            existing_customer = db.fetch_query("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
            if not existing_customer:
                print("Customer not found. Please enter customer details.")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                address = input("Enter Address: ")
                credit_score = int(input("Enter Credit Score: "))
                customer = Customer(customer_id, name, email, phone, address, credit_score)
                query = """
                    INSERT INTO customer (customer_id, name, email, phone, address, credit_score)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                db.execute_query(query, (customer.customer_id, customer.name, customer.email, customer.phone, customer.address, customer.credit_score))
            else:
                customer = Customer(*existing_customer[0])

            # Now proceed with loan application
            loan_id = int(input("Enter Loan ID: "))
            principal = float(input("Enter Principal Amount: "))
            rate = float(input("Enter Interest Rate: "))
            term = int(input("Enter Loan Tenure (months): "))
            loan_type = input("Enter Loan Type (HomeLoan/CarLoan): ")
            loan = Loan(loan_id, customer, principal, rate, term, loan_type, 'Pending')

            repo.apply_loan(loan)

        elif choice == '2':
            repo.get_all_loan()

        elif choice == '3':
            loan_id = int(input("Enter Loan ID: "))
            try:
                repo.get_loan_by_id(loan_id)
            except InvalidLoanException as e:
                print(e)

        elif choice == '4':
            loan_id = int(input("Enter Loan ID: "))
            amount = float(input("Enter Repayment Amount: "))
            repo.loan_re_payment(loan_id, amount)

        elif choice == '5':
            loan_id = int(input("Enter Loan ID: "))
            try:
                repo.calculate_interest(loan_id)
            except InvalidLoanException as e:
                print(e)

        elif choice == '6':
            loan_id = int(input("Enter Loan ID: "))
            repo.calculate_emi(loan_id)

        elif choice == '7':
            loan_id = int(input("Enter Loan ID: "))
            try:
                repo.loan_status(loan_id)
            except InvalidLoanException as e:
                print(e)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
