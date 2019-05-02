[
  {
    "name": "django-service",
    "image": "090442518795.dkr.ecr.ap-northeast-1.amazonaws.com/django:latest",
    "hostname": "django-service",
    "cpu": 333,
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
    "command": 	["bash","-c","python manage.py collectstatic --noinput && python manage.py custom_createsuperuser --username admin --email admin@example.com --password admin && gunicorn django_service.wsgi -b 0.0.0.0:8000"],
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
    "mountPoints": [
                {
                    "sourceVolume": "static-storage",
                    "containerPath": "/usr/src/app/static",
                    "readOnly": false
                }
            ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "django-service",
        "awslogs-region": "ap-northeast-1",
        "awslogs-stream-prefix": "service"
      }
    }
  },

    {
    "name": "nginx",
    "image": "090442518795.dkr.ecr.ap-northeast-1.amazonaws.com/nginx:latest",
    "hostname": "nginx",
    "cpu": 100,
    "memory": null,
    "memoryReservation": 300,
    "essential": true,
    "portMappings": [
      {
        "hostPort": 0,
        "protocol": "tcp",
        "containerPort": 80
      }
    ],
    "links": ["django-service"],
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
    "mountPoints": [
                {
                    "sourceVolume": "static-storage",
                    "containerPath": "/usr/src/app/static",
                    "readOnly": false
                }
            ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "nginx",
        "awslogs-region": "ap-northeast-1",
        "awslogs-stream-prefix": "nginx"
      }
    }
  }
]