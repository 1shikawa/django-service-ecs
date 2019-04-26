resource "aws_ecr_repository" "django" {
  name = "django"
}

resource "aws_ecr_repository" "nginx" {
  name = "nginx"
}