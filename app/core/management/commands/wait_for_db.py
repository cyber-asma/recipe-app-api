"""
djando command to wait for database to be available
"""

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError
import time
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = 'Waits for the database to be available'

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
