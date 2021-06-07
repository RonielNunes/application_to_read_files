import os.path
from typing import Text
 
def leituraArquivo(file_directory) -> str:
    text = '' # empity text - texto vazio
    if os.path.isfile(file_directory): #Verifica se o arquovo é uma file retornando true or false
        with open(file_directory) as file: # leitura do abertura do arquivo
            for line in file: 
                #print(line) #leiura das linhas que compõem o texto
                text += line #armazenando
            #print('Text: ' + text)
        file.close()
    else:
         text = 'Error in directory or archives no existes'
    return text
    



file_directory = './ArquivosPdfs/teste.pdf'

texto = leituraArquivo(file_directory=file_directory) 
if texto != '':
    ##pass
    print(texto)
else:
    print('Error')