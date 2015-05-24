# coding=utf-8
__author__ = 'Shan'
from flask import render_template
from app import app
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from threading import Thread
from config import MAIL_SERVER, ADMINS, MAIL_USERNAME, MAIL_PASSWORD
from .decorators import async

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

@async
def send_sync_email(app,sender,recipients, msg):
	'''
	with app.app_context():
		smtp.sendmail(sender, recipients, msg.as_string())
	'''
	smtp = smtplib.SMTP()
	try:
		smtp.connect(MAIL_SERVER)
		smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
		smtp.sendmail(sender, recipients, msg.as_string())
	except Exception as e:
		print(e)
	finally:
		smtp.quit()

# 发送邮件代码，暂时只支持html格式
def send_email(subject, sender, recipients, text_body, html_body):
	msg = MIMEText(html_body, 'html', 'utf-8')
	# 格式化管理员的邮件地址
	msg['From'] = _format_addr(u'noreply <%s>' % sender)
	msg['to'] = _format_addr(u'Member <%s>' % recipients[0])
	msg['Subject'] = subject

	thr = Thread(target=send_sync_email, args=[app, sender, recipients, msg])
	thr.start()

def follower_nitification(followed, follower):
	send_email("[microblog] %s is now following you!" % follower.nickname,
			   ADMINS[0],
			   [followed.email],
			   render_template("follower_email.txt", user=followed, follower=follower),
               render_template("follower_email.html", user=followed, follower=follower))
