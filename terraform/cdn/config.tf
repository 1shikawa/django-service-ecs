terraform {
  backend "s3" {
    bucket = "terraform-setting"
    key    = "cloudfront/terraform.tfstate"
    region = "ap-northeast-1"
  }
}

provider "aws" {
  region = "ap-northeast-1"
}
