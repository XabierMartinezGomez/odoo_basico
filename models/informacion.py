# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Tipos de datos basicos'

    name = fields.Char(string = 'Titulo', required = True, size = 20)
    descripcion = fields.Text(string = 'A descripcion')
    autorizado = fields.Boolean(string = "¿Esta autorizado", default = True)
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string = "Sexo")
    alto_en_cms = fields.Integer(string = 'Alto en Cms.')
    longo_en_cms = fields.Integer(string = 'Longo en Cms.')
    ancho_en_cms = fields.Integer(string = 'Ancho en Cms.')
    volume = fields.Float(compute = "_volume", store=True)
    peso = fields.Float(string = "Peso",default = 2.7,digits = (6,2))
    densidade = fields.Float(compute = "_densidade=", store = True)

    @api.depends('alto_en_cms','longo_en_cms','ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)

    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = (float(rexistro.peso) / float(rexistro.volume)) * 100
            else:
                rexistro.densidade = 0