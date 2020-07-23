from .models import Player
from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser
from .serializers import PlayerSerializer

# player Serializer


class PlayerViewSet(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    queryset = Player.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.Player.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
