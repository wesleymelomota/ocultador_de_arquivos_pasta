import ctypes


class Ocultador:

    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def cript(self):
        atributo_ocultar = 0x02
        retorno = ctypes.windll.kernel32.SetFileAttributesW(self.__arquivo, atributo_ocultar)
        if retorno:
            return f'arquivo Ocultado'
        else:
            return 'Não foi possivel ocultar o arquivo'


obj = Ocultador('test.txt')
print(obj.cript())
