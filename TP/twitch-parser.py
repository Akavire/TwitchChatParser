'''
Simple program to parse the txt document outputed by
jdpurcell's RechatTool and gather information on keywords
https://github.com/jdpurcell/RechatTool
'''

import pathlib

def main():
    filepath = user_input()
    file_counts = read_file(filepath)
    metrics(file_counts)
    
def user_input() -> str:
    ''' 
    gather input on VOD number
    (assumes txt is in current folder)
    '''
    vod_number = input("Enter vod number: ")
    current_path = pathlib.Path().absolute()
    current_path = str(current_path) + "\\" + str(vod_number) + ".txt"
    return current_path

def read_file(filepath) -> dict:
    '''
    open and read the file, store
    lowered words in a dict
    '''
    file_counts = dict()
    with open(filepath, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.split()
            del line[0:2]
            for word in line:
                word = word.lower()
                if word in file_counts:
                    file_counts[word] += 1
                else:
                    file_counts[word] = 1
    return file_counts

def metrics(file_counts) -> None:
    '''
    transform and print counts
    '''
    res = {key: val for key, val in sorted(file_counts.items(), key = lambda ele: ele[1], reverse = True)} 
    keys = list(file_counts.keys()) 
    keys.sort()
    sorted_dict = {i: file_counts[i] for i in keys}
    print("---------------------")
    print("By Values Descending")
    print("---------------------")
    print(res) # by values descending
    print("---------------------")
    print("By Alpabetical Order")
    print("---------------------")
    print(sorted_dict) # alphabetically
    
                
            
            
       
        
            
            

    
if __name__ == "__main__":
    main()