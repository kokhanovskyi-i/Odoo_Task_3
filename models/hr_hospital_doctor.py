import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class HrHospitalDoctor(models.Model):
    _name = "hr.hospital.doctor"
    _description = "Hospital doctor"

    name = fields.Char(
        string="Name",
        required=True,
    )

    specialty = fields.Char(
        string="Specialty",
        required=True,
    )

    email = fields.Char(
        string="Email",
        required=True,
    )

    phone = fields.Char(
        string="Phone",
        required=True,
    )