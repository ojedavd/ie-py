# -*- coding: utf-8 -*-
{
    'name': "ie",

    'summary': """
        Sistema para la Gestion del Instituto """,

    'description': """
        ABM alumnos, cursos, inscripciones
        Reportes de cobranzas
        Gestion de usuarios
    """,

    'author': "ojedavd",
    'website': "http://www.victorojedaok.blogspot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/ie.xml',
        'views/alumno.xml',       
        'views/ciudad.xml',       
        'views/curso.xml',       
        'views/inscripcion.xml',       
        'views/noticia.xml',       
        'views/pago.xml',       
        'views/provincia.xml',       
        'views/recurso.xml',       
        'views/sede.xml',      
        'reports.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}