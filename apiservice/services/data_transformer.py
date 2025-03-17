from apiservice.clients.re3data_client import Re3DataClient
from apiservice.exceptions import PageOutOfRangeException, InvalidPageSizeException
from apiservice.models import Repository


class DataTransformer:
    @classmethod
    def transform_repository_data(cls, repositories_data):
        for repository_data in repositories_data:
            re3repository_data = Re3DataClient.get_repository_data((repository_data["id"]))

            repository_data["last_update"] = cls.get_last_update(re3repository_data)
            repository_data["api_url"] = cls.get_api_url(re3repository_data)
            repository_data.pop("link", None)
        return repositories_data

    @classmethod
    def get_api_url(cls, repository_data):
        api_url = None
        re3api = repository_data["r3d:api"]
        # when there is only one api type provided it returns a dict, otherwise list of dicts
        # imo it would be better if it had always the same structure
        if isinstance(re3api, dict):
            if re3api["@apiType"] != "OAI-PMH":
                raise Exception("Change for custom exept - oai-pmh not supported")
            return re3api["#text"]

        for api in repository_data["r3d:api"]:
            if api["@apiType"] == "OAI-PMH":
                api_url = api["#text"]
                break

        if not api_url:
            raise Exception("Change for custom exept - oai-pmh not supported")

        # TODO some supposed OAI-PMH are not OAI-PMH apis XD -> check if said OAI-PMH is correct

        return api_url

    @classmethod
    def get_last_update(cls, repository_data):
        return repository_data["r3d:lastUpdate"]

    @classmethod
    def get_repositories_response_json(cls, repositories, page_size, requested_page):
        if page_size <= 0:
            raise InvalidPageSizeException(page_size)

        records_count = len(repositories)
        pages_count = records_count // page_size + 1 if records_count else 0

        if pages_count < requested_page or not requested_page:
            raise PageOutOfRangeException(requested_page, pages_count)

        records_start = (requested_page - 1) * page_size
        records_end = requested_page * page_size if requested_page != pages_count else records_count

        requested_records = [cls.serialize_repository(rep) for rep in repositories[records_start:records_end]]

        return {
            "pages_count": pages_count,
            "current_page": requested_page,
            "records_count": records_count,
            "repositories": requested_records,
        }

    @classmethod
    def serialize_repository(cls, repository: Repository):
        return {"name": repository.name, "id": repository.id, "doi": repository.doi}
