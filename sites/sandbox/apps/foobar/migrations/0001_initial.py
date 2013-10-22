# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyNewModel'
        db.create_table(u'foobar_mynewmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('bar', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'foobar', ['MyNewModel'])


    def backwards(self, orm):
        # Deleting model 'MyNewModel'
        db.delete_table(u'foobar_mynewmodel')


    models = {
        u'foobar.mynewmodel': {
            'Meta': {'object_name': 'MyNewModel'},
            'bar': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['foobar']