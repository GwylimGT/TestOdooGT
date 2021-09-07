# -*- coding: utf-8 -*-
# from odoo import http


# class EventGtExtended(http.Controller):
#     @http.route('/event_gt_extended/event_gt_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_gt_extended/event_gt_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_gt_extended.listing', {
#             'root': '/event_gt_extended/event_gt_extended',
#             'objects': http.request.env['event_gt_extended.event_gt_extended'].search([]),
#         })

#     @http.route('/event_gt_extended/event_gt_extended/objects/<model("event_gt_extended.event_gt_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_gt_extended.object', {
#             'object': obj
#         })
