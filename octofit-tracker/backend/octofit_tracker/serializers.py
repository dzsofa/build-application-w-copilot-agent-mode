from rest_framework import serializers
from .mongo_models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    team = serializers.CharField()

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    difficulty = serializers.CharField(max_length=50)

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    score = serializers.IntegerField()
