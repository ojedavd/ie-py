# -*- coding: utf-8 -*-
from openerp import http

# class Ie(http.Controller):
#     @http.route('/ie/ie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ie/ie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ie.listing', {
#             'root': '/ie/ie',
#             'objects': http.request.env['ie.ie'].search([]),
#         })

#     @http.route('/ie/ie/objects/<model("ie.ie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ie.object', {
#             'object': obj
#         })