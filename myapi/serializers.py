from rest_framework import serializers
from .models import Students2

class StudentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students2
		fields = [
			'pk', 
			'fname', 
			'lname', 
			'email', 
			'phone'
		]
		read_only_field = ['pk']

	def validate_email(self, value):
		qs = Students2.objects.filter(email__iexact=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError("The Email must be unique")
		return value