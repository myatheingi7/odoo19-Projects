from odoo import fields,models

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Book Borrow Record'

    name = fields.Char(string='Reference', required=True)
    member_id = fields.Many2one(
        'res.partner',
        string='Member', required=True
    )
    book_id = fields.Many2one(
        'library.book',
        string='Book', required=True
    )
    borrow_date = fields.Date(string='Borrow Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True)
    active = fields.Boolean(string='Active', default=True)

    def action_borrow(self):
        self.write({'state':'borrowed'})

    def action_return(self):
        self.write({'state':'returned'})

    def action_cancel(self):
        self.write({'state':'cancelled'})


