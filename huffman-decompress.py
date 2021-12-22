# 
# Decompression application using static Huffman coding
#
# Usage: python huffman-decompress.py InputFile OutputFile
# This decompresses files generated by the huffman-compress.py application.
# 
# Copyright (c) Project Nayuki
# 
# https://www.nayuki.io/page/reference-huffman-coding
# https://github.com/nayuki/Reference-Huffman-coding
# 

import huffmancoding


# Command line main application function.
def main(inputfile, outputfile):
	
	# Perform file decompression
	with open(inputfile, "rb") as inp, open(outputfile, "wb") as out:
		bitin = huffmancoding.BitInputStream(inp)
		canoncode = read_code_len_table(bitin)
		code = canoncode.to_code_tree()
		decompress(code, bitin, out)


def read_code_len_table(bitin):
	def read_int(n):
		result = 0
		for _ in range(n):
			result = (result << 1) | bitin.read_no_eof()  # Big endian
		return result
	
	codelengths = [read_int(8) for _ in range(257)]
	return huffmancoding.CanonicalCode(codelengths=codelengths)


def decompress(code, bitin, out):
	dec = huffmancoding.HuffmanDecoder(bitin)
	dec.codetree = code
	while True:
		symbol = dec.read()
		if symbol == 256:  # EOF symbol
			break
		out.write(bytes((symbol,)))

