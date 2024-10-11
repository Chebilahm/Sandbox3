
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
# from django import re

# Liste alle Kontakte
def contact_list(request):
    contacts = Contact.objects.all().order_by('name')  # Liste der Kontakte nach namen sortiert
    contact_names = []

# die for-Schleife wird hier verwendet um die Liste der Kontakte durchzulaufen
# hier werden die Namen in der Liste conatct_names gespeichert
    for contact in contacts: 
        contact_names.append(contact.name)

    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# Eine while-Schleife Beispiel: es läuft durch die ersten 5 Kontakte und fgt sie zur Liste conatct_names zu
# und dann gibt die ersten 5 Kontakte aus

def contact_list(request):
    contacts = Contact.objects.all().order_by('name')  # Liste der Kontakte nach Namen sortiert
    contact_names = []

    # Begrenze die Anzahl der angezeigten Kontakte auf 5
    i = 0
    limit = 10
    while i < limit and i < len(contacts):
        contact_names.append(contacts[i].name)
        i += 1

    return render(request, 'contacts/contact_list.html', {'contacts': contacts[:limit], 'contact_names': contact_names})


# Einen Kontakt nach ID anzeigen
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

# Neuen Kontakt erstellen
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # speichert den neuen Kontakt
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_create.html', {'form': form})

# Kontakt bearbeiten
def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  # speichert die Änderungen
            return redirect('contact_detail', contact_id=contact_id)  # zurück zu contact_detail
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_edit.html', {'form': form, 'contact': contact})


# Kontakt löschen
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)  # Versucht, den Kontakt zu finden
    except Contact.DoesNotExist:
        # Wenn der Kontakt nicht existiert wird der Benutzer zurück zur Kontaktliste geleitet
        return redirect('contact_list')

    if request.method == "POST":
        contact.delete()  # Löscht den Kontakt, wenn der Benutzer die Löschung bestätigt hat
        return redirect('contact_list')  # Leitet zur Kontaktliste zurück

    # Zeigt die Bestätigungsseite an, wenn der Benutzer die Seite per GET-Request aufruft
    return render(request, 'contacts/delete_contact.html', {'contact': contact})
