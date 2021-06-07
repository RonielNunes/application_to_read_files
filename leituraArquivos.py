import os.path
 
def leituraArquivo(file_directory):
    if os.path.isfile(file_directory): #Verifica se o arquovo é uma file retornando true or false
        with open(file_directory) as file: # leitura do abertura do arquivo
            print(file.read()) #leiura das linhas que compõem o texto
    else:
        print('Error in directory or archives no existes')

file_directory = './ArquivosPdfs/teste.pdf'

leituraArquivo(file_directory=file_directory) 