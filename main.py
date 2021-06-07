import leituraArquivos
import speakTexto

if __name__ == '__main__':

    name_file = input('Write the filename with its extension (text.pdf): ')
    texto = leituraArquivos.read(file_directory= './ArquivosDeTexto/' + name_file)
    speakTexto.speak(text=texto)
 