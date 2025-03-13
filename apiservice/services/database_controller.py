from apiservice.models import Repository


class DatabaseController:
    @staticmethod
    def save_repository(repository):
        record = Repository(**repository)
        record.save()
