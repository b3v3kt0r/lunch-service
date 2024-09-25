from rest_framework import versioning


class HeaderVersioning(versioning.BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        return request.headers.get("X-API-Version", "2.0")
