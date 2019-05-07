resource "aws_ecs_service" "django-service" {
  name            = "django-service"
  cluster         = "${aws_ecs_cluster.django-cluster.id}"
  task_definition = "${aws_ecs_task_definition.django-service.arn}"
  desired_count   = 2
  launch_type     = "EC2"

  load_balancer {
    target_group_arn = "${aws_lb_target_group.http.arn}"
    container_name   = "nginx"
    container_port   = "80"
  }
}