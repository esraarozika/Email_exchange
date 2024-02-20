from email import charset

from numpy import unicode
from odoo import models, fields, api, exceptions
import email
import imaplib
import re
from bs4 import BeautifulSoup
from mistletoe import markdown
import html2text


class InBoxMail(models.Model):
    _name = "inbox.mail"
    _rec_name = "from_email"
    _order = 'id desc'

    logged_in_user = fields.Many2one("res.users", default=lambda self: self.env.user.id)
    from_email = fields.Many2one('res.partner', string='From:')
    subject = fields.Char(string='Subject:')
    text = fields.Text('Rich-text Contents', help="Rich-text/HTML message")
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Attachments',
        help='Attachments are linked to a document through model / res_id and to the message '
             'through this field.')

    def receive_mail(self):
        from_id = 0
        # print("ttt", self.get_logged_in_user())
        print(self.env.user.x_email_server.incoming_server)
        mail = imaplib.IMAP4_SSL(self.env.user.x_email_server.incoming_server)
        mail.login(self.env.user.x_email_email, self.env.user.x_email_pass)
        mail.select('inbox')
        status, data = mail.search(None, '(UNSEEN)')
        mail_ids = []
        attachment = []
        body = ""
        for block in data:
            mail_ids += block.split()

        for i in mail_ids:
            status, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    if message.is_multipart():
                        mail_content = ''
                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                            if part.get_content_type() == 'multipart/alternative':
                                for subsubpart in part.get_payload():
                                    if subsubpart.get_content_type() == 'text/plain':
                                        body = str(subsubpart.get_payload(decode=True).decode(encoding="utf-8"))+'\n'
                                        text = re.split('[*]', BeautifulSoup(body).getText())[0]
                                    elif subsubpart.get_content_type() == 'text/html':
                                        html = unicode(part.get_payload(decode=True), str(charset), "ignore").encode(
                                            'utf8', 'replace')
                            if part.get_content_type() == 'application/pdf':
                                attachment.append(self.env['ir.attachment'].create({
                                            'name': part.get_filename(),
                                            'datas': part.get_payload(),
                                            'datas_fname': part.get_filename(),
                                            # 'type': 'binary'
                                        }).id)
                            if part.get_content_type() == 'image/png' or part.get_content_type() == 'image/jpeg':
                                attachment.append(self.env['ir.attachment'].create({
                                    'name': part.get_filename(),
                                    'datas': part.get_payload(),
                                    'datas_fname': part.get_filename(),
                                    # 'type': 'binary'
                                }).id)
                            else:
                                mail_content = message.get_payload(decode=True)

                    mail_from = re.split('[<>]', mail_from)[1]
                    for rec in self.env['res.partner'].search([('email', '=', mail_from)]):
                        from_id = rec.id
                    self.env['inbox.mail'].create({
                        'logged_in_user': self.env.user.id,
                        'from_email': from_id,
                        'subject': mail_subject,
                        'text': text,
                        'attachment_ids':  [[6, 0, attachment]],
                    })
