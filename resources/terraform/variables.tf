variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "access_key" {
  description = "AWS Access Key"
  type        = string
  default     = "to-change" // TODO
}

variable "secret_key" {
  description = "AWS Secret Key"
  type        = string
  default     = "to-change" // TODO
}


variable "session_token" {
  description = "AWS Session Token"
  type        = string
  default     = "to-change" // TODO
}


variable "role_arn" {
  description = "AWS Lab Role ARN"
  type        = string
  default     = "to-change" // TODO
}

variable "separator" {
  description = "Command line separator. If using windows use '&', if using macOS use ';'"
  type = string
  default = "&" // TODO
}


