from Band.models import Band,Music
import json

Band.objects.all().delete()
Music.objects.all().delete()


with open('Band/json/bands.json') as f:
    bandas = json.load(f)

    for band_data in bandas:

        Band.objects.create(
            bandName=band_data['nome'],
            dateOfAppearance=band_data['ano_criacao'],
            nationality=band_data['nacionalidade']
        )

with open('Band/json/music.json') as f:
        music_data = json.load(f)
        for data in music_data:
            Music.objects.create(
                titulo=data['title'],
                ano_do_lancamento=data['release_year'],
                duration = data['duration']
            )
