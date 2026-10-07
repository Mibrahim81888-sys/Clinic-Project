from odoo import fields, models


class HospitalClinic(models.Model):
    _name = 'hospital.clinic'
    _description = 'Hospital Clinic Management'

    name = fields.Char(string='Name', required=True)
    open_datetime = fields.Datetime(string='Open')
    end_datetime = fields.Datetime(string='End')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')
    state = fields.Selection(
        [
            ('new', 'New'),
            ('open', 'Open'),
            ('closed', 'Closed'),
        ],
        string='State',
        default='new',
    )
    doctor_id = fields.Many2one('res.partner', string='Doctor')
    patient_ids = fields.Many2many('hospital.patient', string='Patients')

    def open_clinic(self):
        for record in self:
            record.state = 'open'

    def close_clinic(self):
        for record in self:
            record.state = 'closed'