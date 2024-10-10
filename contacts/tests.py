from django.test import TestCase
from django.urls import reverse
from .models import Contact


class ContactTests(TestCase):
    def setUp(self):
        # Setup einen Beispielkontakt
        self.contact = Contact.objects.create(name = 'Max Mustermann', email = 'max@example.com',phone = '1234567890')

    def test_contact_list_view(self):
        # Testet, ob die Kontaktliste korrekt funktioniert
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.contact.name)  # Überprüft, ob der Name des Kontakts auf der Seite erscheint
        self.assertTemplateUsed(response, 'contacts/contact_list.html')


# Testet, ob der Detailansicht eines Kontakts korrekt funktioniert
    def test_contact_detail_view(self):        
        response = self.client.get(reverse('contact_detail', args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.contact.name)  # Überprüft, ob der Kontaktname in der Detailansicht angezeigt wird
        self.assertTemplateUsed(response, 'contacts/contact_detail.html')


# Testet, ob das Erstellen eines neuen Kontakts funktioniert
    def test_contact_create_view(self):        
        response = self.client.post(reverse('contact_create'), {
            'name': 'Hans Meyer',
            'email': 'hans@example.com',
            'phone': '9876543210'
        })
        self.assertEqual(response.status_code, 302)  # Überprüft, ob die Seite nach dem Erstellen weiterleitet
        self.assertEqual(Contact.objects.count(), 2)  # Es sollten jetzt 2 Kontakte in der DB sein


# Testet, ob das Bearbeiten eines Kontakts funktioniert
    def test_contact_edit_view(self):
        response = self.client.post(reverse('contact_edit', args=[self.contact.id]), {
            'name': 'Max Mustermann Geändert',
            'email': 'max@example.com',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 302)  # Überprüft, ob die Seite nach dem Bearbeiten weiterleitet
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, 'Max Mustermann Geändert')  # Überprüft, ob der Name geändert wurde


# Testet, ob das Löschen eines Kontakts funktioniert
    def test_contact_delete_view(self):        
        response = self.client.post(reverse('delete_contact', args=[self.contact.id]))
        self.assertEqual(response.status_code, 302)  # Überprüft, ob die Seite nach dem Löschen weiterleitet
        self.assertEqual(Contact.objects.count(), 0)  # Es sollte kein Kontakt mehr in der DB sein
