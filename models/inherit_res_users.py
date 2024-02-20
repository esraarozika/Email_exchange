from odoo import models, fields, api, exceptions, tools
import re


class MailResUser(models.Model):
    _inherit = "res.users"

    x_email_email = fields.Char(string="Email", required=True)
    x_email_pass = fields.Char(string="Password", required=True)
    x_email_server = fields.Many2one('mail.servers', string="Email Server")
    x_outgoing_server = fields.Many2one('mail.servers', string="Outgoing Server")
    x_incoming_server = fields.Many2one('mail.servers', string="Incoming Server")
    x_smtp_port = fields.Integer(string="SMTP Port")

    @api.onchange('x_email_email')
    def on_change_login(self):
        if self.x_email_email and tools.single_email_re.match(self.x_email_email):
            self.email = self.x_email_email

    @api.onchange('x_email_email')
    @api.depends('x_email_email')
    def get_server(self):
        for rec in self:
            mail_extension = re.split('[@.]', rec.x_email_email)[1]
            print(mail_extension)
            for server in self.env['mail.servers'].search([('name', '=', mail_extension)]):
                print(">>>>>>", server.name)
                rec.x_email_server = server.id
