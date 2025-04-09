class Loan:
    def __init__(self, loan_id=None, customer=None, principal_amount=0.0, interest_rate=0.0, loan_term=0, loan_type="", loan_status="Pending"):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status