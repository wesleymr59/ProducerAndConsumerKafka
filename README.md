ProducerAndConsumerKafka
Projeto que implementa um produtor e um consumidor Kafka usando Python, para comunicação e troca de mensagens em um ambiente de microsserviços. Este projeto utiliza Docker e Kafka para garantir a escalabilidade e a confiabilidade do sistema.

Estrutura do Projeto
Producer: Envia mensagens para um tópico Kafka específico.
Consumer: Escuta o tópico Kafka e processa as mensagens recebidas.
Kafka-UI: Interface gráfica para monitoramento de tópicos, mensagens e consumidores.
Pré-requisitos
Para executar o projeto, você precisará dos seguintes requisitos:

Docker e Docker Compose instalados
Python 3.7+
Bibliotecas Python (listadas em requirements.txt)
Configuração
Clone o repositório e instale as dependências:
```
bash

git clone <URL do repositório>
cd ProducerAndConsumerKafka
pip install -r requirements.txt
```
Docker Compose
O projeto utiliza um arquivo docker-compose.yml para levantar o ambiente Kafka e Kafka-UI:
```
yaml

version: '2'

networks:
  app-tier:
    driver: bridge

services:
  kafka:
    image: 'bitnami/kafka:latest'
    networks:
      - app-tier
    environment:
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka:9093
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092
    ports:
      - "9092:9092"

  kafka-ui:
    image: provectuslabs/kafka-ui
    container_name: kafka-ui
    networks:
      - app-tier
    depends_on:
      - kafka
    ports:
      - "8080:8080"
    environment:
      - KAFKA_CLUSTERS_0_NAME=KafkaCluster
      - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka:9092
```

Para iniciar os serviços, execute:

```
docker-compose up -d  
```
A interface Kafka-UI estará disponível em http://localhost:8080.

Configuração de Conexão com Kafka
A configuração do cliente Kafka é definida no código como um dicionário de parâmetros. Por exemplo:

```

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'teste-consumer',
    'session.timeout.ms': 6000,
    'auto.offset.reset': 'earliest',
}
```
Este código define o servidor de bootstrap, o ID do grupo de consumidores e outros parâmetros necessários para conexão.

Como Executar
Producer (Produtor)
O produtor envia mensagens para o tópico Kafka definido. Para rodar o produtor, execute o script producer.py:

```
python producer.py
```
Consumer (Consumidor)
O consumidor escuta o tópico Kafka e processa as mensagens recebidas. Para rodar o consumidor, execute o script consumer.py:

```
python consumer.py
```
Exemplo de Mensagem
Uma mensagem JSON é enviada pelo produtor, como:

```
{"message": "Exemplo de mensagem para Kafka"}
```
O consumidor receberá e processará esta mensagem, convertendo o JSON em um dicionário Python.

Erros Comuns
ConfigException: Ocorre se as configurações de Kafka estiverem incorretas. Verifique o arquivo docker-compose.yml e as configurações de conexão.
Connection setup timed out: Verifique se o bootstrap.servers está configurado corretamente com o endereço do broker Kafka.
Contribuição

Para contribuir com este projeto, crie um fork, faça suas alterações em uma nova branch e envie um pull request.
