stack = [10, 20, 30,40,50,60,70,80,90,100]
print("Original stack: ", stack)
if len(stack) == 0:
    print("Stack underflow")

else:
    removed = stack.pop()
    print("Popped value: ", removed)
print("Stack value after pop: ", stack)