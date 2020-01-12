# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import timedelta


class cita(models.Model):
     _name = 'upopet.cita'

     _rec_name = 'citaID'
     citaID = fields.Integer('ID cita', compute='compute_cita_log', store=False)
    
     fechaHoraInicio = fields.Datetime('Fecha y Hora Inicio', required=True, readonly=False, select=True)
     fechaHoraFin = fields.Datetime('Fecha y Hora Fin', required=True, readonly=False, select=True)
     
     state = fields.Selection([('pendiente', 'Pendiente'),
                                     ('presentado', 'Presentado'),
                                     ('nopresentado', 'No Presentado'), ],
                                     'Estado',
                                     default='pendiente')

     tratamiento_ids = fields.One2many('upopet.tratamiento', 'cita_id', string='Tratamiento')
     mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
     clinica_id = fields.Many2one('upopet.clinica', string='Clinica')
     veterinario_id = fields.Many2one('upopet.veterinario', string='Veterinario')

     @api.one
     def btn_submit_to_presentado(self):
         self.write({'state':'presentado'})
        
     @api.one
     def btn_submit_to_nopresentado(self):
         self.write({'state':'nopresentado'})
        
     #Validación fecha de inicio: tiene que ser superior que la fecha actual
     @api.one 
     @api.constrains('fechaHoraInicio')
     def _check_fechaHoraInicio(self):       
         ahora = datetime.now()
         if str(ahora) > self.fechaHoraInicio:
             raise models.ValidationError('La fecha de inicio de la cita debe ser superior a la fecha actual')
    
     #Validación fecha fin: tiene que ser superior que la fecha de inicio
     @api.one 
     @api.constrains('fechaHoraFin')
     def _check_fechaHoraFin(self):       
         if str(self.fechaHoraInicio) > self.fechaHoraFin:
             raise models.ValidationError('La fecha fin de la cita debe ser superior a la fecha de inicio')
     
     @api.onchange('fechaHoraInicio')
     def onchange_fechaHoraInicio(self):
         if (self.fechaHoraInicio != False):
             hora = self.fechaHoraInicio
             hora = datetime.strptime(hora,'%Y-%m-%d %H:%M:%S')
             hora = hora  + timedelta(minutes = 30)
             hora = str(hora)
             self.fechaHoraFin = hora
         
        
     @api.one
     def compute_cita_log(self):
         self.citaID = self.id
    
