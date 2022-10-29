from sqlite3 import OperationalError
from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
  def handle(self, *args, **options):
    self.stdout.write("Waiting for database...")
    conn = None

    while not conn:
      try:
        conn = connections['default']
      except OperationalError:
        self.stdout("Database unavailable, waiting for 1 second...")
        time.sleep(1)

    self.stdout.write(self.style.SUCCESS("Database available"))