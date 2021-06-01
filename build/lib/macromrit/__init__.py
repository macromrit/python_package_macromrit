import csv
import pickle

#--------------------------------------------------------->
def write_txt(filename: str, 
                fillers: str="Hello it me amrit.. How is it going")->str:
    """
    this function should be used to write txt files
    notice%% add extension as  .txt to the file name as it's mandatory 
    file type = txt
    step1: enter the file name
    step2: enter the string you wanna input in a single go
    step3: enjoy.. thats all. 
    
    """
    with open(filename, 'a') as creator:
        print(fillers, file=creator)
    print(F"""
______________________________________
file written or appended successfully
details:
    file_name: {filename}
    content: {fillers}
thanks for using amrit's library
______________________________________
        """)    
    return "file written successfully"    



def read_txt(filename: str, mode: str="p"):
    """
    
    this function should be used to read txt files
    notice%% add extension as  .txt to the file name as it's mandatory 
    file type = str
    just enter the filename
    then enter the medium of range you wanna use the output i.e enter 'p' for printing the text or 'r' to make the text return
    then rest would work like charm
    
    """

    if mode=='p':
        with open(filename, 'r') as reader:
            x = reader.read()
            print(x)
            
    elif mode=='r':
        with open(filename, 'r') as reader:
            x = reader.read()
        return x
    
#---------------------------------------------------------->

def write_csv(filename: str, 
              total_columns: int=2, total_rows: int=2):
    
    """
    
    this function should be used to write csv files
    notice%% never add extensions like .csv to the file name as it's pre-built inside the function
    file type = csv[comma seperated values]
    step1: enter the filename
    step2: enter the no. of columns you wanna write.. if you wanna append rows to an existing file then enter 0.. the rest would be handled by the program
    step3: enter the no. of rows you wanna write
    step4: enjoy.. that's all.    
    
    """
    if total_columns==0:
        x = int(input("enter total no. of columns you wanna write in the given file: "))
            
        with open(filename, 'a', newline="") as writer:
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
    thanks for using amrit's library
    ______________________________________
        """)

    
    else:
        with open(filename, 'a', newline="") as writer:
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
                    adding = str(input(F'enter value for column {column_list[i-1]} in row {count}: '))
                    main_list.append(adding)
                main.writerow(main_list)
                count+=1
        print(F"""
    ______________________________________
    process successful
    total columns = {total_columns}
    total rows = {total_rows}
    thanks for using amrit's library
    ______________________________________
        """)
        return "process successful"
            

def read_csv(filename: str, mode: str='p'):
    """
    
    this function should be used to read csv files
    notice%% add extension as  .csv to the file name as it's mandatory 
    file type = csv[comma seperated values]
    just enter the filename to read it.
    then enter the medium of range you wanna use the output i.e enter 'p' for printing the csv file's content or 'r' to use the csv content for programming purposes which releases a list of all the elements
    then rest would work like charm
    
    """    
    
    
    if mode=='p':
        with open(filename, 'r') as reader:
            reading = csv.reader(reader)
            for i in reading:
                print(i)
    elif mode=='r':
        with open(filename, 'r') as reader:
            reading = csv.reader(reader)
            mainlist=[]
            for i in reading:
                mainlist.append(i)
            return mainlist
    else:
        print('Invalid mode')            
#---------------------------------------------------------->

def write_bin(filename: str, *vals):
    """
    
    this function should be used to write binary files via pickling
    notice%% add extensions like .bin or .pkl to the file name as it's mandatory 
    file type = binary or bin
    step1: enter the filename
    step2: enter the values you wanna input one after another in the function
    step3: enjoy... that's all
    
    """
    if vals==():
        print("Ooops.. no elements inputed.")
    else:
        real_vals = vals
        with open(filename, 'ab') as appendizer:
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
        return "process successful"
    

def read_bin(filename: str, mode: str='p'):
    """
    
this function should be used to read a pickled binary file
    notice%% add extensions like .bin or .pkl to the file name as it's mandatory 
    file type = bin or binary
    just enter the filename to read it.
    then enter the medium of range you wanna use the output i.e enter 'p' for printing the bin file's content or 'r' to use the binary content for programming purposes which releases a list of all the elements
    then rest would work like charm
    
    """

    if mode=='p':
        with open(filename, 'rb') as reader:
            reading = pickle.load(reader)

            while reading:
                print(reading)               
                try:
                    reading = pickle.load(reader)
                except:
                    break

    elif mode=='r':
        with open(filename, 'rb') as reader:
            reading = pickle.load(reader)
            mainlist = []
            while reading:
                mainlist.append(reading)
                try:
                    reading = pickle.load(reader)
                except:
                    break
            return mainlist
    else:
        print('Invalid mode')

#---------------------------------------------------------->