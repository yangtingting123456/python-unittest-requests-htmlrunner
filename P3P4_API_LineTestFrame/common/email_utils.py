#!/usr/bin/env python
# encoding: gbk
# @author: liusir
# @file: email_utils.py
# @time: 2020/10/18 2:38 ����

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import config

class EmailUtils:
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 25
        self.smtp_sender = '329999897@qq.com'
        self.smtp_password = 'wvcsgattkyqqbhah'
        self.smtp_receiver = config.SMTP_RECEIVER
        self.smtp_cc = '329999897@qq.com,2431904050@qq.com'
        self.smtp_subject = 'P3P4�ӿ��Զ������Ա���'
        self.smtp_body = smtp_body
        self.smtp_attch_path = smtp_attch_path

    def email_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf-8') )
        if self.smtp_attch_path:
            attach_file_obj = MIMEText(open(self.smtp_attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.smtp_attch_path)))
            message.attach(attach_file_obj)
        return message

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server,self.smtp_port)
        smtp.login(self.smtp_sender,self.smtp_password)
        smtp.sendmail( self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(',')   ,self.email_message_body().as_string() )

if __name__=='__main__':
    email_u = EmailUtils('testʹ��','./API_TEST_V2.0.html')
    email_u.send_mail()
