from odoo import models, fields, api, exceptions, tools


class InheritResPartner(models.Model):
    _inherit = "res.partner"

    x_logo = fields.Binary(string="Company Logo")
