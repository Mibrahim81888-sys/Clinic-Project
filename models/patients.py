from odoo import fields, models


class Patients(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender',
    )
    phone = fields.Char(string='Phone')
