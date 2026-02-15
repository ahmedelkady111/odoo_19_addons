from odoo import api, models
import logging

_logger = logging.getLogger(__name__)


class CustomInvoiceReport(models.AbstractModel):
    _name = 'report.alkader_invoice.custom_invoice'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('alkader_invoice.custom_invoice')

        obj = self.env[report.model].browse(docids)

        invoices = []
        for doc in obj:
            invoices.append(doc)

        return {
            'invoices': invoices,
        }
