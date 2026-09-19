# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory
from gdb.domain.iaccount import IAccount

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # Step 1: Create one account of each type ONLY through AccountFactory.create_account()
    sa = AccountFactory.create_account("SAVINGS", "SA001", "Alice", 25, 10000.0, "Active", "1234")
    ca = AccountFactory.create_account("CURRENT", "CA001", "Bob", 35, 50000.0, "Active", "5678")
    sal = AccountFactory.create_account("SALARY", "SAL001", "Charlie", 28, 0.0, "Active", "9999")
    fd = AccountFactory.create_account("FIXEDDEPOSIT", "FD001", "Diana", 45, 100000.0, "Active", "0000")

    # Step 2: Using only IAccount members, assert balances and types, then exercise deposit/withdraw
    assert sa.balance == 10000.0, f"Expected 10000.0, got {sa.balance}"
    assert sa.get_account_type() == "Savings", f"Expected Savings, got {sa.get_account_type()}"
    assert ca.balance == 50000.0, f"Expected 50000.0, got {ca.balance}"
    assert ca.get_account_type() == "Current", f"Expected Current, got {ca.get_account_type()}"
    assert sal.balance == 0.0, f"Expected 0.0, got {sal.balance}"
    assert sal.get_account_type() == "Salary", f"Expected Salary, got {sal.get_account_type()}"
    assert fd.balance == 100000.0, f"Expected 100000.0, got {fd.balance}"
    assert fd.get_account_type() == "FixedDeposit", f"Expected FixedDeposit, got {fd.get_account_type()}"

    sa.deposit(500.0)
    sa.withdraw(200.0)
    ca.deposit(1000.0)
    fd.withdraw(5000.0)

    assert sa.balance == 10300.0, f"Expected 10300.0, got {sa.balance}"
    assert ca.balance == 51000.0, f"Expected 51000.0, got {ca.balance}"
    assert sal.balance == 0.0, f"Expected 0.0, got {sal.balance}"
    assert fd.balance == 95000.0, f"Expected 95000.0, got {fd.balance}"

    print("All assertions passed!")

if __name__ == "__main__":
    main()
