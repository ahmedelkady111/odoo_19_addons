from odoo import api, models
import logging

_logger = logging.getLogger(__name__)


class CustomInvoiceReport(models.AbstractModel):
    _name = 'report.alkader_invoice.custom_invoice'
    _description = 'Custom Invoice Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        
        invoices = []
        for doc in docs:
            invoices.append(doc)

        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'invoices': invoices,
        }
    
    def _render_qweb_html(self, docids, data=None):
        """Override to ensure UTF-8 encoding for Arabic text"""
        result = super()._render_qweb_html(docids, data)
        if isinstance(result, bytes):
            # Ensure result is properly decoded as UTF-8
            try:
                result = result.decode('utf-8')
            except UnicodeDecodeError:
                _logger.warning("Failed to decode report as UTF-8, trying to fix encoding")
                # If it's already garbled, try to fix it
                try:
                    result = result.decode('latin-1').encode('utf-8').decode('utf-8')
                except:
                    result = result.decode('utf-8', errors='ignore')
        return result
