# Feb 8th, 2019
# Zixin Zhang

def lib_lines(filepath):
    """
    This function takes an input Python script and count the number of lines and number of characters of this script. 

    Parameters
    ---------
    input_path(string): the path to the input .py script

    """
    in_file=open('test.py',"r") ### Open File
    lines = in_file.readlines() ### Read Lines of File
    total_lines = len(lines) ### Number of lines
    
    char = []
    for line in lines: ### For Loop for Each Line
        thisline = line.split(" ") 
        char.append(thisline)
    total_char = len(sum(char, [])) ### Number of characters
    
    return print("Total number of lines of this script is", total_lines, 
                 "\nTotal number of characters of this script is", total_char)

