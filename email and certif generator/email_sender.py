import tkinter
import tkinter.messagebox
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import customtkinter
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smail import sign_message

def send_email(subject, body, sender, recipients, password, CERT_FILE, KEY_FILE):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    if ',' in recipients:
        msg['To'] = (', ').join(recipients.split(','))
        recipients = (', ').join(recipients.split(','))
    else:
        msg['To'] = recipients
    signed_msg = sign_message(msg, KEY_FILE, CERT_FILE)
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo('Gmail')
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients , signed_msg.as_string())
    smtp_server.quit()
    print('mail sent')

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

f = customtkinter.CTk()
f.title("Email Sender")
f.geometry(f"{920}x{640}")



# create main entry and button
f.logo_label = customtkinter.CTkLabel(f, text="Signed Email Sender", font=customtkinter.CTkFont(size=20, weight="bold"))
f.logo_label.grid(row=0, column=6, padx=20, pady=(20, 10))
f.label_subject = customtkinter.CTkLabel(f, text="Email Subject :",  font=("Times", 18, "bold"))
f.label_subject.grid(row=1, column=4, padx=20, pady=20)
f.subject = customtkinter.CTkEntry(f)
f.subject.grid(row=1, column=6, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
f.label_body = customtkinter.CTkLabel(f, text="Email Body :",  font=("Times", 18, "bold"))
f.label_body.grid(row=2, column=4, padx=20, pady=20)
f.body = customtkinter.CTkTextbox(f, width=200)
f.body.grid(row=2, column=6, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
f.label_recipients = customtkinter.CTkLabel(f, text="Email Recipients : (separate with commas)",  font=("Times", 18, "bold"))
f.label_recipients.grid(row=3, column=4, padx=20, pady=20)
f.recipients = customtkinter.CTkEntry(f)
f.recipients.grid(row=3, column=6, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
f.button_recipients = customtkinter.CTkButton(master=f, border_width=2, text="Browse", command=lambda: f.recipients.insert(0,customtkinter.filedialog.askopenfile().read()))
f.button_recipients.grid(row=3, column=8, padx=(20, 20), pady=(20, 20), sticky="nsew")
f.label_key_file = customtkinter.CTkLabel(f, text="Key File : ",  font=("Times", 18, "bold"))
f.label_key_file.grid(row=4, column=4, padx=20, pady=20)
f.key_file = customtkinter.CTkEntry(f)
f.key_file.grid(row=4, column=6, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
f.button_key_file = customtkinter.CTkButton(master=f, border_width=2, text="Browse", command=lambda: f.key_file.insert(0,customtkinter.filedialog.askopenfile().name))
f.button_key_file.grid(row=4, column=8, padx=(20, 20), pady=(20, 20), sticky="nsew")
f.label_cert_file = customtkinter.CTkLabel(f, text="Certificate File : ",  font=("Times", 18, "bold"))
f.label_cert_file.grid(row=5, column=4, padx=20, pady=20)
f.cert_file = customtkinter.CTkEntry(f)
f.cert_file.grid(row=5, column=6, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
f.button_cert_file = customtkinter.CTkButton(master=f, border_width=2, text="Browse", command=lambda: f.cert_file.insert(0,customtkinter.filedialog.askopenfile().name))
f.button_cert_file.grid(row=5, column=8, padx=(20, 20), pady=(20, 20), sticky="nsew")
f.mail_label = customtkinter.CTkLabel(f, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
f.mail_label.grid(row=6, column=2, padx=20, pady=(20, 10))
f.button_send_mail = customtkinter.CTkButton(master=f, border_width=2, text="Send Email", command= lambda: [send_email(f.subject.get(),f.body.get(1.0, "end-1c"),"detroitdre2022@gmail.com",f.recipients.get(),"yaikwnsfztqybqdg",f.cert_file.get(), f.key_file.get()),f.mail_label.configure(text="Mail Sent")])
f.button_send_mail.grid(row=6, column=8, padx=(10, 10), pady=(10, 10), sticky="nsew")


if __name__ == "__main__":
    
    f.mainloop()
