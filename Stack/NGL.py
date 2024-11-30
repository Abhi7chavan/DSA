#Nearest Largest Left Element

from implement_stack import Stack


def NGL(array,stack,vector):
    for i in array:
        if stack.Size() == 0:
            vector.append(-1)
        
        elif stack.Size() > 0 and stack.Top() >i:
            vector.append(stack.Top())
        
        elif stack.Size() > 0 and stack.Top() < i:
            while stack.Size() > 0 and stack.Top() < i:
                stack.Pop()
                
            if stack.Size() == 0:
                vector.append(-1)
                
            else:
                vector.append(stack.Top())
               

        stack.Push(i)

    return vector


if __name__ =="__main__":
    array = [1,3,2,4]
    stack = Stack()
    vector = []
    
    result = NGL(array,stack,vector)
    print(result)

