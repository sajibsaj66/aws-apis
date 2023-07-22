`aws-robot-avatar-api.py` uses robohash.org for generating robot-based avatars based on username.

`aws-video-transcode-api.py` merges multiple `.ts` files with the same prefix `channel_name` and converts the output to an `.mp4` file.

To deploy the former to AWS Lambda you may need to create a deployment .zip package with dependencies as it requires the use of `requests` package. Refer [this documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) for more information.

The latter can be deployed directly to Lambda without requiring any additional packages, but you will need to create a pipeline in [Elastic Transcoder](https://aws.amazon.com/elastictranscoder/). Assign the input bucket, IAM Role, output bucket correctly when creating the pipeline.

Replace the PipelineID value in the `aws-video-transcode-api.py` file with the id of the newly created pipeline (you'll find this when you click the search button close to the pipeline in question).

Next, you have to create new REST APIs for the Lambda functions with AWS API Gateway.

For robot avatar generator REST API, create a resource at the root (/) with resource name and path set to `username`. Next, create a GET method for this resource and integrate it with the `aws-robot-avatar-api.py` Lambda function.

For transcoding API, create a resouce at the root (/) with resource name and path set to `channel_name`, and create a GET method for it with the `aws-video-transcode-api.py` Lambda function.

Finally, deploy both the APIs.
