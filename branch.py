"""
branch.py
"""
class Branch:
    """
    Reprasent a bank branch.
    """
    next_id = "1"

    def __init__(self, branch_address: str, employees_list=None):
        self.branch_id = Branch.next_id
        Branch.next_id = int(Branch.next_id) + 1
        self.branch_address = branch_address

        if employees_list is None:
            employees_list = []
        else:
            self.employees_list = employees_list

    def add_employee(self, name: str) -> None:
        """
        Add an employee to the employees list.
        """
        self.employees_list.append(name)

    def get_employees_list(self) -> list:
        """
        Displaying the list of employees.
        """
        return self.employees_list

    def get_branch_info(self) -> str:
        """
        Displaying the information of branch.
        """
        return f"Branch's information\nBranch ID: {self.branch_id}\
            \nBranch adress: {self.branch_address}"