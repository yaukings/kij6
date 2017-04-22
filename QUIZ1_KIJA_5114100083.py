# convert character to binary
def tobinary(character):
    return (bin(ord(character)))

# Inverse Operation
def INV(q):
    c = int(q, 2)
    temp = []
    r = len(q)
    count = 0
    c = "{0:0b}".format(c)
    #print c
    for x in range(0,len(q)):
        if q[x]!='b' or len(q)!=9:
            if q[x] == '1':
                temp.append('0')
                count += 1
            else:
                temp.append('1')
                count += 1
    return ''.join(temp)

# MOD operation
def MOD(q):
    temp = (int(q, 2) % 255)
    temp = "{0:0b}".format(temp)
    return temp

#convert binary to string
def tostring(X):
    return chr(int(X[:8], 2))

# XOR operation
def XOR(q, w):
    c = int(q,2)^int(w,2)
    c = "{0:0b}".format(c)
    return c

# SUM operation
def SUM(q, w):
    c = (int(q,2) + int(w,2))
    c = "{0:0b}".format(c)
    return c

def encrypt(e,k0,k1):
    return tostring(MOD(SUM(XOR(e, k0), k1)))

def decrypt(e,k1,k0):
    return tostring(XOR(MOD(SUM(e, INV(k1))), k0))

if __name__ == '__main__':
    print "Program Quiz No.3\n"
    print "SYAUKI AULIA THAMRIN"
    print "5114100083\n"

    # Read File Txt
    file_object = open("test.txt", 'r')

    # read file
    text = file_object.readline()

    # print file contents
    print "Konten file:"
    print "%s\n" % text

    # print character length
    print("panjang karakter: %d\n") % len(text)

    # our key
    key = "syauki25"

    e = []
    d = []

    first = 0
    end = 4

    # do Encryption for each character
    for x in range(0, len(text)):
        # algorithm for encrypt the plain text depends on quiz no.1
        e.append(encrypt(tobinary(text[x]),tobinary(key[first]),tobinary(key[end])))
        if first + 1 > 4:
            first = 0
        else:
            first += 1

        if end + 1 > 7:
            end = 4
        else:
            end += 1

    # change list into string
    e_join = ''.join(e)

    # print the Encrypt result
    print "Hasil Encrypt (Ciphertext):"

    print e_join

    first = 0
    end = 4

    for x in range(0, len(text)):
        # algorithm for decrypt depends on quiz no.1a answer
        d.append(decrypt(tobinary(e[x]),tobinary(key[end]),tobinary(key[first])))
        if first + 1 > 4:
            first = 0
        else:
            first += 1

        if end + 1 > 7:
            end = 4
        else:
            end += 1

    # print the Decrypt result
    print "\n"
    print "Hasil Decrypt:"

    # change list into string
    d_join = ''.join(d)
    print d_join

    # print character length after decrypt
    print "\nJumlah karakter setelah decrypt : %d" % len(d)

    # close file
    file_object.close()




