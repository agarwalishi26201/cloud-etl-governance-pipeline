provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "data_lake_raw" {
  bucket = "enterprise-data-lake-raw-logs-prod"
}

resource "aws_s3_bucket_lifecycle_configuration" "tiering" {
  bucket = aws_s3_bucket.data_lake_raw.id

  rule {
    id     = "move-to-glacier"
    status = "Enabled"

    transition {
      days          = 90
      storage_class = "STANDARD_IA"
    }
  }
}
