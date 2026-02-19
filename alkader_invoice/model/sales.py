from odoo import models, fields, api, _


class PaymentSales(models.Model):
    _name = 'sale.order.payment'
    _description = 'Sale Order Payment Method'

    name = fields.Char(string='Name')
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)


class SalesInherit(models.Model):
    _inherit = "sale.order"

    payment_way = fields.Many2one('sale.order.payment',
                                  string='Payment Way',
                                  check_company=True,
                                  domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
