# -*- coding: utf-8 -*-
{
    'name': "Product Image(changeable) On Sale Order Line",

    'summary': """
        Display product image on sale order line + optional product line, print product image on sale order report""",

    'description': """
        Display product image on sale order line and optional product line. It will also display product image on sale order report. 	
			Product Image On Sale Order Line in odoo,
			Product Image On Optional Product Line in odoo,
			Sale report with product image in odoo,
			product image on sale order line and sale report in odoo,
			Identify product via image in odoo,
			Identify priduct via image on sale report in odoo
    """,

    'author': "B-Infotech",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '16.0.0.1',
    'license' : 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/sale_order_optional_products.xml',
        'reports/sale_quotation_report.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'currency': "USD",
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': False,
    "images":['static/description/sale.gif'],
    'price': 25.00,
}
