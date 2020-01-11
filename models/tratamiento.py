# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tratamiento(models.Model):
    _name = 'upopet.tratamiento'

    _rec_name = 'tratamientoID'
    tratamientoID = fields.Integer('ID tratamiento', compute='compute_tratamiento_log', store=False)
    
    patologia = fields.Char('Patología', size=20, required=True)
    inicio = fields.Datetime('Inicio', required=True, readonly=False, select=True)
    fin = fields.Datetime('Fin', required=False, readonly=False, select=True)
    observaciones = fields.Text()

    cita_id = fields.Many2one('upopet.cita', string='Cita')
    mascota_id = fields.Many2one('upopet.mascota', string='Mascota')
    veterinario_id = fields.Many2one('upopet.veterinario', string='Veterinario')
    medicamento_ids = fields.Many2many('upopet.medicamento', string='Medicamento')

    state = fields.Selection([('solicitado','Solicitado'), 
                              ('enTratamiento', 'En Tratamiento'),
                              ('finalizado','Finalizado'),], 
                              'Estado', 
                              default = 'solicitado')
    
        
    @api.one
    def btn_submit_to_enTratamiento(self):
        self.write({'state':'enTratamiento'})


    @api.one
    def btn_submit_to_Finalizado(self):
        self.write({'state':'finalizado'})
    
    @api.one
    def compute_tratamiento_log(self):
      self.tratamientoID = self.id
   