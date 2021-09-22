# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_order_checkbox_show_unit_price(models.Model):
    _inherit = 'sale.order.line'

    show_unit_price_to_client = fields.Boolean(string="Show Unit Price to client", required=True, default=True)
    extra_field_test = fields.Boolean(string="Extra test", required=True, default=True)