# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Centralized Business Rules Engine for banking policies."""

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        normalised = account_type.strip().upper()
        if normalised == "SAVINGS":
            return 1000.0
        return 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        normalised = account_type.strip().upper()
        if normalised == "SAVINGS":
            return 4.0
        if normalised == "FIXEDDEPOSIT":
            return 6.5
        return 0.0

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        normalised = account_type.strip().upper()
        if normalised == "CURRENT":
            return 10000.0
        return 0.0

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft = AccountRulesEngine.get_overdraft_limit(account_type)
        floor = min_bal - overdraft
        return (current_balance - amount) >= floor
