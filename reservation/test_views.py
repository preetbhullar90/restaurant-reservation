from django.test import TestCase, Client
from django.urls import reverse
from reservation.models import Customer, Table, Reservation
from django.contrib.auth.models import User


class TestReservationsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.client.login(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.reservations_url = reverse('reservation:reserve_table')
        self.register_url = reverse('reservation:register')
        self.login_url = reverse('reservation:login')
        self.view_reservations_url = reverse(
            'reservation:customer_table', args=[1])
        self.create_customer_details_url = reverse('reservation:create_order')
        self.update_reservation1_url = reverse(
            'reservation:update_reservations', args=[2])
        self.delete_reservation1_url = reverse(
            'reservation:delete_reservations', args=[2])

        self.table = Table.objects.create(
            table_name='Table 5',
            max_no_people=4
        )

        self.customer = Customer.objects.create(
            name='Project Test',
            email='project.test@test.com',
            phone='+447980987654',
            owner='1'
        )

        self.reservation1 = Reservation.objects.create(
            user=self.user,
            customer=self.customer,
            table=self.table,
            persons=1,
            date='2022-05-20',
            time='12:00',
            status='pending'
        )

        self.reservation2 = Reservation.objects.create(
            user=self.user,
            customer=self.customer,
            table=self.table,
            persons=1,
            date='2022-05-20',
            time='12:00',
            status='pending'
        )

    def test_reservation_GET(self):
        response = self.client.get(self.reservations_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation/reservation.html')

    def test_view_reservation_GET(self):
        response = self.client.get(self.view_reservations_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation/view_reservation.html')

    def test_create_reservation_GET(self):
        response = self.client.get(self.create_customer_details_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'Reservation/create_reservation.html')

    def test_update_reservation_GET(self):
        response = self.client.get(self.update_reservation1_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'Reservation/update_reservation.html')

    def test_delete_reservation_GET(self):
        response = self.client.get(self.delete_reservation1_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'Reservation/delete_reservation.html')

    def test_register_form_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation/register.html')

    def test_login_form_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation/login.html')

    def test_reservation_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.reservations_url)

        self.assertEquals(response.status_code, 302)

    def test_view_reservation_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.view_reservations_url)
        self.assertEquals(response.status_code, 302)

    def test_delete_reservation_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.delete_reservation1_url)
        self.assertEquals(response.status_code, 302)

    def test_edit_reservation_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.create_customer_details_url)
        self.assertEquals(response.status_code, 302)

    def test_update_reservation_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.update_reservation1_url)
        self.assertEquals(response.status_code, 302)

    def test_register_form_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_login_form_GET_unathorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_reservation_POST_adds_new_customer_and_reservation(self):
        table = self.table
        customer = Customer.objects.create(
            name='Project Test123',
            email='project.test123@test.com',
            phone='+447980987654',
            owner='2'
        )

        reservation = Reservation.objects.create(
            user=self.user,
            customer=customer,
            table=table,
            persons=1,
            date='2022-03-29',
            time='12:00',
            status='pending'
        )

        response = self.client.post(self.reservations_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Reservation.objects.all()), 3)
        self.assertEquals(len(Customer.objects.all()), 2)

    def test_reservation_POST_does_not_add_customer_that_exists(self):
        table = self.table
        customer = self.customer
        reservation = Reservation.objects.create(
            user=self.user,
            customer=self.customer,
            table=self.table,
            persons=1,
            date='2022-05-20',
            time='12:00',
            status='pending'
        )
        response = self.client.post(self.reservations_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Reservation.objects.all()), 3)
        self.assertEquals(len(Customer.objects.all()), 1)

    def test_edit_reservation_POST_updates_model(self):
        reservation = self.reservation1
        reservation.date = '2022-04-01'
        response = self.client.post(self.update_reservation1_url)
        self.assertEquals(self.reservation1.date, '2022-04-01')

    def test_delete_reservation_POST_updates_model(self):
        reservation = self.reservation2
        response = self.client.post(self.delete_reservation1_url)
        self.assertEquals(len(Reservation.objects.all()), 1)
        self.assertNotIn(self.reservation2, Reservation.objects.all())
