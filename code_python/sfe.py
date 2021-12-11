from math import log2, ceil
import numpy as np

def getFonteTexto(file):
    letras = []
    fTexto = open(file, 'r')
    # cria fonte de texto
    range1 = np.arange(65, 91)
    range2 = np.arange(97, 123)
    alfabetoTxt = np.concatenate((range1, range2))
    for letra in fTexto.read():
        l = ord(letra)
        letras.append(l)

    fTexto.close()
    fonteTexto = np.asarray(letras)
    mask = np.isin( np.unique(fonteTexto),alfabetoTxt)
    for i in range(len(mask)):
        if (mask[i] == False):
            alfabetoTxt = np.append(alfabetoTxt, np.unique(fonteTexto)[i])
    return fonteTexto, alfabetoTxt

def probabilidades(fonte, alfabeto):
    prob = {}
    for letra in alfabeto:
        prob.update({letra: 1})
    for elemento in fonte:
        prob[elemento] += 1
    for e in prob:
        prob[e] /= len(fonte)

    return prob

def compute_cdf(dict):
    cdf = {}
    prev_val = 0

    for letter, value in dict.items():
        cdf[letter] = value + prev_val
        prev_val = cdf[letter]

    return cdf


def code(mids, probs):
    codes = {}

    for letter, value in mids.items():
        length = ceil(log2(1/probs[letter])) + 1
        fraction = int(str(value).split('.')[1])
        code = ''
        for _ in range(length):
            fraction = float('0.' + str(fraction))*2
            whole, fract = str(fraction).split('.')
            code += whole
            fraction = int(fract)
        codes[letter] = code

    return codes


def shannon_fano_elias_code(dict):
    cdf = compute_cdf(dict)
    midpoints = {letter: round(f - dict[letter]/2, 7) for letter, f in cdf.items()}
    codes = code(midpoints, dict)
    return codes


def shannon_fano_elias_decode(number, probs):
    bottom, top = 0, 1
    cdf = compute_cdf(probs)
    for c in str(number):
        diff = (top - bottom)/2
        if int(c) == 1:
            bottom += diff
        elif int(c) == 0:
            top -= diff

    result = ''
    for letter, f in cdf.items():
        if top <= f:
            result = letter
            break

    return result