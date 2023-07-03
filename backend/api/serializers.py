from rest_framework import serializers
from .models import Person, Project


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PersonPreviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'speciality', 'photo']


class ProjectPreviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'short_description']


class PersonWithProjectsPreviewSerializer(PersonSerializer):

    def to_representation(self, instance: Person):
        representation = super().to_representation(instance)
        representation['projects'] = ProjectPreviewReadSerializer(instance.projects, many=True).data
        return representation


class ProjectWithPersonPreviewSerializer(ProjectSerializer):

    def to_representation(self, instance: Project):
        representation = super().to_representation(instance)
        representation['contributors'] = PersonPreviewReadSerializer(instance.contributors, many=True).data
        return representation


class PersonQueryParamSerializer(serializers.Serializer):
    employment_type = serializers.ChoiceField(choices=Person.EmploymentType.choices)


class ProjectQueryParamSerializer(serializers.Serializer):
    project_type = serializers.ChoiceField(choices=Project.ProjectType.choices)

