# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Medical Surgical Appointment',
    'summary': """
        medical_surgical_appointment""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Creu Blanca',
    'website': 'www.creublanca.es',
    'depends': [
        'cb_medical_administration_center',
        'cb_medical_careplan_sale',
        'medical_administration_encounter',
        'medical_medication',
        'medical_administration_second_lastname',
        'product',
        'mail',
    ],
    'external_dependencies': {
        'python': [
            'fuzzywuzzy',
        ],
    },
    'data': [
        'wizards/medical_surgical_appointment_patient.xml',
        'data/surgical_appointment_sequence.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/medical_surgical_appointment.xml',
        'views/product_template.xml',
        'views/res_partner.xml',
        'views/webclient_templates.xml',
    ],
}
