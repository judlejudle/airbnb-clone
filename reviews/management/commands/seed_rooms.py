from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review


class Command(BaseCommand):
    help = "this command create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
