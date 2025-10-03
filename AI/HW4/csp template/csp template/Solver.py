from collections import deque
from typing import Callable, List, Tuple, Any
from CSP import CSP



class Solver(object):

    def __init__(self, csp: CSP, domain_heuristics: bool = False, variable_heuristics: bool = False, MAC: bool = False) -> None:
     
        self.domain_heuristic = domain_heuristics
        self.variable_heuristic = variable_heuristics
        self.MAC = MAC
        self.csp = csp

        self.board_size = int(len(self.csp.variables) ** 0.5)


    def backtrack_solver(self) -> None | dict:
        
        if self.csp.is_complete():
            return self.csp.assignments

        variable= self.select_unassigned_variable()

        domain= self.ordered_domain_value(variable)

        for value in domain:
            if self.csp.is_consistent(variable ,value ):
                self.csp.assign(variable ,value )
                removed_values = []

                result= self.backtrack_solver()

                if result:
                    return result

                self.csp.un_assign(removed_values ,variable )
        return None

    def select_unassigned_variable(self) -> any:

            return self.csp.unassigned_var[0] 

    def ordered_domain_value(self, variable: str) -> Any:

            return self.csp.variables[variable]

'''''
    def apply_MAC(self) -> List[Any]:


    def multi_arc_reduce(self, constraint_func: callable, variables: List[Any]) -> List[Tuple[Any, Any]]:


    def binary_arc_reduce(self, x: Any, y: Any, constraint_func: callable) -> list[Any] | None:


    def MRV(self, variables) -> Any:


    def LCV(self, variable: Any) -> List[any]:

'''''