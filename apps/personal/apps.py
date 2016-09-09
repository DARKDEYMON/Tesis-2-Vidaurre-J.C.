from django.apps import AppConfig

class PersonalConfig(AppConfig):
    name = 'personal'
        
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def create_perms():
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_personal',
			name='Ver personal',
			content_type=content_type,
		)
	except:
		print ("1 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_seguimiento',
			name='Ver seguimineto',
			content_type=content_type,
		)
	except:
		print ("2 ya aderido")
	try:
		content_type = ContentType.objects.get_for_model(User)
		permission = Permission.objects.create(
			codename='view_almacen',
			name='Ver almacen',
			content_type=content_type,
		)
	except:
		print ("3 ya aderido")
create_perms()