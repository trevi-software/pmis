# -*- coding: utf-8 -*-
{
    'name': 'Fancy Project WBS',
    'version': '8.0.1.0.7',
    'summary': 'Enhance the Project WBS UI',
    'author':   'Matmoz d.o.o., '
                'Project Expert Team',
    'contributors': [
        'Matjaž Mozetič <m.mozetic@matmoz.si>',
    ],
    'website': 'http://project.expert',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'depends': [
        'web_tree_dynamic_colored_field',
        'project_wbs',
        'analytic_plan'
    ],
    'data': [
        'views/project_view.xml',
        'views/analytic_view.xml'
    ],
    'demo': [],
    'installable': False,
}
