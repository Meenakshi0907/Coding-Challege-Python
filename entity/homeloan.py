from LoanManagement.entity.loan import Loan
class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=0.0, interest_rate=0.0, loan_term=0, loan_status="Pending", property_address="", property_value=0):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, loan_type="HomeLoan", loan_status=loan_status)
        self.property_address = property_address
        self.property_value = property_value