# -*- coding: utf-8 -*-
from odoo import http

# class Upopet(http.Controller):
#     @http.route('/upopet/upopet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upopet/upopet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upopet.listing', {
#             'root': '/upopet/upopet',
#             'objects': http.request.env['upopet.upopet'].search([]),
#         })

#     @http.route('/upopet/upopet/objects/<model("upopet.upopet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upopet.object', {
#             'object': obj
#         })