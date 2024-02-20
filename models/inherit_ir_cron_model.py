from odoo import models, fields, api, exceptions, tools


class InheritIrCron(models.Model):
    _inherit = "ir.cron"

    logged_in_user = fields.Many2one("res.users", default=lambda self: self.env.user.id)

    @api.onchange('logged_in_user')
    def change_scheduler_user(self):
        for rec in self:
            print('yyyyyyyyyyy')
            for cron in rec.env['ir.cron'].search('name', '=', 'Check Mail Inbox'):
                cron.user_id = rec.logged_in_user
