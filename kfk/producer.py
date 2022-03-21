import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['119.91.148.181:9092'])
i = 0
while True:
    value = f"s1-{i}"
    future = producer.send('my_topic' , key= b'my_key', value= bytes(value,encoding="utf8"), partition= 0)
    result = future.get(timeout= 10)
    print(result)
    time.sleep(1)
    i+=1
