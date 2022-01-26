# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Banks Check',
    'version': '0',
    'depends': [
        'base',
        'web',
        'account'
    ],
    'author': 'Routhberis Milano',
    'description': """
        Version: odoo14 Enterprise
        Is a module custom of module Accounts and contains
        Reports in excel and pdf on banks check
    """,
    'category':  'Accounting/Accounting',
    'website': 'http://www.odoo.com/',
    'data': [
        'security/ir.model.access.csv',
        'wizard/report_bank_wizard.xml',
        'views/report_bank_qweb.xml',
        'report/report_bank.xml',
        'views/menu.xml',
    ],
    'demo': [
    ],
    'license': 'LGPL-3',
}