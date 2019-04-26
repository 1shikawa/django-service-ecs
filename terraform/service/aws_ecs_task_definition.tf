resource "aws_ecs_task_definition" "django-service" {
  family                = "django-service"
  container_definitions = "${data.template_file.service_container_definition.rendered}"

  task_role_arn = "${data.terraform_remote_state.aws_iam.ecs_task_role_arn}"
  network_mode  = "bridge"

  volume {
    name = "static-storage"

    docker_volume_configuration {
      scope = "shared"
      autoprovision = true
    }
  }
}

resource "aws_ecs_task_definition" "django-migrate" {
  family                = "django-migrate"
  container_definitions = "${data.template_file.migrate_container_definition.rendered}"

  task_role_arn = "${data.terraform_remote_state.aws_iam.ecs_task_role_arn}"
  network_mode  = "bridge"
}
