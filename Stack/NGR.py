#Nearest Greater to right.
from implement_stack import Stack


def NGR(st,array,vector):
    for i in reversed(array):
        if st.Size()==0:
            vector.append(-1)
            
        elif st.Size() > 0 and st.Top() > i:
            vector.append(st.Top())
        elif st.Size() > 0 and st.Top() < i:
            while st.Size() > 0 and st.Top() < i:
                st.Pop()
                
            if st.Size() == 0:
                vector.append(-1)
                
            else:
                vector.append(st.Top())
    
        st.Push(i)
        
    return vector[::-1]
    
if __name__ =="__main__":
    vector = []
    array = [1,3,2,4]
    stack = Stack()
    result = NGR(stack,array,vector)
    print(result)
   
