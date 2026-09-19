# gdb/tests/test_abstract_account.py
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import MinimumBalanceViolationException

def main():
    print("=== Activity 10: Banking Operations Suite ===")
    sa = SavingsAccount("SA001", "Alice", 25, 10000.0, "Active", "1234", 4.0, 1000.0)
    ca = CurrentAccount("CA001", "Bob", 35, 50000.0, "Active", "5678", 25000.0)
    fd = FixedDepositAccount("FD001", "Charlie", 40, 100000.0, "Active", "9999", 12, 6.5)

    interests = {sa: 400.0, ca: 0.0, fd: 6500.0}
    for account in [sa, ca, fd]:
        assert account.calculate_interest() == interests[account]

    try:
        sa.withdraw(9001)
        assert False, "Expected MinimumBalanceViolationException"
    except MinimumBalanceViolationException:
        pass

if __name__ == "__main__":
    main()
