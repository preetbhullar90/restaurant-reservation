
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import registerpage, loginpage, logoutuser
from reservation.views import reserve_table, create_order, update_reservations
from reservation.views import delete_reservations, customer_table


class TestReservationUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url = reverse('reservation:register')
        self.assertEquals(resolve(url).func, registerpage)

    def test_loginPage_url_is_resolved(self):
        url = reverse('reservation:login')
        self.assertEquals(resolve(url).func, loginpage)

    def test_logoutUser_url_is_resolved(self):
        url = reverse('reservation:logout')
        self.assertEquals(resolve(url).func, logoutuser)

    def test_reserve_table_url_is_resolved(self):
        url = reverse('reservation:reserve_table')
        self.assertEquals(resolve(url).func, reserve_table)

    def test_create_order_url_is_resolved(self):
        url = reverse('reservation:create_order')
        self.assertEquals(resolve(url).func, create_order)

    def test_update_reservation_url_is_resolved(self):
        url = reverse('reservation:update_reservations', args=['some-slug'])
        self.assertEquals(resolve(url).func, update_reservations)

    def test_delete_reservations_url_is_resolved(self):
        url = reverse('reservation:delete_reservations', args=['some-slug'])
        self.assertEquals(resolve(url).func, delete_reservations)

    def test_customer_table_url_is_resolved(self):
        url = reverse('reservation:customer_table', args=['some-slug'])
        self.assertEquals(resolve(url).func, customer_table)
