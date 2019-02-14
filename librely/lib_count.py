
def lib_count(filepath):

    """
    This function takes in a Python script (.py) and returns two lists
    containing the libraries and functions imported at the top of the script

    Parameters
    ----------
    input_path(string): The path to the input .py script

    Return
    ----------
    dependency, function_list(list): Lists that stores all the dependencies
    """
        ##### First Function Block
    dependency=[] #### Set an empty list containing dependencies
    function_list=[]

    in_file=open(filepath,"r") ### Open File
    lines = in_file.readlines() ### Read Lines of File

    for line in lines: ### For Loop for Each Line
        thisline=line.split(" ") ### Split Every Word in the Line

        if thisline[0] == 'import': ### If the line starts with 'import'
            edits = thisline[1].replace('\n', '') #### Grab the word after it
            dependency.append(edits) #### Append the word into dependency list

        elif thisline[0] == 'from':
            edits = thisline[1] ##### To Deal with packages where someone imports using 'from'
            dependency.append(edits) ### append the word after 'from' to dependency list

            ### Second core aspect, this grabs the functions imported at the top of the script
            func_top = thisline[3].replace('\n','') ### Grab any functions from top of script
            function_list.append(func_top) ### Grab functions at top of script if directly imported


    return dependency, function_list
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("str", help="display the dependencies and function lists", type=str)
args = parser.parse_args()
print(lib_count(args.str))
