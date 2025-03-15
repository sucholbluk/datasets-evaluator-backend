import requests
import xmltodict


class Re3DataClient:
    REPOSITORIES_URL = "https://www.re3data.org/api/beta/repositories"
    REPOSITORY_BASE_URL = "https://www.re3data.org/api/v1/repository/"

    @classmethod
    def get_repositories(cls, query_params={"apis[]": "OAI-PMH"}):
        response = requests.get(cls.REPOSITORIES_URL, query_params)

        if response.status_code != 200:
            raise Exception("Change for custom Unexpected API response Exception")

        return xmltodict.parse(response.text)["list"]["repository"]

    @classmethod
    def get_repository_data(cls, id):
        response = requests.get(cls.REPOSITORY_BASE_URL + id)

        if response.status_code != 200:
            raise Exception("Change for custom Unexpected API response Exception")

        return xmltodict.parse(response.text)["r3d:re3data"]["r3d:repository"]
