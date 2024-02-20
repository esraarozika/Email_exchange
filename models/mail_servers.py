from odoo import models, fields, api, exceptions


class MailServers(models.Model):
    _name = "mail.servers"

    name = fields.Char(string="Server Name")
    outgoing_server = fields.Char(string="Outgoing Server")
    incoming_server = fields.Char(string="Incoming Server")
    port = fields.Char(string="Port")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag category already exists !"),
    ]