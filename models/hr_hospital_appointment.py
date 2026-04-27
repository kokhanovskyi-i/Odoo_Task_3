import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class HrHospitalAppointment(models.Model):
    _name = "hr.hospital.appointment"
    _description = "Hospital appointment"
    _rec_name = 'appointment_datetime'

    appointment_datetime = fields.Datetime(
        string="Appointment and time",
        default=fields.Datetime.now,
        required=True,
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
        required=True,
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string="Patient",
        required=True,
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string="Disease",
    )