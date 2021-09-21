# -*- coding: utf-8 -*-
# from odoo import http


# class VisibilityUnitPrice(http.Controller):
#     @http.route('/visibility_unit_price/visibility_unit_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visibility_unit_price/visibility_unit_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('visibility_unit_price.listing', {
#             'root': '/visibility_unit_price/visibility_unit_price',
#             'objects': http.request.env['visibility_unit_price.visibility_unit_price'].search([]),
#         })

#     @http.route('/visibility_unit_price/visibility_unit_price/objects/<model("visibility_unit_price.visibility_unit_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visibility_unit_price.object', {
#             'object': obj
#         })
