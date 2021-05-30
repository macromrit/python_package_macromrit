import csv
import pickle

#--------------------------------------------------------->
def write_txt(filename: str="norm", 
                fillers: str="Hello it me amrit.. How is it going")->str:
    """

    this function should be used to write txt files
    notice%% never add extensions like .txt to the file name as it's pre-built inside the function
    file type = txt
    step1: enter the file name
    step2: enter the string you wanna input in a single go
    step3: enjoy.. thats all. 
    
    """

    if '.txt' not in filename:
        with open(F'{filename}.txt', 'a') as creator:
            print(fillers, file=creator)
        print(F"""
______________________________________

file written or appended successfully
details:
    file_name: {filename}
    content: {fillers}

thanks for using amrits library
______________________________________

        """)    
        return "file written successfully"    
    else:
        print("hey no need to terminalize .txt extensions while naming your file.. this package autocompletes it")
        return None


def read_txt(filename: str="norm"):
    """
    
    this function should be used to read txt files
    notice%% never add extensions like .txt to the file name as it's pre-built inside the function
    file type = str
    just enter the filename and the rest would work like charm
    
    """
    
    with open(F'{filename}.txt', 'r') as reader:
        x = reader.read()
        print(x)
        return "read successfully"
    
#---------------------------------------------------------->

def write_csv(filename: str="norm", 
              total_columns: int=2, total_rows: int=2):
    
    """
    
    this function should be used to write csv files
    notice%% never add extensions like .csv to the file name as it's pre-built inside the function
    file type = csv[comma seperated values]
    step1: enter the filename
    step2: enter the no. of columns you wanna write.. if you wanna append rows to an already existing file then enter 0.. the rest would be handled by the program
    step3: enter the no. of rows you wanna write
    step4: enjoy.. that's all.    
    
    """
    if total_columns==0:
        x = int(input("enter total no. of columns you wanna write: "))
        
        with open(F'{filename}.csv', 'a', newline="") as writer:
            main = csv.writer(writer,
                            delimiter=",")

            count = 1
            
            while count<total_rows+1:
                main_list = []
                for i in range(1, x+1):
                    adding = str(input(F'enter value for column {i} row {count}: '))
                    main_list.append(adding)
                main.writerow(main_list)
                count+=1
        print(F"""
______________________________________

process successfull
total columns = {x}
total rows = {total_rows}

thanks for using amrits library
______________________________________

    """)

 
    else:
        with open(F'{filename}.csv', 'a', newline="") as writer:
            main = csv.writer(writer,
                            delimiter=",")
    
            column_list = []
            for i in range(1, total_columns+1):
                columns = str(input("enter value of column {0}: ".format(i))) 
                column_list.append(columns)

            main.writerow(column_list)

            count = 1
            
            while count<total_rows+1:
                main_list = []
                for i in range(1, total_columns+1):
                    adding = str(input(F'enter value for column {i} row {count}: '))
                    main_list.append(adding)
                main.writerow(main_list)
                count+=1
        print(F"""
______________________________________

process successfull
total columns = {total_columns}
total rows = {total_rows}

thanks for using amrits library
______________________________________

    """)
    return "process successfull"
        

def read_csv(filename: str):
    """
    
    this function should be used to read csv files
    notice%% never add extensions like .csv to the file name as it's pre-built inside the function
    file type = csv[comma seperated values]
    just enter the filename to read it... the rest works like charm
    
    """    

    with open(F'{filename}.csv', 'r') as reader:
        reading = csv.reader(reader)
        for i in reading:
            print(i)
    
#---------------------------------------------------------->

def write_bin(filename: str="amrit", *vals):
    """
    
    this function should be used to write binary files via pickling
    notice%% never add extensions like .bin or .pkl to the file name as it's pre-built inside the function
    file type = binary or bin
    step1: enter the filename
    step2: enter the values you wanna input one after another in the function
    step3: enjoy... that's all
    
    """
    
    if vals==():
        print("Ooops.. no elements inputed.")
    else:
        real_vals = vals
        with open(F'{filename}.pkl', 'ab') as appendizer:
            count = 0
            for i in real_vals:
                pickle.dump(i, appendizer, protocol=0)
                count+=1
        print(
F'''
{count} elements have been appended to the file you desired.. 
Thanks for using amrits library

'''
    )
    

def read_bin(filename: str):
    """
    
    this function should be used to read a pickled binary file
    notice%% never add extensions like .bin or .pkl to the file name as it's pre-built inside the function
    file type = bin or binary
    just enter the filenamname to read what's inside it.. the rest would work like charm
    
    """
    
    with open(F'{filename}.pkl', 'rb') as reader:
        reading = pickle.load(reader)
        while reading:
            print(reading)
            try:
                reading = pickle.load(reader)
            except:
                break
#---------------------------------------------------------->


write_csv('amrit', 0, 2)