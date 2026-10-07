from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    clinic_ids = fields.One2many(
        'hospital.clinic', 'doctor_id', string='Clinics'
    )
