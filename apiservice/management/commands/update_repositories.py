from django.core.management.base import BaseCommand
from apiservice.clients.re3data_client import Re3DataClient
from apiservice.services.data_transformer import DataTransformer
from apiservice.services.database_controller import DatabaseController


class Command(BaseCommand):
    help = "Update repository data for repositories in re3data"

    def handle(self, *args, **options):
        self.stdout.write("Sending HTTP request to re3data API")
        api_response = Re3DataClient.get_repositories()

        self.stdout.write("Transforming data to match db model")
        transformed_repositories_data = DataTransformer.transform_repository_data(api_response)
        self.stdout.write("Updating records in database")
        DatabaseController.update_repositories(transformed_repositories_data)
        self.stdout.write("All done")
