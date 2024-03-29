import unittest

from entity.Vehicle import Vehicle
from serviceanddatabase.VehicleService import VehicleService
from serviceanddatabase.DatabaseConnect import DatabaseConnect


class TestGetAvailableVehicles(unittest.TestCase):
    def setUp(self):
        db_context = DatabaseConnect(database="carconnect")
        db_context.connect()
        self.vehicle_service = VehicleService(db_context)

    def test_get_available_vehicles(self):
        test_vehicles = [
            {
                'Model': 'Subaru BRZ',
                'Make': 'Subaru',
                'Year': 2022,
                'Color': 'Dark Gray',
                'RegistrationNumber': 'JP202212',
                'Availability': 'y',
                'DailyRate': 700.00,
            },
            {
                'Model': 'Mitsubishi Eclipse Cross',
                'Make': 'Mitsubishi',
                'Year': 2023,
                'Color': 'Deep Blue',
                'RegistrationNumber': 'JP202312',
                'Availability': 'n',
                'DailyRate': 750.00,
            },
            {
                'Model': 'Honda HR-V',
                'Make': 'Honda',
                'Year': 2021,
                'Color': 'Burgundy',
                'RegistrationNumber': 'JP202112',
                'Availability': 'y',
                'DailyRate': 720.00,
            },
        ]

        for vehicle_data in test_vehicles:
            self.vehicle_service.add_vehicle(vehicle_data)

        available_vehicles_result = self.vehicle_service.get_available_vehicles()
        available_vehicles = [Vehicle(*available_vehicle_result) for available_vehicle_result in available_vehicles_result]
        for vehicle in available_vehicles:
            self.assertEqual(vehicle.availability,  1)


if __name__ == '__main__':
    unittest.main()