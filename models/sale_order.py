from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def copy(self, default=None):
        user = self.env.user
        if not user.has_group('restrict_duplicate_button.group_allow_duplicate'):
            raise models.ValidationError("No tienes permiso para duplicar órdenes de venta.")
        return super(SaleOrder, self).copy(default)
