# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cita(models.Model):
     _name = 'upopet.cita'

     fechaHora = fields.Datetime('Fecha y Hora', required = True)
     estado = fields.Selectionfields.Selection([('pendiente','Pendiente'),
                                     ('presenado','Presentado'),
                                     ('nopresentado','No Presentado'),],
                                     'Estado')

     tratamiento_ids = fields.One2many('upopet.tratamiento', string='Tratamiento')
     mascota_ids = fields.Many2one('upopet.mascota', string='Mascota')
     clinica_ids = fields.Many2one('upopet.clinica', string='Clinica')
