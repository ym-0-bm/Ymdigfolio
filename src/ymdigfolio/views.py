from django.shortcuts import render
from portfolio.models import Band
from portfolio.forms import BandForm
from portfolio.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect  # ajoutez cet import


def band_list(request):
    bands = Band.objects.all()
    return render(request, "portfolio/band_list.html", {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request, "portfolio/band_detail.html", {'band_id': band_id, 'band': band})


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Portfolio Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['muhamadyesufu2000@gmail.com'],
            )
            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
            return redirect('contact')  # ajoutez cette instruction de retour

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                  'portfolio/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer,
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'portfolio/band_create.html',
                  {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)  # on a pré-remplir le formulaire avec un groupe existant
    return render(request,
                  'portfolio/band_update.html',
                  {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                  'portfolio/band_delete.html',
                  {'band': band})
