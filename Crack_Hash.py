import hashlib
from colorama import *
import time
import sys 
import pyfiglet
#text = input("enter the text : ")
log =pyfiglet.figlet_format("Crack_Hash")
print(log)
text ="This tool supports these types."

for char in text:
                    print(char, end='', flush=True)
                   # print('-----------------------')  
                    time.sleep(0.1) 
print('\n')
print('-----------------------')
print('md5')
print('sha224')
print('sha256')
print('sha384')
print('sha512') 
print('sha3_224')
print('sha3_256')
print('sha3_384') 
print('sha3_512') 
Hash =input('Enter The Hash : ')
List =input('Enter The List : ')
type_hash=input('enter the type hash: ')
ff =open(List ,"r")
f =ff.read().splitlines()
if type_hash == 'md5':
                         for line in f:
                                          time.sleep(7)
                                          enl=line.encode("utf-8")
                                          m = hashlib.md5()
                                          m.update(enl)
                                          m.digest()
                                          hh= m.hexdigest()

                                          if hh == Hash:
                                                           print(Hash,"=====>> ", Fore.GREEN +line)
                                                           break
                                          else:
                                                  print(Fore.RED,'Error ==> ' ,Hash ,line)

if type_hash == 'sha224':
                            for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha224()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha256':
                            for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha256()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha384':
                            for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha384()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)

if type_hash == 'sha512':
                            for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha512()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha3_224':
                          for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha3_224()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha3_256':
                          for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha3_256()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha3_384':
                          for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha3_384()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
if type_hash == 'sha3_512':
                          for line in f:
                                             time.sleep(7)
                                             enl=line.encode("utf-8")
                                             m = hashlib.sha3_512()
                                             m.update(enl)
                                             m.digest()
                                             hh= m.hexdigest()

                                             if hh == Hash:
                                                              print(Hash,"=====>> ", Fore.GREEN +line)
                                                              break
                                             else:
                                                     print(Fore.RED,'Error ==> ' ,Hash ,line)
