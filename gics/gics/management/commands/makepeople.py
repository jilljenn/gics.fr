# coding=utf8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from gics.models import Discipline, School, Person

class Command(BaseCommand):
    args = ''
    help = 'Creates people from data/intervenants.csv'
    def handle(self, *args, **options):
        schools = {}
        for school in School.objects.all():
            schools[school.title] = school
        print(schools.keys())
        disciplines = {}
        for discipline in Discipline.objects.all():
            disciplines[discipline.title] = discipline
        school_names = {
            '': 'École inconnue',
            'P6': 'Université Paris VI',
            'P7': 'Université Paris VII',
            'Centrale': 'Centrale Paris',
            'ENSKL': 'ENS Ker Lann',
            'ENS': 'ENS Paris',
            'ENSC': 'ENS Cachan',
            'ENSC, P9': 'ENS Cachan',
            'ENSL': 'ENS Lyon',
            'X': 'École polytechnique'
        }
        discipline_repl = {
            '': '',
            'Info': 'Informatique',
            'bio': 'Biologie',
            'Neurosciences cognitives': 'Neurosciences cognitives',
            'info': 'Informatique',
            'Économie Gestion': 'Éco-gestion',
            'Finance': 'Finance',
            'Bio': 'Biologie',
            'Eco': 'Économie',
            'probas': 'Probabilités',
            'Physique': 'Physique',
            'éco': 'Économie',
            'Chimie': 'Chimie',
            'Maths': 'Mathématiques',
            'finance': 'Finance',
        }
        with open('../data/intervenants.tsv') as f:
            next(f)
            for line in f:
                tokens = line.strip().split('\t')
                comments2 = ''
                if len(tokens) == 8:
                    name, _, _, comments, mail, school_id, discipline_ids, comments2 = tokens
                elif len(tokens) == 7:
                    name, _, _, comments, mail, school_id, discipline_ids = tokens
                elif len(tokens) == 6:
                    name, _, _, comments, mail, school_id = tokens
                else:
                    print('Error with', line)
                    raise BaseException
                school_name = school_names[school_id]
                # print(discipline_ids.split(', '), discipline_names.keys()))
                discipline_names = [discipline_repl[discipline_id] for discipline_id in discipline_ids.split(', ')]
                if school_name in schools:
                    school = schools[school_name]
                else:
                    school = School(title=school_name)
                    school.save()
                    schools[school_name] = school
                person = Person(name=name, comments=comments + '\n' + comments2, mail=mail, school=school)
                person.save()
                for discipline_name in discipline_names:
                    if discipline_name == '':
                        continue
                    if discipline_name in disciplines:
                        discipline = disciplines[discipline_name]
                    else:
                        discipline = Discipline(title=discipline_name)
                        discipline.save()
                        disciplines[discipline_name] = discipline
                    person.majors.add(discipline)
        print(schools.keys())
                # schools.add(school)
                # disciplines.update(discipline.split(', '))
