# -*- coding: utf-8 -*-
{
    'name': "Alkader Invoice",
    'summary': """
        Alkader Invoice
        """,
    'description': """
        Alkader Invoice
    """,
    'author': "elblasy.app",
    'website': "https://elblasy.app",
    'category': 'account',
    'version': '19.0.1.0.0',
    'depends': ['base', 'account', 'sale', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/report_custom_invoice.xml',

        'views/sales_view.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
