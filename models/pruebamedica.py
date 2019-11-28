# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pruebamedica(models.Model):
     _name = 'upopet.pruebamedica'

     cif = fields.Char('CIF', size = 9, required = True)
     nombre = fields.Char('Nombre', size = 70, required = True)
     direccion = fields.Char('Direccion', size = 60, required = True)
     telefono = fields.Char('Telefono', size = 9, required = True)

     veterinario_ids = fields.Many2one('upopet.veterinario', string='Veterinario')
     mascota_ids = fields.Many2one('upopet.mascota', string='Mascota')
     clinica_ids = fields.Many2one('upopet.clinica', string='Clinica')
