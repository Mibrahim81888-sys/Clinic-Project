# from odoo import http


# class HospitalSystem(http.Controller):
#     @http.route('/hospital_system/hospital_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_system/hospital_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_system.listing', {
#             'root': '/hospital_system/hospital_system',
#             'objects': http.request.env['hospital_system.hospital_system'].search([]),
#         })

#     @http.route('/hospital_system/hospital_system/objects/<model("hospital_system.hospital_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_system.object', {
#             'object': obj
#         })
