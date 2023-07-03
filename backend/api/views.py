from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person, Project
from .serializers import (PersonWithProjectsPreviewSerializer,
                          PersonQueryParamSerializer,
                          ProjectQueryParamSerializer,
                          ProjectWithPersonPreviewSerializer)


class PersonView(APIView):
    def get(self, request: Request, *args, **kwargs):
        if not request.query_params.get('employment_type'):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'EMPLOYMENT_TYPE_IS_NEEDED'}
            )

        serializer = PersonQueryParamSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'EMPLOYMENT_TYPE_IS_INVALID'}
            )

        persons = Person.objects.filter(employment_type=request.query_params.get('employment_type'))
        if not persons:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'message': 'NO_PERSONS_FOUND'}
            )

        return Response(
            status=status.HTTP_200_OK,
            data={'items': PersonWithProjectsPreviewSerializer(persons, many=True).data}
        )


class ProjectView(APIView):
    def get(self, request: Request, *args, **kwargs):
        if not request.query_params.get('project_type'):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'PROJECT_TYPE_IS_NEEDED'}
            )

        serializer = ProjectQueryParamSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'PROJECT_TYPE_IS_INVALID'}
            )

        projects = Project.objects.filter(project_type=request.query_params.get('project_type'))
        if not projects:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'message': 'NO_PROJECTS_FOUND'}
            )

        return Response(
            status=status.HTTP_200_OK,
            data={'items': ProjectWithPersonPreviewSerializer(projects, many=True).data}
        )


class PersonDetailsView(APIView):
    def get(self, request: Request, *args, **kwargs):
        person = Person.objects.filter(id=kwargs['person_id']).first()
        if not person:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'message': 'NO_PERSON_FOUND'}
            )

        return Response(
            status=status.HTTP_200_OK,
            data={'items': PersonWithProjectsPreviewSerializer(person).data}
        )
      
      
class ProjectDetailsView(APIView):
    def get(self, request: Request, *args, **kwargs):
        project = Project.objects.filter(id=kwargs['project_id']).first()
        if not project:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'message': 'NO_PROJECT_FOUND'}

            )

        return Response(
            status=status.HTTP_200_OK,
            data={'items': ProjectWithPersonPreviewSerializer(project).data}
        )
