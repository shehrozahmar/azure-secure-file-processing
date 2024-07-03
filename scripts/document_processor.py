from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Initialize the DefaultAzureCredential
credential = DefaultAzureCredential()

# Create a BlobServiceClient using the managed identity
blob_service_client = BlobServiceClient(account_url="https://<storage-account>.blob.core.windows.net", credential=credential)

# Get a client to interact with the specific container
container_client = blob_service_client.get_container_client("shehrozcontainer")

# Open a local file to write the results
with open("processed_files_results.txt", "w") as result_file:
    # List and process blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        blob_client = container_client.get_blob_client(blob)
        download_stream = blob_client.download_blob()
        file_content = download_stream.readall()
        result_file.write(f"Processing blob: {blob.name}\n")
        result_file.write(f"File content: {file_content}\n\n")
