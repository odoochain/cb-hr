# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class HrAttendanceWarningSolve(models.TransientModel):
    _name = "hr.attendance.warning.solve"
    _description = "hr.attendance.warning.solve"

    @api.multi
    def solve_warnings(self):
        context = dict(self._context or {})
        self.env["hr.attendance.warning"].browse(
            context.get("active_ids")
        ).pending2solved()
        return True
