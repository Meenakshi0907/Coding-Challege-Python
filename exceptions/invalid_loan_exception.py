class InvalidLoanException(Exception):
    def __init__(self, message="Invalid Loan ID or Loan not found."):
        super().__init__(message)
