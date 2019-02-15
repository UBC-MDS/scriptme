# LibRely (Python)

### Collaborators
| Name | GitHub Handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


### Releases

[Milestone 1 Release](https://github.com/UBC-MDS/LibRely-Py-/releases/tag/V1.0)

### Overview
The `LibRely` package is designed to provide a meta analysis of Python scripts to aid in the workflow for a data science or software development project. The functionalities in this package interpret scripts to compile library/module dependencies, document specific functions imported in the script and measure the length of the script by the number of lines and characters.

The user can use `LibRely` to better understand the packages used in a script authored by someone else. Alternatively, a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `LibRely` package.

`lib_search()`

- Input parameter(string): a file path to the script
- Output parameter(list): a list of dependencies
- Function purpose: find and list the libraries/modules used in the script passed as an argument

`lib_count()`

- Input parameter(string): a file path to the script
- Output parameter(dataframe): a data frame has
- Function purpose: count the functions used and detail their corresponding libraries/packages

 `lib_lines()`

 - Input parameter(string): a file path to the script
 - Output parameter(print statements):
 - Function purpose: count the number of lines and characters of the script


### Python Ecosystem

- **Python**: We were not able to find any Python software packages that address the same functionality as we intend to with ```LibRely```, however, a package called [meta_func](https://pypi.org/project/meta_func/) does keep track of metadata about function use in a given script you examine. Our package fits the python ecosystem because it analyzes a `.py` script and all these functions return common return types, like a list and a pandas' dataframe. 

