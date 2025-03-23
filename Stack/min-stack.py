class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None

obj = MinStack()

while True:
    command = input("Enter the command (push X, pop, top, getMin, exit): ").split()

    if command[0] == "push":
        obj.push(int(command[1]))
    if command[0] == "pop":
        obj.pop()
    if command[0] == "top":
        print(obj.top())
    if command[0] == "getMin":
        print(obj.getMin())
    if command[0] == "exit":
        break
    else:
        print("This is not command!")