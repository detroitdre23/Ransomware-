import nacl, nacl.secret, pathlib, os, ctypes 
from time import sleep
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
hexed_key    =  input('Enter the key to decrypt your files : ')
box = nacl.secret.SecretBox(bytes.fromhex(hexed_key))                        
Paths    = [r"C:/Users/"+User+"/Desktop/files"] 
for  AllFiles in Paths:                                             
    if (pathlib.Path(AllFiles).exists()):                           
        for path, subdirs, files in os.walk(AllFiles):
            for file in files :                                 
                if(".locked" in file):                             
                    FilePath    = os.path.join(path, file)      
                    Decrypt(FilePath,box).FileE() 
change_bg()