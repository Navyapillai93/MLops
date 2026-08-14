from azure.storage.blob import BlobServiceClient

# Azure Storage connection string
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=navyavoismldemo;AccountKey=Fj0i+OzM1f3DEstOc5vkZCG+pFtYuxrSO35mq5LNlTjGsGnDpqrDqe6Q6HGRWGWnZNvWQ9YesouT+AStEu7z0Q==;EndpointSuffix=core.windows.net"

# Blob container
CONTAINER = "mlops"

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(
    CONNECTION_STRING
)

def download_blob(blob_name, local_file):

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER,
        blob=blob_name
    )

    with open(local_file, "wb") as file:
        data = blob_client.download_blob()
        file.write(data.readall())

    print(f"Downloaded: {blob_name}")

def upload_blob(local_file, blob_name):

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER,
        blob=blob_name
    )

    with open(local_file, "rb") as file:
        blob_client.upload_blob(
            file,
            overwrite=True
        )

    print(f"Uploaded: {blob_name}")
