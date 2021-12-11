from code_python import sfe
from code_python import funcoesAux
import numpy as np


def add2(binary):
    decimal = 0
    if len(binary) < 8:
        decimal = int(binary, 2)
    else:
        split_strings = []
        s = 0
        for index in range(0, len(binary), 8):
            split_strings.append(binary[index: index + 8])
        print(split_strings)

        for i in split_strings:
            s += len(str(decimal))-1
            decimal += int(i, 2) * 10 ** s
    return decimal


def dicPLista(dict):
    data = list(dict.items())
    an_array = np.array(data)
    print(an_array)
    return an_array


def main():
    lista = dicPLista(sfe.shannon_fano_elias_code(
            sfe.probabilidades(sfe.getFonteTexto("original_files/bible.txt")[0],
                               sfe.getFonteTexto("original_files/bible.txt")[1])))

    sfe.shannon_fano_elias_decode()





if __name__ == "__main__":
    main()
