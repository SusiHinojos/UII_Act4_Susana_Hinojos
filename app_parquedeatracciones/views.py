from django.shortcuts import render

# Create your views here.
def index(request):
    atracciones = [
        {
            'nombre': 'Montaña Rusa Gigante',
            'descripcion': 'Una experiencia de adrenalina pura con caídas vertiginosas y giros inesperados.',
            'imagen_url': 'https://example.com/montana_rusa.jpg' # Reemplaza con tu URL de imagen real
        },
        {
            'nombre': 'Carrusel Mágico',
            'descripcion': 'Un clásico atemporal perfecto para toda la familia, con caballos y figuras encantadoras.',
            'imagen_url': 'https://example.com/carrusel.jpg' # Reemplaza con tu URL de imagen real
        },
        {
            'nombre': 'Casa del Terror',
            'descripcion': 'Prepárate para sustos y sorpresas en esta oscura y misteriosa atracción.',
            'imagen_url': 'https://example.com/casa_terror.jpg' # Reemplaza con tu URL de imagen real
        }
    ]

    return render(request, 'index.html', {'atracciones':atracciones})