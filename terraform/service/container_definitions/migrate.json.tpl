[
  {
    "name": "django-service",
    "image": "090442518795.dkr.ecr.ap-northeast-1.amazonaws.com/django:latest",
    "cpu": 200,
    "memory": null,
    "memoryReservation": 600,
    "essential": true,
    "portMappings": [
      {
        "hostPort": 0,
        "protocol": "tcp",
        "containerPort": 8000
      }
    ],
    "command": ["bash","-c","python manage.py makemigrations && python manage.py migrate"],
    "environment": [
      {
        "name": "VERSION_INFO",
        "value": ""
      },
      {
        "name": "BUILD_DATE",
        "value": ""
      }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "django-service",
        "awslogs-region": "ap-northeast-1",
        "awslogs-stream-prefix": "migration"
      }
    }
  }
]
