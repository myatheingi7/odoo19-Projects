from odoo import fields,models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Name', required=True)
    isbn = fields.Char(string='ISBN')
    author = fields.Char(string='Author')
    published_date = fields.Date(string='Published Date')
    book_price = fields.Float(string='Price')
    available_copies = fields.Integer(string='Available Copies')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    book_code = fields.Char(string='Book Code', readonly=True)

    category_id = fields.Many2one(
        'library.book.category',
        string='Category'
    )

    author_ids = fields.Many2many(
        'library.author',
        string='Authors'
    )

    def action_generate_book_code(self):
        for rec in self:
            if rec.book_code:
                continue

            all_books = self.search([('book_code', '!=', '')])
            max_num = 0

            for book in all_books:
                if book.book_code and book.book_code.startswith('BOOK'):
                    try:
                        num_str = book.book_code.replace('BOOK', '')
                        num = int(num_str)
                        if num > max_num:
                            max_num = num
                    except (ValueError, TypeError):
                        continue

            new_num = max_num + 1
            rec.book_code = f"BOOK{new_num:04d}"