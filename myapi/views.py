# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .models import Students2
from .serializers import StudentsSerializer

class StudentRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = StudentsSerializer
	def get_queryset(self):
		return Students2.objects.all()

	def perform_create(self, serializers):
		serializer.save(pk=self.request.pk)

class StudentCView(generics.ListCreateAPIView):
	lookup_field = 'pk'
	serializer_class = StudentsSerializer
	def get_queryset(self):
		return Students2.objects.all()
# Create your views here.
