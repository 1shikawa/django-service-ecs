resource "aws_db_parameter_group" "django-service" {
  name   = "django-service"
  family = "mysql5.7"

  parameter {
    name  = "character_set_database"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_server"
    value = "utf8mb4"
  }

    parameter {
    name  = "character_set_client"
    value = "utf8mb4"
  }

    parameter {
    name  = "character_set_connection"
    value = "utf8mb4"
  }

    parameter {
    name  = "collation_connection"
    value = "utf8mb4_general_ci"
  }

    parameter {
    name  = "collation_server"
    value = "utf8mb4_general_ci"
  }

    parameter {
    name  = "character_set_results"
    value = "utf8mb4"
  }
}


resource "aws_db_option_group" "django-service" {
  name                 = "django-service"
  engine_name          = "mysql"
  major_engine_version = "5.7"

  option {
    option_name = "MARIADB_AUDIT_PLUGIN"
  }
}


resource "aws_db_instance" "django-service" {
  identifier                 = "django-service"
  engine                     = "mysql"
  engine_version             = "5.7.23"
  instance_class             = "db.t3.small"
  allocated_storage          = 20
  storage_type               = "gp2"
  storage_encrypted          = true
  # kms_key_id                 = aws_kms_key.example.arn
  username                   = "mysiteuser"
  password                   = "mysitepass"
  multi_az                   = true
  publicly_accessible        = false
  # backup_window              = "09:10-09:40"
  backup_retention_period    = 30
  # maintenance_window         = "mon:10:10-mon:10:40"
  auto_minor_version_upgrade = false
  deletion_protection        = true
  skip_final_snapshot        = false
  port                       = 3306
  apply_immediately          = false
  vpc_security_group_ids     = "${data.terraform_remote_state.vpc.vpc_id}"
  parameter_group_name       = "${aws_db_parameter_group.django-service.arn}"
  option_group_name          = "${aws_db_option_group.django-service.arn}"
  db_subnet_group_name       = "${data.terraform_remote_state.db_subnet_group_name}"

  # lifecycle {
    # ignore_changes = [password]
  # }
}