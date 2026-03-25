from descriptors.positive_value import PositiveValue
from descriptors.name import Name
from descriptors.log_descriptor import LogDescriptor


class BankAccount:
    owner = Name()
    balance = PositiveValue()
    log_balance = LogDescriptor("balance")

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.log_balance = balance