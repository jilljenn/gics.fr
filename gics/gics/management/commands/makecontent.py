from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from gics.models import Lecture, School, Session
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    args = ''
    help = 'Creates dummy content'
    def handle(self, *args, **options):
        for _ in range(5):
            for school in School.objects.all():
                Session(lecture=random.choice(Lecture.objects.all()), school=school, date=timezone.now() + timedelta(days=random.randint(1, 10)), speaker=random.choice(User.objects.all())).save()
