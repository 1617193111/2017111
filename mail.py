import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'fl4611304@163.com'
msg['to'] = '2773221059@qq.com'
msg['subject'] = 'test'
content = "自动邮件"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('fl4611304@163.com', '212zxc')
smtp.sendmail('fl4611304@163.com', '2773221059@qq.com', str(msg))
smtp.quit()