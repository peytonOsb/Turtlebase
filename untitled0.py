def Read_Specific_Line(file_name, line_number):
    with open(file_name, 'r') as file:
        line = ''
        for i in range(line_number):
            line = file.readline().strip()
        return line
    
def FindAdd(item, item_list): #finds a specified item in a list and returns its position unless it doesnt exist then it appends it to the list
    found = False
    for i in range(0, len(item_list)):
        if item == str(item_list[i]):
            found = True
            return i
        else:
            found = False
    if found == False:
        item_list.append(item)
        return len(item_list)

def Replace(item, newitem, List): #replaces a specified item in a list with a new specified item
    for i in range(len(List)):
        if item == str(List[i]):
            List[i] = newitem
            break
        else:
            print("not there")
            
def Format(List):
    temp_list = []
    T = 0
    
    #compiles a temporary list to sort through so we have a duplicate of values
    for item in List:
        temp_list.append(int(item))
    
    #must find the length of the temp list before manipulating it so it can finish its processes
    length = len(temp_list)
    
    #sorts through the temp list and outputs the minimum values one after another
    while T < length:
        smallest = temp_list[0]
        for item in range(len(temp_list)):
            if temp_list[item] < smallest:
                smallest = temp_list[item]
                
        List[T] = smallest
        temp_list.remove(smallest)
        T += 1
        
    
        
IDs = Read_Specific_Line("turtlebase.txt", 1).strip("IDs: ").split() 

for i in range(1, 1000):
    FindAdd(f"{i}", IDs)
    
Format(IDs)