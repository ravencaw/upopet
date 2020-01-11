# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cita(models.Model):
     _name = 'upopet.cita'

     _rec_name = 'citaID'
     citaID = fields.Integer('ID cita', compute='compute_cita_log', store=False)
    
     fechaHora = fields.Datetime('Fecha y Hora', required=True)
     estado = fields.Selection([('pendiente', 'Pendiente'),
                                     ('presentado', 'Presentado'),
                                     ('nopresentado', 'No Presentado'), ],
                                     'Estado',
                                     default='pendiente')

     tratamiento_ids = fields.One2many('upopet.tratamiento', 'cita_id', string='Tratamiento')
     mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
     clinica_id = fields.Many2one('upopet.clinica', string='Clinica')
     veterinario_id = fields.Many2one('upopet.veterinario', string='Veterinario')

<<<<<<< HEAD
#@api.one
def btn_submit_to_presentado(self):
    self.write({'estado':'presentado'})
=======
 
     @api.one
     def btn_submit_to_presentado(self):
        self.write({'estado':'presentado'})
>>>>>>> Maria
        
     @api.one
     def btn_submit_to_nopresentado(self):
        self.write({'estado':'nopresentado'})
    
     @api.one
     def compute_cita_log(self):
      self.citaID = self.id