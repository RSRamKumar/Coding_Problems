"""
Reverse a string using stack
"""

class Stack:
    def __init__(self):
        self.list = []

    def push(self,element):
        self.list.append(element)

    def peek(self):
        return str(self.list[-1])

    def pop(self):
        try:
            return self.list.pop()
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.list)

    def __repr__(self):
         return f"{self.list}"




def reversing_string_using_stack(string):
    reverse_string = ""
    S = Stack()
    for i in range(len(string)):
        S.push(string[i])
    for _ in range(len(string)):
        reverse_string += S.peek()
        S.pop()
    return reverse_string


if __name__ == "__main__":
     print(reversing_string_using_stack("RamKumarRuppaSurulinathan"))
     print(reversing_string_using_stack("AbrahamCornelius"))

