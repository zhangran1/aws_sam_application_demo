variable "allocated_storage" {
  default = 20
}

variable "storage_type" {
  default = ""
  type = string
}

variable "engine" {
  default = ""
  type = string
}

variable "instance_class" {
  default = ""
  type = string
}

variable "db_name" {
  default = ""
  type = string
}

variable "db_username" {
  default = ""
  type = string
}

variable "db_password" {
  default = ""
  type = string
}
