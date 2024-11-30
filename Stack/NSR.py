# Nearest Smallest Right Element

from implement_stack import Stack


def NSR(array,stack,vector):
    for i in reversed(array):
        if stack.Size() == 0:
            vector.append(-1)
            
        elif stack.Size() > 0 and stack.Top() < i:
            vector.append(stack.Top())
            
        elif stack.Size() > 0 and stack.Top() > i:
            while stack.Size() > 0 and stack.Top() > i:
                stack.Pop()
                
            if stack.Size() == 0:
                vector.append(-1)
                
            else:
                vector.append(stack.Top())
                
        stack.Push(i)
        
    return vector[::-1]

if __name__ == "__main__":
    stack = Stack()
    vector = []
    array = [4,5,2,10,8]
    
    result = NSR(array,stack,vector)
    print(result)