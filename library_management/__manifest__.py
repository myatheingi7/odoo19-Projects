{
    "name":"Library Management System",
    "version":"19.0.1.0.0",
    "category":"Library",
    "summary":"Manage Library Books",
    "depends":["base"],
    "data":[
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_author_views.xml",
        "views/library_book_category_views.xml",
        "views/library_borrow_views.xml",
        "views/library_book_views.xml",
        "views/res_partner_views.xml",
        "views/library_menus.xml",
        "reports/library_borrow_reports.xml",
        "wizard/library_book_report_wizard_views.xml"
    ],
    "installable":True,
    "application":True,
    "license":"LGPL-3"
}