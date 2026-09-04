from odoo import fields,models

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Author Name', required=True)
    email = fields.Char(string='Email')
    description = fields.Text(string='Description')