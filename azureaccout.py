from azure.storage.blob import BlobServiceClient

connect_str = ""
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = "images"
blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample.txt")


with open("sample.txt", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("Upload successful!")

 