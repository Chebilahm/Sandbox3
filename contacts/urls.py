
from django.urls import path
from . import views

urlpatterns = [
    # path('', home, name='home'),  führt zur Startseite, dafür muss eine Datei home.html im Template erstellt werden
    path('', views.contact_list, name='contact_list'),  # die Liste aller Kontakte
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),  # Details eines Kontakts
    path('contacts/create/', views.contact_create, name='contact_create'),  # ein neuen Kontakt erstellen
    path('contacts/<int:contact_id>/edit/', views.contact_edit, name='contact_edit'),  # Kontakt bearbeiten
    path('list/', views.contact_list, name='contact_list'),  # hier die Liste der Kontakte
    path('contacts/', views.contact_list, name='contact_list'),  # hier die Liste der Kontakte
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'), # Kontakt löschen
]
