from rest_framework import viewsets, status
from rest_framework.response import Response
from .mongo_models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = Team(**serializer.validated_data).save()
            return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            team = Team.objects.get(id=serializer.validated_data['team'])
            user = User(name=serializer.validated_data['name'], email=serializer.validated_data['email'], team=team).save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=serializer.validated_data['user'])
            activity = Activity(user=user, type=serializer.validated_data['type'], duration=serializer.validated_data['duration'], date=serializer.validated_data['date']).save()
            return Response(ActivitySerializer(activity).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            workout = Workout(**serializer.validated_data).save()
            return Response(WorkoutSerializer(workout).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=serializer.validated_data['user'])
            lb = Leaderboard(user=user, score=serializer.validated_data['score']).save()
            return Response(LeaderboardSerializer(lb).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
