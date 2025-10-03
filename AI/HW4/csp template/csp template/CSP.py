from collections import deque
from typing import Callable, List, Tuple

class CSP(object):
    def __init__(self, *args, **kwargs) -> None:
        
        self.variables = {}
        self.constraints = []
        self.unassigned_var = []
        self.var_constraints = {}
        self.assignments = {}
        self.assignments_number = 0

    def add_constraint(self, constraint_func: Callable, variables: List) -> None:

        self.constraints.append((constraint_func ,variables ))

    def add_variable(self, variable: any, domain: List) -> None:

        self.variables[variable]= domain
        self.unassigned_var.append(variable )
        self.assignments[variable]= None


    def assign(self, variable: any, value: any) -> None:

        self.assignments[variable]= value
        self.unassigned_var.remove(variable )

    def is_consistent(self, variable: any, value: any) -> bool:

        for constraint_func ,variables in self.constraints:
            if variable in variables:

                assigned_values= {}
                for var in variables: 
                    if self.assignments[var] is not None: 
                        assigned_values[var]= self.assignments[var] 
                        assigned_values[variable]= value 

            if not constraint_func(assigned_values ):
                return False
        
            return True

    def is_complete(self) -> bool:

        return len(self.unassigned_var) == 0
    
    def is_assigned(self, variable: any) -> bool:

        return self.assignments[variable] is not None

    def un_assign(self, removed_values_from_domain: List[Tuple[any, any]], variable: any) -> None:

        self.assignments[variable]= None
        self.unassigned_var.append(variable )

