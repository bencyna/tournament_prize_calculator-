class Stack:
    def __init__(self):
        self.stack= []
        
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            raise Exception("Stack empty")

        return self.stack.pop()

    def add(self):
        if len(self.stack) < 2:
            raise Exception("Stack empty")

        stack_top = self.stack.pop()
        stack_second = self.stack.pop()
        
        if type(stack_top) != int or type(stack_second) != int:
            stack_top == str(stack_top)
            stack_second == str(stack_second)
        
        self.stack.append(stack_top + stack_second)
        
    def get(self):
        if not self.stack:
            return self.stack[-1]
    
def exceute(program: List[List[]]):
    i = 0
    stack = Stack()
    while i < len(program):
        function = program[0]
        
        if function[0] == "Push":
            stack.push()
        elif function[0] == "Pop":
            stack.pop()
        elif function[0] == "print":
            stack.Print() 
        elif function[0] == "Add":
            stack.add()
        elif function[0] == "Jump":
            i == function[1] 
            continue
        elif function[0] == "Jnz":
            if stack.get() != 0:
                i == function[1]
                continue
    
        i+=1


def transform(program):
    if not program: return
    # create prefix sum 
    prefix = [0]
    if program[0][0] == "jump":
        prefix[0] = 3
    for i in range(1, len(program)):
        function, num = program[i]
        prefix.append(prefix[i-1])
        if function == "Jump":
            prefix[i] += 3
    
    # add functions to program list
    new_program = []
    
    for i, function_call in enumerate(program):
        function, value = function_call
        if function == "Jump":
            new_program.append(["Push", f"Jumping to {value}"])
            new_program.append(["Print", None])
            new_program.append(["Pop", None])
            value = prefix[i] + value
        new_program.append([function, value]) 
                
                
    
        
        
        
        
        