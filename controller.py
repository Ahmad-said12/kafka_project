from fastapi import APIRouter
from aiokafka import AIOKafkaProducer
from schemas import ItemCreate
import json

router = APIRouter()

async def send_to_kafka(topic: str, name: str):
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await producer.start()
    try:
        message = json.dumps({"name": name}).encode("utf-8")
        await producer.send_and_wait(topic, message)
    finally:
        await producer.stop()

@router.post("/items")
async def create_item(item: ItemCreate):
    await send_to_kafka("items_topic", item.name)
    return {"status": "sent to items_topic", "name": item.name}

@router.post("/items2")
async def create_item2(item: ItemCreate):
    await send_to_kafka("items_topic2", item.name)
    return {"status": "sent to items2", "name": item.name}

@router.post("/items3")
async def create_item3(item: ItemCreate):
    await send_to_kafka("items_topic3", item.name)
    return {"status": "sent to items3", "name": item.name}

@router.post("/items4")
async def create_item4(item: ItemCreate):
    await send_to_kafka("items_topic4", item.name)
    return {"status": "sent to items4", "name": item.name}