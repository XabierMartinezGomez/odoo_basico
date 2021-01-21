# -*- coding: utf-8 -*-

from odoo import models, fields


class suceso(models.Model):
    _name = 'odoo_basico.suceso'
    _description = 'Proba de vista tree en modo edicion'

    name = fields.Char(string = 'Suceso', required = True, size = 20)
    descripcion = fields.Text(string = 'A descripcion do suceso')
    nivel = fields.Selection([('Alto','Alto'),('Medio','Medio'),('Baixo','Baixo')], string = "Nivel")
    data_hora = fields.Datetime(string = "Data e hora")