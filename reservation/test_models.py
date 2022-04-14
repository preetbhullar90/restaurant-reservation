
from django.test import TestCase
from reservation.models import Reservation, Table, Customer


class TestReservationsModels(TestCase):

    def setUp(self):
        self.table = Table(table_name='Table 1', max_no_people=4)
        self.customer = Customer(
            name='Test 123', email='test123@gmail.com',
            phone='12345', owner='1')
        self.reservation = Reservation(
            table=self.table,
            customer=self.customer,
            persons=4, date='2022-01-23',
            time='12:00', status='pending')

    def test_create_table(self):
        self.assertEquals(self.table.table_name, 'Table 1')
        self.assertEquals(self.table.max_no_people, 4)

    def test_create_customer(self):
        self.assertEquals(self.customer.name, 'Test 123')
        self.assertEquals(self.customer.email, 'test123@gmail.com')

    def test_create_reservation(self):
        self.assertEquals(self.reservation.table, self.table)
        self.assertEquals(self.reservation.customer, self.customer)
        self.assertEquals(self.reservation.persons, 4)
        self.assertEquals(self.reservation.date, '2022-01-23')
        self.assertEquals(self.reservation.time, '12:00')
        self.assertEquals(self.reservation.status, 'pending')

    def test_customer_on_delete_cascade_works(self):
        customer = self.customer
        customer.save()

        reservations = len(Reservation.objects.all())

        self.assertEquals(reservations, 0)

    def test_table_on_delete_cascade_works(self):
        table = self.table
        table.save()

        reservations = len(Reservation.objects.all())

        self.assertEquals(reservations, 0)
