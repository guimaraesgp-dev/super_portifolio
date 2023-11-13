from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class NoCretifiedInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name"]


class CertifiedInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NoCretifiedInstitutionSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new = CertifyingInstitution.objects.create(**validated_data)
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=new,
                **certificate_data,
            )
        return new
