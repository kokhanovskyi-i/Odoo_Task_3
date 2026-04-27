import logging

from odoo import fields, models
from ..const import GENDER_LIST

_logger = logging.getLogger(__name__)

class HrHospitalPatient(models.Model):
    _name = "hr.hospital.patient"
    _description = "Hospital patient"

    name = fields.Char(
        string="Name",
        required=True,
    )

    birth_date = fields.Date(
        string="Birth date",
        required=True,
    )

    gender = fields.Selection(
        selection=GENDER_LIST,
        string="Gender",
        required=True,
    )

    email = fields.Char(
        string="Email",
    )

    phone = fields.Char(
        string="Phone",
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
        required=True,
    )