resource "aws_cloudwatch_log_group" "django-service" {
  name = "django-service"
}

resource "aws_cloudwatch_log_group" "nginx" {
  name = "nginx"
}
