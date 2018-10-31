variable "account_id" {}

module "lambda_api_gateway" {
    source               = "git@github.com:techjacker/terraform-aws-lambda-api-gateway"

    # tags
    project              = "tykvc"
    service              = "tykvc"
    owner                = "joshuaj004"
    costcenter           = "joshuaj004-tykvc"

    # vpc
    vpc_cidr             = "10.0.0.0/16"
    public_subnets_cidr  = ["10.0.1.0/24", "10.0.2.0/24"]
    private_subnets_cidr = ["10.0.3.0/24", "10.0.4.0/24"]
    nat_cidr             = ["10.0.5.0/24", "10.0.6.0/24"]
    igw_cidr             = "10.0.8.0/24"
    azs                  = ["us-east-1a", "us-east-1b"]

    # lambda
    lambda_zip_path      = "flask-app.zip"
    lambda_handler       = "run_lambda.http_server"
    lambda_runtime       = "python3.6"
    lambda_function_name = "HttpWebserver"

    # API gateway
    region               = "us-east-1"
    account_id           = "${var.account_id}"
}

output "api_url" {
  value = "${module.lambda_api_gateway.api_url}"
}

output "lambda_zip" {
  value = "${module.lambda_api_gateway.lambda_zip}"
}
