# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False



def check_brackets_in_code(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            bracket = Bracket(opening_brackets_stack[-1][1], i)
            if bracket.Match(next):
                opening_brackets_stack.pop()
            else:
                print(i+1)
                sys.exit()
    if not opening_brackets_stack == []:
        print(opening_brackets_stack.pop(0)[0]+1)
    else:
        print('Success')

if __name__ == "__main__":
    # text = sys.stdin.read()
    text = open(r'C:\Users\c6158\OneDrive - business\Coursera Learn\data structure\week1\example\check_brackets_in_code\tests\29','r')
    text = text.read()
    
    check_brackets_in_code(text)

    # Printing answer, write your code here
