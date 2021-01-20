from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddressSerializer
from hello_app.services import address_parser


class AddressEndpoint(APIView):
    def get(self, request: Request) -> Response:
        serializer = AddressSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = address_parser.parse(serializer.validated_data["address"])
        except address_parser.ParseError as e:
            return Response(str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(data)
