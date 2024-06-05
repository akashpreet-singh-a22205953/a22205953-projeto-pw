from curso.models import Curso,disciplina,projeto
import json

Curso.objects.all().delete()
disciplina.objects.all().delete()
projeto.objects.all().delete()

with open('curso/json/competencias.json') as f:
    data = json.load(f)
with open('curso/json/reasons.json') as f:
    reasons_data = json.load(f)

reasons_texts = []
apresentacao_text = []
competencias_text = []

for item in reasons_data:
    # Append each "reason" text to the list
    reasons_texts.append(item['reason'])

for item in data:
    apresentacao_text = item['descricao']
    competencias_text = item['competencias']


Curso.objects.create(apresentacao=apresentacao_text,objectivos=reasons_texts ,competencias =competencias_text)




SEMESTER_MAPPING = {
    "1º Semestre": 1,
    "2º Semestre": 2,
    "Anual": 3
}

with open('curso/json/cadeiras.json') as f:
    data = json.load(f)

    for item in data:
        semester_code = item['semester']
        # Get the semester number from the mapping, defaulting to 0 if not found
        semester = SEMESTER_MAPPING.get(semester_code, 0)

        disciplina.objects.create(
            nome=item['curricularUnitName'],
            ano=item['curricularYear'],
            semestre=semester,
            ects=item['ects'],
            curricular_IUnit_Readable_Code=item['curricularIUnitReadableCode']
        )




with open('curso/json/projetos.json') as f:
    data = json.load(f)

    for item in data:
        projetos = projeto.objects.create(
            projeto=item['projeto'],
            disciplina=item['disciplina'],
            ano=item['ano'],
            semestre=item['semestre'],
            descricao=item['descricao'],
            conceitos_aplicados=item['conceitos_aplicados'],
            link_video=item['link_video'],
            link_gitHub=item['link_gitHub']
        )
        projetos.save()