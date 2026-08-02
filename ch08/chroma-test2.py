import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db",  # Path to the persistent database directory)
)


client.heartbeat()