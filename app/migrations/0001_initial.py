# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'app_company', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'app', ['Company'])

        # Adding model 'Stock'
        db.create_table(u'app_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Company'])),
            ('Date', self.gf('django.db.models.fields.DateField')()),
            ('Open', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('High', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Low', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Close', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Adj_Close', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Symbol', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['Stock'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'app_company')

        # Deleting model 'Stock'
        db.delete_table(u'app_stock')


    models = {
        u'app.company': {
            'Meta': {'object_name': 'Company'},
            'created': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'})
        },
        u'app.stock': {
            'Adj_Close': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Close': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.DateField', [], {}),
            'High': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Low': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Stock'},
            'Open': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Symbol': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']