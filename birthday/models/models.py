# -*- coding: utf-8 -*-
from odoo import models, fields, api


class event_gt_extended(models.Model):
    _inherit = 'res.partner'
    
    birthday = fields.Datetime('Date of birth')