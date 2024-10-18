class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit" : 1, "sign" : 2, "dot" : 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit" : 1, "dot": 3},
            {"digit" : 4},
            {"digit": 4, "exponent" : 5},
            {"sign":6 , "digit" : 7},
            {"digit" :7},
            {"digit" : 7},
        ]

        current_state = 0
        for c in s: 
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]:
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False 
            
            if group not in dfa[current_state]:
                return False 
            
            current_state = dfa[current_state][group]
        return current_state in [1, 4, 7]


"""

Mention that you have defined different states in the DFA that represent how far along you are in processing the string. For example:

State 0: Initial state before reading any digits.
State 1: A valid number with digits (before a decimal or exponent).
State 2: A state where a sign (+/-) has been read.
State 3: A state where only a decimal has been read (without any digit before it).
State 4: A state where a valid number includes a decimal and digits.
State 5: A state where an exponent (e/E) is found, preparing for digits or a sign.
State 6: A state after reading an exponent followed by a sign (+/-).
State 7: A state where the number includes an exponent followed by digits.
"""
        