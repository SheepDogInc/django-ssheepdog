# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'NamedApplicationKey'
        db.create_table('ssheepdog_namedapplicationkey', (
            ('application_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssheepdog.ApplicationKey'])),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ssheepdog', ['NamedApplicationKey'])

        # Adding field 'ApplicationKey.is_named'
        db.add_column('ssheepdog_applicationkey', 'is_named', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'NamedApplicationKey'
        db.delete_table('ssheepdog_namedapplicationkey')

        # Deleting field 'ApplicationKey.is_named'
        db.delete_column('ssheepdog_applicationkey', 'is_named')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ssheepdog.applicationkey': {
            'Meta': {'object_name': 'ApplicationKey'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_named': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'private_key': ('django.db.models.fields.TextField', [], {}),
            'public_key': ('ssheepdog.fields.PublicKeyField', [], {})
        },
        'ssheepdog.client': {
            'Meta': {'object_name': 'Client'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'ssheepdog.login': {
            'Meta': {'object_name': 'Login'},
            'additional_public_keys': ('ssheepdog.fields.PublicKeyField', [], {'blank': 'True'}),
            'application_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.ApplicationKey']", 'null': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.Client']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.Machine']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'ssheepdog.loginlog': {
            'Meta': {'object_name': 'LoginLog'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.Login']", 'null': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'stderr': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'stdout': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'ssheepdog.machine': {
            'Meta': {'object_name': 'Machine'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.Client']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_down': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'manual': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '22'})
        },
        'ssheepdog.namedapplicationkey': {
            'Meta': {'object_name': 'NamedApplicationKey'},
            'application_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ssheepdog.ApplicationKey']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'ssheepdog.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'ssh_key': ('ssheepdog.fields.PublicKeyField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'_profile_cache'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['ssheepdog']
