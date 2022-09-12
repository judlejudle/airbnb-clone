from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "this command create amenities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid Parking on Premises",
            "Paid Parking off Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)}facilities created"))
