import base64
import re
import numpy as np
import cv2
from odoo import models, fields, api, exceptions, tools, modules


class InheritMailMail(models.Model):
    _name = "inherit.mail.mail"
    _inherit = "mail.mail"
    _rec_name = "to_email"

    logged_in_user = fields.Many2one("res.users", default=lambda self: self.env.user.id)
    to_email = fields.Many2one('res.partner', string='To:', required=True)
    cc_email = fields.Many2one('res.partner', string='CC:')

    @api.depends('logged_in_user')
    @api.onchange('logged_in_user')
    def pass_logged_in_user(self):
        for rec in self:
            for inbox in rec.env['ir.cron'].search([('cron_name', '=', 'Check Mail Inbox'),
                                                    ('model_id', '=', 'inbox.mail')]):
                inbox.write({'user_id': rec.logged_in_user.id})

    @api.multi
    def _send_prepare_body(self):
        user = self.env.user.partner_id
        user_name = self.env.user.name
        user_position = self.env.user.function
        user_phone = self.env.user.phone
        user_mobile = self.env.user.mobile
        user_email = self.env.user.email
        user_website = self.env.user.website
        user_logo = self.env.user.x_logo
        self.body_html = self.body_html + "<br><br><br><br>" + "<img width='300' height='100' data - image - whitelisted = ''" \
                                                               " class ='CToWUd a6T' tabindex='0' src='data:image/png;base64," \
                         + str(user_logo, "utf-8") + "'> <br><br>" + user_name + "<br>" + user_position + "<br>" \
                         + user_phone + "<br>" + user_mobile + "<br>" + user_email + "<br>" + user_website + "<br>"
        res = super(InheritMailMail, self)._send_prepare_body()
        return res

    @api.onchange('to_email')
    def get_email_to(self):
        for rec in self:
            rec.email_to = rec.to_email.email
            print("email to", rec.email_to)
            print("rec.to_email.email", rec.to_email.email)
            logged_in_user = rec.env.user
            outgoing_server_id = rec.env['ir.mail_server'].search([
                ('smtp_user', '=', logged_in_user.x_email_email)]).id
            if outgoing_server_id:
                rec.mail_server_id = outgoing_server_id
            else:
                outgoing_server_id = rec.env['ir.mail_server'].create({
                    'name': logged_in_user.name,
                    'smtp_host': logged_in_user.x_email_server.outgoing_server,
                    'smtp_encryption': 'starttls',
                    'smtp_port': logged_in_user.x_email_server.port,
                    'smtp_user': logged_in_user.x_email_email,
                    'smtp_pass': logged_in_user.x_email_pass,
                }).id
                rec.mail_server_id = outgoing_server_id

    @api.onchange('cc_email')
    def get_email_cc(self):
        for rec in self:
            rec.email_cc = rec.cc_email.email
