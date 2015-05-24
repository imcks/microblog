# coding=utf-8
__author__ = 'Shan'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from threading import Thread

MAIL_SERVER = 'smtp.163.com'
# MAIL_USE_TLS = False
# MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# 管理员列表
ADMINS = ['kaishan0810@163.com']

def send_sync_email(sender,receiver, masg):
	try:
		smtp = smtplib.SMTP()
		smtp.connect(MAIL_SERVER)
		smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
		smtp.sendmail(sender, receiver, masg)
	except Exception as e:
		print(e)
	finally:
		smtp.quit()
	# print('hello python.')


sender = ADMINS
receiver = 'supercks@163.com'
subject = 'python email test'
html_body = '<html><body>lsdhgs python22222</body></html>'

msg = MIMEText(html_body, 'html', 'utf-8')
msg['Subject'] = subject
# smtp = smtplib.SMTP()
# smtp.connect(MAIL_SERVER)
# smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
masg = msg.as_string()
# print masg
thr = Thread(target=send_sync_email, args=[sender, receiver,  masg])
thr.start()
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.sendmail(sender, receiver, masg)
# smtp.quit()