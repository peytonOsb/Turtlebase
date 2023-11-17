def Read_Specific_Line(file_name, line_number):
    with open(file_name, 'r') as file:
        line = ''
        for i in range(line_number):
            line = file.readline().strip()
        return line
    
def FindAdd(item, item_list):
    for i in range(len(item_list)):
        try:
            if item == int(item_list[i]):
                return i  # Item found, return its index
        except(ValueError):
                continue

    # If the item is not found, append it to the list
    item_list.append(item)
    return len(item_list) - 1

def Replace(item, newitem, List): #replaces a specified item in a list with a new specified item
    for i in range(len(List)):
        if item == str(List[i]):
            List[i] = newitem
            break
        else:
            print("not there")
        
def merge_sort(List):

    

    if len(List) > 1:
        #finds the midpoint of a list
        mid = round(len(List) / 2)  # Find the middle of the array
        
        #splits the list into two halfs a left and right around the midpoint
        left = List[ :mid]
        right = List[mid:]
        
        #basically splits each halfs into more halfs if need be
        merge_sort(left)
        merge_sort(right)
        
        #initializes a "position holders" for the different halves of the split list
        i = j = k = 0
        
        #iterates through the left and right lists and compares the respective values
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                List[k] = left[i]
                i += 1
            else:
                List[k] = right[j]
                j += 1
            k += 1
            
        #since the main loop finishes when one hlaf has reached its end it could leave some unsorted numbers
        #so we need cleaner code
        
        #sees if anything is left in the left half and if so adds it to the list
        while i < len(left):
            List[k] = left[i]
            i += 1
            k += 1
            
        #sees if anything is left in the right half and if so adds it to the list
        while j < len(right):
            List[k] = right[j]
            j += 1
            k += 1
            
def formater(file_name, pos, ID, State, Heading):
    str_formated = ""
    IDs_formated = "IDs:      "
    prefixes = ['x: ','y: ','z: ']
    
    for i in range(len(pos)):
        str_formated = str_formated + '|' + " " + prefixes[i] + str(pos[i]) + " "
        
    str_formated = f'Turtle{ID} {str_formated} | facing: {Heading} | state: {State} |'
    
    with open(file_name, 'r') as file:
        IDs = Read_Specific_Line(file_name, 1).strip("IDs: ").split("|")
        
    IDs.remove('')    
    IDs.remove('')       
    
    for i in range(len(IDs)):
        IDs[i] = int(IDs[i])
    
    file_pos = FindAdd(ID, IDs)
    merge_sort(IDs)
    
    for i in range(len(IDs)):
        IDs_formated = IDs_formated + "| " + str(IDs[i]) + " "
    IDs_formated = IDs_formated + "|"
    
    return IDs_formated, str_formated, IDs
       
p = [36515, 9495, 2994]
f = "turtlebase.txt"
i = 1
s = "running"
h = 4

IDs_formated, entry, IDs = formater(f, p, i, s, h)

position_in = (FindAdd(i, IDs) * 2) + 2

with open(f, 'r') as file:
    contents = file.read().split('\n')

contents[position_in] = entry


print(contents)

with open(f, 'w') as file:
    for item in contents:
        file.write(item + '\n')
    
    





   
    
