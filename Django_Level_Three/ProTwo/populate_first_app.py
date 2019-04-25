import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
	for entry in range(N):
		#create fake data
		fake_fn = fakegen.first_name()
		fake_ln = fakegen.last_name()
		fake_email = fakegen.email()
		#create webpage entry
		User.objects.get_or_create(FirstName = fake_fn, LastName = fake_ln, Email = fake_email)

if __name__ == '__main__':
	print("populating script!")
	populate(60)
	print("populating complete!")
