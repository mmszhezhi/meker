import time

from kafka import KafkaProducer
from kafka.admin.new_partitions import NewPartitions
from kafka import KafkaAdminClient
producer = KafkaProducer(bootstrap_servers=['119.91.148.181:9092'])
i = 0
client = KafkaAdminClient(bootstrap_servers='119.91.148.181:9092')
# rsp = client.create_partitions({
#     'my_topic': NewPartitions(4)
# })
# print(rsp)

while True:
    value = f"s2-{i}"
    future = producer.send('my_topic' , key= b'my_key', value= bytes(value,encoding="utf8"), partition= 2)
    result = future.get(timeout= 10)
    print(result)
    time.sleep(1)
    i+=1
