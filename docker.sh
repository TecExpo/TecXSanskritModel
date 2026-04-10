# Building and Running the Pipeline:- 
# Once your Dockerfile is ready, use standard Docker CLI commands to build the image and execute your batch jobs. 
# Build the Image: Create a runnable image locally.


docker build -t sanskrit-batch-processor .


# Run the Container: Use bind mounts to link your local folders to the container so you can see the output files on your machine.

docker run -v 
$(pwd)/my_texts:/app/raw_sanskrit -v 
$(pwd)/results:/app/tokenized_sanskrit 
sanskrit-batch-processor
