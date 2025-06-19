from django.core.management import BaseCommand

from study.models import Course
from users.models import CustomUser, Payment


class Command(BaseCommand):
    """Команда для создания оплаты"""

    def handle(self, *args, **options):
        user = CustomUser.objects.get(email="admin@gmail.com")
        course = Course.objects.get(title="Python")

        payment = Payment.objects.create(
            user=user, course=course, amount="20000", method="TRANSFER"
        )
        payment.save()
