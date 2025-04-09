from abc import ABC, abstractmethod
from LoanManagement.entity.loan import Loan

class ILoanRepository(ABC):

    @abstractmethod
    def apply_loan(self, loan: Loan):
        pass

    @abstractmethod
    def calculate_interest(self, *args):
        pass

    @abstractmethod
    def loan_status(self, loan_id):
        pass

    @abstractmethod
    def calculate_emi(self, *args):
        pass

    @abstractmethod
    def loan_re_payment(self, loan_id, amount):
        pass

    @abstractmethod
    def get_all_loan(self):
        pass

    @abstractmethod
    def get_loan_by_id(self, loan_id):
        pass
