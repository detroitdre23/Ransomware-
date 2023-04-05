Hey guys 
This is like a info file for the ransomware 
so you'll find 2 folders Source Code fih 4 files :
* Ransomware.py (the ransomware)
it's simple how it works :
- there's a function 'send_email' which will be used to send an email containing the key generated for the lock of file to the mail 'test_key_dre@hotmail' 
the pass is 'SSI2022@' if you want to try it.
You can also change to any mail you want to send to.
- a function 'after_work' which will save the current wallpaper (it will get it from a specific path and save it to 'user/wallpaper') then will change the wallpaper
with the file background.jpg which is provided.
- then l sa7 g3 the ransomware i defined a class Encrypt which has a target (the path targeted) and a box which is used in the module nacl to encrypt each file in the path
we want defining some variables.
for each file it's gonna open it read it's content encrypt using the key and writing to another file with the extension .locked and delete the original file.
I defined some environement variable : User to get current user, Key which the generated key for encrypting Box used to encrypt maxthreads for big files and Pathlist 
which the path where the files will be encrypted
Here you have to create a folder on desktop names files and put any file in it it doesn't matter what type of file it is.
kyn chwiya les variable hdok t3 lmail brk.
ani 9lbtha 3rbiya 3lsh m3lblich
anyways then with a for loop it's gonna go through the files of the path and encrypt them if the file is big more than 50mb it will use threads to encrypt it.
then we'll change wallpaper and copy the decrypt program to desktop.
* now for the DeRansomware (Decrypt file):
it's even more simple :
there's the function change_bg which will retrieve the old wallpaper saved before.
and what it will do is that it's gonna loop over the whole folder and decrypt everyfile (do the opposite thing) using the key sent to the mail i talked about earlier.
like when you double click on it it will tell you to input the key paste it and it will unlock everything and get wallpaper back.
the key is in hex format so it will be decoded to utf-8 automatically.
* background.png file which is ransome notes used as new wallpaper.
kyn tan folder images to use for hiding ns79ohom ki nkhabiw the program f image 
w kyn folder fih the hidden ssma ki khbit kolch f image w tan video kifsh drtha
now i hid everything in a picture using winrar sfx as i said.
first convert py to exe using these 2 commands
pyinstaller --onefile --noconsole Ransomware.py 
pyinstaller --noconfirm --onefile --console --hidden-import=_cffi_backend DeRansomware.py
then get the image you want convert to ico to use it as an icon 
and follow the vid i'll upload for options on sfx.
you'll get at the end a image.png file when you double click on it the image will open but in the background the ransomeware will work too.
aya thank you for reading saha shourkom 
now i'll upload too the email sending program and the certificate generation 
but i'll try to make a gui for em before.