# -*- coding: utf-8 -*-
{
    'name': "CSmart Car Rental Booking Discount Management",

    'summary': """
        Aplikasi Manajemen Diskon Booking Rental""",

    'description': """
        Aplikasi untuk me-manage diskon booking mobil
    """,

    'author': "DTBS",
    'website': "http://www.dtbsindo.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rental',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['carrent_booking'],

    # always loaded
    'data': [
        'views/booking_discount.xml'
    ],
}
