import asyncio
import chromadb

async def main():
    client = await chromadb.AsyncHttpClient()

    collection = await client.get_or_create_collection(name="minutes_collection")
    await collection.add(
        documents=["hello world", "this is a test document"],
        ids=["doc1", "doc2"]
    )

asyncio.run(main())