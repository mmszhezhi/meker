from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', group_id= 'group2', bootstrap_servers= ['119.91.148.181:9092'])
for msg in consumer:
    print(str(msg.value.decode()))