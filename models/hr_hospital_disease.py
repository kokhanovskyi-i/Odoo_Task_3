import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class HrHospitalDisease(models.Model):
    _name = "hr.hospital.disease"
    _description = "Disease"

    code = fields.Char(
        string="Code",
        required=True,
    )

    name = fields.Char(
        string="Name",
        required=True,
    )