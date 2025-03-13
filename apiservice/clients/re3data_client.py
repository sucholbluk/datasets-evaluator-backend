import requests
import xmltodict


class Re3DataClient:
    REPOSITORIES_URL = "https://www.re3data.org/api/beta/repositories"

    @classmethod
    def get_repositories(cls, query_params={"apis[]": "OAI-PMH"}):
        response = requests.get(cls.REPOSITORIES_URL, query_params)

        if response.status_code != 200:
            raise Exception("Change for custom Unexpected API Exception")

        return xmltodict.parse(response.text)["list"]["repository"]
