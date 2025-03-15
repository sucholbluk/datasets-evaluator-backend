from apiservice.models import Repository


class DatabaseController:
    @staticmethod
    def save_repository(repository_data):
        record = Repository(**repository_data)
        record.save()

    @classmethod
    def update_repositories(cls, repositories_data):
        saved_repository_identifiers = set(Repository.objects.values_list("id"))
        for repository_data in repositories_data:
            if repository_data["id"] in saved_repository_identifiers:
                saved_repository_identifiers.discard(repository_data["id"])

            Repository.objects.update_or_create(id=repository_data, defaults=repository_data)

        Repository.objects.filter(id__in=saved_repository_identifiers).delete()
