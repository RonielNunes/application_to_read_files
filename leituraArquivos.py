import os.path
from typing import Text
 
def read(file_directory) -> str:
    text = ''

    if os.path.isfile(file_directory):

        with open(file_directory) as file:
            for line in file: 
                text += line

        file.close()
        
    else:
         text = 'Error in directory or archives no existes'
    return text
    
