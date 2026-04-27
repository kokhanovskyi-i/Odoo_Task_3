{
    'name': 'HR Hospital',
    'summary': 'Hospital management system',
    'author': 'Kokhanovskyi Ivan',
    'website': 'https://github.com/kokhanovskyi-i/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '19.0.1.0.0',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'data/hr_hospital.xml',
    ],

    'demo': [
        'demo/hr_hospital.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}