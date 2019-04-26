terraform {
  backend "s3" {
    bucket = "terraform-setting"
    key    = "sample/service/terraform.tfstate"
    region = "ap-northeast-1"
  }
}

provider "aws" {
  region = "ap-northeast-1"
}
