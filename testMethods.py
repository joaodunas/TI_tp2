
import lzwencoder
import lz78
import lzw


def main():
    #lzwencoder.encode("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.txt")
    #lzwencoder.decode("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.lzw")
    #lz78.encodeLZ("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.txt", "C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.lz78")
    #lz78.decodeLZ("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.lz78", "C:\\Users\\35191\\Downloads\\TP2\\dataset\\bibledecodelz78.txt")
    infile = lzw.readbytes("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.txt")
    compressed = lzw.compress(infile)
    lzw.writebytes("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.lzw", compressed)
    i = lzw.readbytes("C:\\Users\\35191\\Downloads\\TP2\\dataset\\bible.lzw")
    uncompressed = lzw.decompress(i)
    with open("C:\\Users\\35191\\Downloads\\TP2\\dataset\\biblelzw.txt", 'w') as file:
        for bt in uncompressed:
            file.write(str(bt))

if __name__ == "__main__":
    main()
