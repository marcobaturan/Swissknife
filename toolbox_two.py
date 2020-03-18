# Import
import pathlib
import re


def extractor_from_files_text_to_dataset(path='',extension='*.',clue=''):
    """Extractor from files text to dataset.
        
        It is for fin in a directory any file ended by specific extension.
        Open the file and find by a key or clue specific lines.
        Save this lines in a data set file in CSV format.
        For take data type text for prepare this information for
        machine learning.
        Eample:
        extractor_from_files_text_to_dataset('data/','*.txt','age')
        
        Return:
        dataset.csv with a set of lines with strings has the 'age' word in.
        
        After this step you will need procces the data set for fit in ML.
    
    """

    # Instance de library with parameter
    p = pathlib.Path(path)
    # Init the list
    list_files=[]

    # Apply the method recursive glob with the parameter in substring .feature
    # in a loop for to append to list_files the feature files type.
    for files in p.rglob(extension):
        list_files.append(files)

    # Init the de variable for text. Read the list in loop for to open in order
    # the file in path for read the lines and attach the result in the variable.
    # Then read in a loop for the variable for select the lines by filtering
    # under conditional pattern the specific line to write in a csv file.
    lines = ''
    data = ''
    file_output = open('dataset.txt','w')
    for file in list_files:
        with open(str(file),'r') as thefile:
            lines = thefile.readlines()
        for i in range(len(lines)):
            if clue in lines[i]: 
                data = '{}'.format(lines[i])
                file_output.write(str(data))
if __name__ =='__main__':
    pass