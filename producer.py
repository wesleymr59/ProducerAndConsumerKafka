from confluent_kafka import Producer
from loguru import logger

def delivery_callback(err, msg):
    if err:
        logger.error("%% Message failed delivery: %s\n", err)
    else:
        logger.success("%% Message delivered to %s [%d]\n", (msg.topic(), msg.partition()))


def createTopic():
    topic = "testeTopic"
    bootstrapServers = "localhost:9092"
    conf = {
        "bootstrap.servers": bootstrapServers,
        "session.timeout.ms": 6000,
        "default.topic.config": {"auto.offset.reset": "smallest"},
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "SCRAM-SHA-256",
    }

    p = Producer(conf)

    try:
        data = {"Message": "teste producer"}
        p.produce(topic, data, callback=delivery_callback)
    except BufferError as e:
        logger.warning(
            "%% Local producer queue is full (%d messages awaiting delivery): try again\n",
            len(p),
        )
    p.poll(0)
    logger.warning("%% Waiting for %d deliveries\n" % len(p))
    p.flush()


createTopic()
