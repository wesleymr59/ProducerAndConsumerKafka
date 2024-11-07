import json
import sys
from confluent_kafka import Consumer, KafkaException, KafkaError
from loguru import logger
def createConsumer():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'teste-consumer',
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
    }
    c = Consumer(conf)
    c.subscribe(['testeTopic'])
    
    try:
        logger.info("Consumer Started")
        while True:
            logger.info("Find Message")
            msg = c.poll(timeout=1.0)
            if msg is None:
               continue
            if msg.error():
               # mensagem de erro
               print( msg.error )
            else:
               msg_value = msg.value()
               decoded_value = msg_value.decode('utf-8')
               # print com a mensagem do tópico
               print(json.loads(decoded_value))
    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')
    # Close down consumer to commit final offsets.
    c.close()

createConsumer()