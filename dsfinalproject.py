import os
import math
#menu functions
def menu():
    print('Written by Kianoosh Soleymani,Student number:40111360023')
    print('''::::::::Data structure tool box::::::::
1. Search in Array(Binary search)
2. Sort array
3. Infix to postfix or Prefix
4. Heapify
5. Adj matrix to Graph And BFS
0.Exit''')
#choice function
def enter_choice():
    choice=int(input('Enter the choice: '))
    return choice
#binary search function declartion 
def binary_s(arr):
    while(True):
        try:
            target = int(input('Enter the element that you want to be found: '))
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low+high)//2
                if arr[mid] == target:
                    return mid   
                elif arr[mid] < target:
                        low = mid + 1
                else:
                        high = mid - 1
            return -1    
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer:") 
            continue
        break
        
#insertion sort 
def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and current < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
        print(f'step{i}:',nums)
    return nums
#selection sort 
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j    
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        print(f'step{i+1}:',numbers)
    return numbers
#Infix to postfix
def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix_expression = ''
    stack = []
    for char in infix_expression:
        if char.isalnum() or char.isalpha():
            postfix_expression += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix_expression += stack.pop()
            stack.append(char)
    while stack:
        postfix_expression += stack.pop()
    return postfix_expression
def infix_to_prefix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    prefix_expression = ''
    stack = []
    for char in reversed(infix):
        if char.isalnum() or char.isalpha():
            prefix_expression = char + prefix_expression
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix_expression = stack.pop() + prefix_expression
            stack.pop()
        else:
            while stack and stack[-1] != ')' and precedence[char] <= precedence[stack[-1]]:
                prefix_expression = stack.pop() + prefix_expression
            stack.append(char)
    while stack:
        prefix_expression = stack.pop() + prefix_expression
    return prefix_expression

 
#heapify
def maxheapify(arr):
    i=0
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxheapify(arr)
    return arr
def minheapify(arr):
    i=0
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minheapify(arr)
    return arr
#BFS Function
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
#the function that must be done
while True:
    try:
        menu()
        choice=enter_choice()
        os.system('cls')
    except ValueError:
        input("Invalid input. Press ENTER to enter valid integer:")
        os.system('cls')
        continue
    while choice > 5 or choice < 0:
        os.system('cls')
        input('Your number is out of range 0 to 5,Press enter to try again!')
        os.system('cls')
        menu()
        choice=enter_choice()
#exit 
    if choice==0:
        print('Thanks for using our program')
        exit(0)
#binary search 
    while choice == 1:
        try:
            os.system('cls')
            arr=[int(i) for i in list(input('Enter the elements of array: ').split(','))]
            arr.sort()
            result=binary_s(arr)
            if result != -1:
                print(f'The sorted list is {arr}')
                print(f'The target that you want is in {result + 1 }')
            elif result == -1:
                print(f'The sorted list is {arr}')
                print('Not found')
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer:")
            continue
        try:
            choice_1 = int(input('[0]exit,[1]menu,[2]another array: '))
            if choice_1==0:
                print('Thanks for using our program')
                exit(0)
            elif choice_1==1:
                os.system('cls')
                menu()
                choice=enter_choice()
            elif choice_1==2:
                continue
            while choice_1 < 0 or choice_1 > 2:
                print('Your number is out of range 0 to 2.Please try again.')
                choice_1 = int(input('[0]exit,[1]menu,[2]another array: '))
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer:")
            choice_1 = int(input('[0]exit,[1]menu,[2]another array: '))
#sorting
    while choice == 2:
        try:
            os.system('cls')
            select=int(input('1.insertion sort,2.selection sort:'))
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer")
            continue
        try:
           while select==1:
                try:
                    os.system('cls')
                    print("INSERTION SORT")
                    numbers=[int(i) for i in input('Enter the elements of array:').split(',')]
                    result=insertion_sort(numbers)
                    print(f'sorted list is{result}')
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
                try:
                    sel = int(input('[0]exit,[1]menu,[2]another array: '))
                    if sel==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif sel==1:
                        os.system('cls')
                        break
                    elif sel==2:
                        os.system('cls')
                        continue
                except ValueError:
                   input("Invalid input. Press ENTER to enter valid integer")
                   sel = int(input('[0]exit,[1]menu,[2]another array: '))
                break
           while select==2:
                try:
                    os.system('cls')
                    print("SELECTION SORT")
                    numbers=[int(i) for i in input('Enter the elements of array:').split(',')]
                    result=selection_sort(numbers)
                    print(f'sorted list is{result}')
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
                try:
                    sel = int(input('[0]exit,[1]menu,[2]another array: '))
                    if sel==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif sel==1:
                        os.system('cls')
                        break
                    elif sel==2:
                        os.system('cls')
                        continue
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    sel = int(input('[0]exit,[1]menu,[2]another array: '))
                break   
        except ValueError:
           print("Invalid input. Press ENTER to enter valid integer")
           continue
        break
      
#infix to postfix or prefix 
    while choice==3:
        try:
            os.system('cls')
            user_selection=int(input('1.postfix,2.prefix:'))
            if user_selection == 1:
                try:
                    os.system('cls')
                    print('Infix to postfix')
                    user_expression=input('Enter your expression: ')
                    converted_expression=infix_to_postfix(user_expression)
                    print(converted_expression)
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer:")
                    os.system('cls')
                    print('Infix to postfix')
                    user_expression=input('Enter your expression: ')
                    converted_expression=infix_to_postfix(user_expression)
                    print(converted_expression)
                try:
                    choice_4=int(input('[0]exit,[1]menu,[2]another expression: '))
                    if choice_4==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif choice_4==1:
                        os.system('cls')
                        break
                    elif choice_4==2:
                        os.system('cls')
                        continue
                    elif choice_4<0 or choice_4>2:
                        print('try again')
                        choice_4=int(input('[0]exit,[1]menu,[2]another expression: '))
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer:")  
                    choice_4=int(input('[0]exit,[1]menu,[2]another expression: '))
            if user_selection==2:           
                try:
                    os.system('cls')
                    print('Infix to prefix')
                    user_expression=input('Enter your expression: ')
                    converted_expression=infix_to_prefix(user_expression)
                    print(converted_expression)
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer:")  
                    os.system('cls')
                    print('Infix to prefix')
                    user_expression=input('Enter your expression: ')
                    converted_expression=infix_to_prefix(user_expression)
                    print(converted_expression)
                try:
                    choice_4=int(input('[0]exit,[1]menu,[2]another expression: '))
                    if choice_4==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif choice_4==1:
                        os.system('cls')
                        break 
                    elif choice_4==2:
                        os.system('cls')
                        continue
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer:")  
                    choice_4=int(input('[0]exit,[1]menu,[2]another expression: '))
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer:")
            continue
#Heapify                
    while choice==4:
        try:
            os.system('cls')
            sel=int(input('1.maxheapify,2.minheaplfy: '))
        except:
            input("Invalid input. Press ENTER to enter valid integer:")
            continue 
        try:
           while sel==1:
                try:
                    os.system('cls')
                    print("MAX HEAPIFY")
                    numbers=[int(i) for i in input('Enter the elements of array:').split(',')]
                    result=maxheapify(numbers)
                    print(f'Max heap is{result}')
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
                try:
                    sele = int(input('[0]exit,[1]menu,[2]another array: '))
                    if sele==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif sele==1:
                        os.system('cls')
                        break
                    elif sele==2:
                        os.system('cls')
                        continue
                except ValueError:
                   input("Invalid input. Press ENTER to enter valid integer")
                   sele = int(input('[0]exit,[1]menu,[2]another array: '))
                break
           while sel==2:
                try:
                    os.system('cls')
                    print("MIN HEAPIFY")
                    numbers=[int(i) for i in input('Enter the elements of array:').split(',')]
                    result=minheapify(numbers)
                    print(f'Min heap is{result}')
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
                try:
                    sele = int(input('[0]exit,[1]menu,[2]another array: '))
                    if sele==0:
                        print('Thanks for using our program')
                        exit(0)
                    elif sele==1:
                        os.system('cls')
                        break
                    elif sele==2:
                        os.system('cls')
                        continue
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    sele = int(input('[0]exit,[1]menu,[2]another array: '))
                break   
        except ValueError:
           input("Invalid input. Press ENTER to enter valid integer")
           continue
        break
#BFS
    while choice==5:
        try:
            os.system('cls')
            n=int(input('Enter the number of vertexes:')) 
            while n<0:
                print('Vertex number can not be negative.try again')  
                n=int(input('Enter the number of vertexes:')) 
            adj_matrix = []
            for i in range(n):
                try:
                    row = [int(x) for x in input(f"Enter row {i+1},you enter 0 or 1 and seperate them by ',': ").split(',') ]
                    adj_matrix.append(row)
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
            try:
                while True:
                    start = int(input('Enter start vertex: '))
                    break
            except ValueError:
               input("Invalid input. Press ENTER to enter valid integer")
               continue 
            print(bfs(adj_matrix,start))
            while True:
                try:
                    select=int(input('[0]exit,[1]menu,[2]another array: '))
                    if select == 0:
                        print('Thanks for using our program')
                        exit(0)
                    elif select==1:
                        os.system('cls')
                        break
                    elif select==2:
                        continue
                except ValueError:
                    input("Invalid input. Press ENTER to enter valid integer")
                    continue
                break
            break  
        except ValueError:
            input("Invalid input. Press ENTER to enter valid integer")
            continue

        


        
        



        

        


        

    
    







    
    
