from odoo import fields,models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Name', required=True)
    isbn = fields.Char(string='ISBN')
    author = fields.Char(string='Author')
    published_date = fields.Date(string='Published Date')
    price = fields.Date(string='Price')
    available_copies = fields.Integer(string='Available Copies')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)