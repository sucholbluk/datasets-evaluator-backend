from django.views import View
from django.http import JsonResponse, HttpRequest
from apiservice.services.database_controller import DatabaseController
from apiservice.services.data_transformer import DataTransformer
from apiservice.exceptions import PageOutOfRangeException, InvalidPageSizeException


class GetRepositoriesView(View):
    def get(self, request: HttpRequest):
        page_size, requested_page, searched_string = (
            request.GET.get("page_size"),
            request.GET.get("requested_page"),
            request.GET.get("searched_string"),
        )

        if all((page_size is None, requested_page is None)):
            return JsonResponse(status=400, data={"message": "Required page_size and searched_string params"})

        searched_string = searched_string if searched_string else ""

        try:
            page_size, requested_page = int(page_size), int(requested_page)
            all_repositories = DatabaseController.get_repositories_by_name(searched_string)
            response_data = DataTransformer.get_repositories_response_json(all_repositories, page_size, requested_page)
            response = JsonResponse(status=200, data=response_data)
        except PageOutOfRangeException as e:
            response = JsonResponse(status=400, data={"message": e.message})
        except InvalidPageSizeException as e:
            response = JsonResponse(status=400, data={"message": e.message})
        except ValueError:
            response = JsonResponse(status=400, data={"message": "page_size and requested_page must be integers"})

        return response
