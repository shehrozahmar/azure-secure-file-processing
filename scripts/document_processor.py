#sample script to process files in a secure way

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(account_url="https://<storage-account>.blob.core.windows.net", credential=credential)

container_client = blob_service_client.get_container_client("<container>")

blob_list = container_client.list_blobs()
for blob in blob_list:
    blob_client = container_client.get_blob_client(blob)
    download_stream = blob_client.download_blob()
    file_content = download_stream.readall()
    print(f"Processing blob: {blob.name}")
