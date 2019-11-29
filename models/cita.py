# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cita(models.Model):
     _name = 'upopet.cita'

     fechaHora = fields.Datetime('Fecha y Hora', required = True)
     estado = fields.Selection([('pendiente','Pendiente'),
                                     ('presentado','Presentado'),
                                     ('nopresentado','No Presentado'),],
                                     'Estado')

     tratamiento_ids = fields.One2many('upopet.tratamiento', 'cita_id', string='Tratamiento')
     mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
     clinica_id = fields.Many2one('upopet.clinica', string='Clinica')
     veterinario_id = fields.Many2one('upopet.veterinario', string='Veterinario')
