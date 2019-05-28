resource "aws_instance" "django-service_1" {
  ami                         = "ami-05b296a384694dfa4"
  instance_type               = "t2.small"
  key_name                    = "${aws_key_pair.auth.id}"
  monitoring                  = true
  iam_instance_profile        = "${data.terraform_remote_state.aws_iam.ecs_instance_profile_name}"
  subnet_id                   = "${data.terraform_remote_state.vpc.public_subnet_1_id}"
  user_data                   = "${data.template_file.user_data.rendered}"
  associate_public_ip_address = true

  vpc_security_group_ids = [
    "${aws_security_group.instance.id}",
  ]

  root_block_device {
    volume_size = "20"
    volume_type = "gp2"
  }
}
# resource "aws_instance" "django-service_2" {
#   ami                         = "ami-05b296a384694dfa4"
#   instance_type               = "t2.small"
#   key_name                    = "${aws_key_pair.auth.id}"
#   monitoring                  = true
#   iam_instance_profile        = "${data.terraform_remote_state.aws_iam.ecs_instance_profile_name}"
#   subnet_id                   = "${data.terraform_remote_state.vpc.public_subnet_2_id}"
#   user_data                   = "${data.template_file.user_data.rendered}"
#   associate_public_ip_address = true

#   vpc_security_group_ids = [
#     "${aws_security_group.instance.id}",
#   ]

#   root_block_device {
#     volume_size = "20"
#     volume_type = "gp2"
#   }
# }

resource "aws_key_pair" "auth" {
  key_name = "django-service"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGJnF9qa4wfumXhpGsf2qd7EcmsZuU/kBc2sndpedrN2Ym39loj38z8p5qE3QlUfbf7xuYULsz4IcRdXFdl2Ful0hxBrLF3q8iKIpCs5MYHgcOeE2j2kBFGLpE1xizdLhO0UjZiey/AQRSVCmEvzKiY2A/pDmq+yICm/4nYtS25WCwKe7VhAbNE7YyFEqKIKtELnHx2hT0up2qZ/m8VimHb15Y1OjaBuwheammBTLa8L3t8Kx27myv4JvQcHDOlZAOv0jWylPGSxVLejKsJfNB5/IEbr8tqWmkCQqyK3jTLuE4mwW89hX8TWGjJ91iwUMQ70hlMN1QAvoUDUKHArtH imported-openssh-key"
}

