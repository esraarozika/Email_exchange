# -*- coding: utf-8 -*-
{
    'name': "Email Exchange",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'snailmail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/inherit_res_users.xml',
        'views/inherit_res_partner.xml',
        'views/email_outbox.xml',
        'views/email_inbox.xml',
        'views/mail_servers.xml',
        'data/cron.xml',

    ],
    'sequence': 0,
}
