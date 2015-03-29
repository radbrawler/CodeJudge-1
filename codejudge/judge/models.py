from django.db import models

# Create your models here.

class Hacker(models.Model):
	hackerName = models.CharField(max_length=200, unique=True, null=False)
	email = models.EmailField(max_length=254, unique=True, null=False)
	password = models.CharField(max_length=200)
	collegeName = models.CharField(max_length=200)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='avatar')

class Contest(models.Model):
	contestName = models.CharField(max_length=200, unique=True, null=False)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()

class Problem(models.Model):
	contest = models.ForeignKey(Contest)
	problemSetter = models.CharField(max_length=200)
	problemTitle = models.CharField(max_length=200)
	problemStatement = models.TextField()
	testInput = models.FileField(upload_to='testInput')
	testOutput = models.FileField(upload_to='testOutput')
	points = models.PositiveSmallIntegerField()
	timeLimit = models.PositiveSmallIntegerField()
	languagesAllowed = models.CommaSeparatedIntegerField(max_length=200)
	solvedBy = models.PositiveSmallIntegerField(default=0)

class Language(models.Model):
	language = models.CharField(max_length=200)

class Solution(models.Model):
	hacker = models.ForeignKey(Hacker)
	contest = models.ForeignKey(Contest)
	problem = models.ForeignKey(Problem)
	points = models.PositiveSmallIntegerField()
	solution = models.TextField()
	attempts = models.PositiveSmallIntegerField()
	language = models.ForeignKey(Language)
	time = models.DecimalField(max_digits=2, decimal_places=2)

class Comments(models.Model):
	commentText = models.TextField()
	hacker = models.ForeignKey(Hacker)
	contest = models.ForeignKey(Contest)
	problem = models.ForeignKey(Problem)
		
