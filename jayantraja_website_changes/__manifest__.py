# -*- coding: utf-8 -*-
{
    'name': 'Jayanthi Raja: Website Configurator Changes',
    'summary': '''
        Modifications to website.
    ''',
    'description': '''
        [LARS] - TASK ID: 2985450
        Modification on how websites are generated:
        - Disabling "Skip and start from scratch" in the welcome screen.
        - Enabling a "Skip button" in the welcome screen that skips the selection of a theme.
    ''',
    'license': 'OPL-1',
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'category': 'Development Services/Custom Development',
    'version': '15.0.1',
    'depends': [
        'website',
    ],
    'data': [
    ],
    'assets': {
        'website.website_configurator_assets_js': [
            ('remove', 'website/static/src/components/configurator/configurator.js'),
            'jayantraja_website_changes/static/src/**/*.js',
        ],
        'web.assets_qweb': [
            'jayantraja_website_changes/static/src/**/*.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False
}
