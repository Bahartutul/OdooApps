from odoo import fields, models, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    print_product_image=fields.Boolean(default=True,string="print Product Image")