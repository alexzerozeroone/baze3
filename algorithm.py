from constants import *
import math

def start(encryptionText):
    encryptionLength = len(encryptionText)
    encryptedText = ":%s:%d:" % (bin(encryptionLength), encryptionLength)
    
    for i in range(encryptionLength):
        encryptedText += "%s" % chr(ord(encryptionText[i]) ^ i)
    
    return encryptedText