from io import BytesIO
import base64
from datetime import datetime
import xlsxwriter
from odoo import models, fields, _
from odoo.exceptions import UserError


class LibraryBookReportWizard(models.TransientModel):
    _name = 'library.book.report.wizard'
    _description = 'Library Book Report Wizard'

    category_ids = fields.Many2many(
        'library.book.category',
        string='Category'
    )
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    def action_export_excel(self):
        self.ensure_one()
        domain = []

        if self.category_ids:
            domain.append(('category_id', 'in', self.category_ids.ids))
        if self.from_date:
            domain.append(('create_date', '>=', self.from_date))
        if self.to_date:
            domain.append(('create_date', '<=', self.to_date))

        active_book_ids = self.env.context.get('active_ids')
        if active_book_ids:
            selected_books = self.env['library.book'].browse(active_book_ids)
            books = selected_books.filtered_domain(domain)
        else:
            books = self.env['library.book'].search(domain)

        if not books:
            raise UserError(_('No books found matching your criteria. Please adjust your filters or select books first.'))
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        ws = workbook.add_worksheet('Book List')
        header_fmt = workbook.add_format({'bold': True, 'bg_color': '#f2f2f2', 'border': 1})

        headers = [
            'Book Code',
            'Book Name',
            'Category',
            'Author',
            'Price',
            'Available Copies'
        ]
        for col, header in enumerate(headers):
            ws.write(0, col, header, header_fmt)

        row = 1
        for book in books:
            ws.write(row, 0, book.book_code or '')
            ws.write(row, 1, book.name or '')
            ws.write(row, 2, book.category_id.name or '')

            author_name = ''
            if hasattr(book, 'author_ids'):
                author_name = ', '.join(a.name for a in book.author_ids)
            elif hasattr(book, 'author_id'):
                author_name = book.author_id.name or ''
            elif hasattr(book, 'author'):
                author_name = book.author or ''
            ws.write(row, 3, author_name)

            price = getattr(book, 'price', getattr(book, 'book_price', 0.0))
            ws.write(row, 4, price)

            ws.write(row, 5, book.available_copies or 0)
            row += 1

        workbook.close()
        output.seek(0)
        filename = f"Book_List_{datetime.now().strftime('%Y%m%d')}.xlsx"
        att = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.b64encode(output.read()),
            'res_model': 'library.book.report.wizard',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{att.id}?download=true',
            'target': 'self',
        }

