# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrLeave(models.Model):

    _inherit = "hr.leave"

    extendable = fields.Boolean(
        related="holiday_status_id.extendable", store=True, readonly=True
    )
