import win32com.client
import os
path = 'C:/testes/mail'
files = [f for f in os.listdir(path) if '.msg' in f]
for file in files:
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    msg = outlook.OpenSharedItem(os.path.join(path, file))
    att=msg.Attachments
    for i in att:
        i.SaveAsFile(os.path.join('C:/testes/email_download', i.FileName))
