"""
branch.py
"""
class Branch:
    """
    Reprasent a bank branch.
    """
    def __init__(self, branch_id: str, branch_address: str,\
                  customers_list: list, employees_list=None):
        self.branch_id = branch_id
        self.branch_address = branch_address

        if customers_list is None:
            self.customers_list = []
        else:
            self.customers_list = customers_list

        if employees_list is None:
            self.employees_list = []
        else:
            self.employees_list = employees_list

    def assign_employee(self, employee_name : str) -> None:
        """
        Assign an employee to the branch.
        """
        self.employees_list.append(employee_name)