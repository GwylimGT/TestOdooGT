# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_order_checkbox_show_unit_price(models.Model):
    _inherit = 'sales.order'

    show_unit_price_to_client = fields.Boolean(string="Show Unit Price to client", required=True, default=True)