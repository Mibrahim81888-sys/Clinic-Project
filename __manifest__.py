{
    'name': 'Hospital System',
    'version': '19.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Hospital Management System',
    'author': 'Mohamed Atef',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_system_view.xml',
        'views/patients_view.xml',
        'views/res_partner_view.xml',
        'views/templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}