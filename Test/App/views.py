# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from App.serializers import WordSerializer
from App.models import WordFrequency
from rest_framework import generics, filters, permissions, viewsets
from App.decorators import validate_request_data



class WordViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    #queryset = WordFrequency.objects.all().order_by('word')
    #serializer_class = WordSerializer
    
    search_fields = ['word']
    filter_backends = (filters.SearchFilter,)
    queryset = WordFrequency.objects.all()
    serializer_class = WordSerializer


class WordCreateSongsView(generics.ListCreateAPIView):
    """
    GET words/
    POST words/
    """
    queryset = WordFrequency.objects.all()
    serializer_class = WordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_word = WordsFrequency.objects.create(
            word=request.data["word"],
            frequency=request.data["frequency"]
        )
        return Response(
            data=WordSerializer(a_word).data,
            status=status.HTTP_201_CREATED
        )


class WordsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET words/:word/
    PUT words/:word/
    DELETE words/:word/
    """
    queryset = WordFrequency.objects.all()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_word = self.queryset.get(word=kwargs["word"])
            return Response(WordSerializer(a_word).data)
        except WordFrequency.DoesNotExist:
            return Response(
                data={
                    "message": "Word with name: {} does not exist".format(kwargs["word"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_word = self.queryset.get(pk=kwargs["pk"])
            serializer = WordSerializer()
            updated_word = serializer.update(a_word, request.data)
            return Response(WordSerializer(updated_song).data)
        except WordsFrequency.DoesNotExist:
            return Response(
                data={
                    "message": "Word with name: {} does not exist".format(kwargs["word"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_word = self.queryset.get(word=kwargs["word"])
            a_word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WordFrequency.DoesNotExist:
            return Response(
                data={
                    "message": "Word with name: {} does not exist".format(kwargs["word"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
