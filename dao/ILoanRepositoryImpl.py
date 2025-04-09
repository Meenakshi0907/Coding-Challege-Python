from LoanManagement.dao.ILoanRepository import ILoanRepository
from LoanManagement.util.db_conn_util import DBConnUtil
from LoanManagement.exceptions.invalid_loan_exception import InvalidLoanException
import math

class LoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.db = DBConnUtil()

    def apply_loan(self, loan):
        confirm = input("Do you want to apply for loan (Yes/No)? ").lower()
        if confirm != 'yes':
            print("Loan application cancelled.")
            return
        query = """
            INSERT INTO loan (loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (loan.loan_id, loan.customer.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term, loan.loan_type, 'Pending')
        self.db.execute_query(query, values)

    def calculate_interest(self, *args):
        if len(args) == 1:
            loan_id = args[0]
            result = self.db.fetch_query(
                "SELECT principal_amount, interest_rate, loan_term FROM loan WHERE loan_id = %s", (loan_id,))
            if not result:
                raise InvalidLoanException("Loan ID not found.")
        principal = float(result[0][0])
        rate = float(result[0][1])
        term = int(result[0][2])
        interest = (principal * rate * term) / 12
        print(f"Interest Amount: {interest}")
        return interest

    def loan_status(self, loan_id):
        result = self.db.fetch_query("SELECT c.credit_score FROM loan l JOIN customer c ON l.customer_id = c.customer_id WHERE l.loan_id = %s", (loan_id,))
        if not result:
            raise InvalidLoanException("Loan ID not found.")
        credit_score = result[0][0]
        status = 'Approved' if credit_score > 650 else 'Rejected'
        self.db.execute_query("UPDATE loan SET loan_status = %s WHERE loan_id = %s", (status, loan_id))
        print(f"Loan {loan_id} is {status}.")

    def calculate_emi(self, *args):
        if len(args) == 1:
            loan_id = args[0]
            result = self.db.fetch_query(
                "SELECT principal_amount, interest_rate, loan_term FROM loan WHERE loan_id = %s", (loan_id,))
            if not result:
                raise InvalidLoanException("Loan ID not found.")
            principal = float(result[0][0])
            rate = float(result[0][1])
            term = int(result[0][2])
            R = rate / 12 / 100
            EMI = (principal * R * pow(1 + R, term)) / (pow(1 + R, term) - 1)
            print(f"EMI: {round(EMI, 2)}")
        return EMI

    def loan_re_payment(self, loan_id, amount):
        emi = self.calculate_emi(loan_id)
        if amount < emi:
            print("Amount is less than EMI. Cannot process payment.")
            return
        num_emi_paid = math.floor(amount / emi)
        print(f"{num_emi_paid} EMI(s) paid for Loan ID {loan_id}.")
        # Extend: update DB for tracking paid EMIs

    def get_all_loan(self):
        results = self.db.fetch_query("SELECT * FROM loan")
        for row in results:
            print(row)

    def get_loan_by_id(self, loan_id):
        result = self.db.fetch_query("SELECT * FROM loan WHERE loan_id = %s", (loan_id,))
        if not result:
            raise InvalidLoanException("Loan ID not found.")
        print(result[0])