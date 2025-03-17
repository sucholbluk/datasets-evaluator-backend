from apiservice.models import Repository


class DatabaseController:
    @staticmethod
    def save_repository(repository_data):
        record = Repository(**repository_data)
        record.save()

    @staticmethod
    def update_repositories(repositories_data):
        saved_repository_identifiers = set(Repository.objects.values_list("id"))
        for repository_data in repositories_data:
            if repository_data["id"] in saved_repository_identifiers:
                saved_repository_identifiers.discard(repository_data["id"])

            Repository.objects.update_or_create(id=repository_data, defaults=repository_data)

        Repository.objects.filter(id__in=saved_repository_identifiers).delete()

    @staticmethod
    def get_repository_by_id(repository_id):
        return Repository.objects.get(id=repository_id)

    @staticmethod
    def get_repositories_by_name(name_part):
        return Repository.objects.filter(name__icontains=name_part)
