# aws-iot-python
Utilities using the Python AWS SDK https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html

Used for creating the AWS
online MQTT lab at https://mqttlab.iotsim.io/aws, and
large-scale prototypes with MIMIC MQTT Simulator https://www.gambitcomm.com/site/mqttsimulator.php

    % python list_things.py
    Usage: listthings.py
    -r|--region region-name AWS_REGION
  	-a|--access access-key  AWS_ACCESS_KEY_ID
  	-s|--secret secret-key  AWS_SECRET_ACCESS_KEY
  	[-v|--verbose]          verbose output

    % python list_things.py -r us-east-2 -a 'XXXXX' -s 'XXXX'
    {u'things': [{u'thingArn': u'arn:aws:iot:us-east-1:409128494776:thing/mimic-10', u'version': 1,
    u'thingName': u'mimic-10', u'attributes': {}}, {u'thingArn': u'arn:aws:iot:us-east-1:409128494776:thing/mimic-9',
    u'version': 1, u'thingName': u'mimic-9', u'attributes': {}},...
    
    % python get_thing_shadow.py -r us-east-2 -a 'xxxxx' -s 'xxxxx' -t mimic-1
    {u'timestamp': 1587393680, u'state': {u'reported': {u'color': u'yellow', u'mem': 25, u'temp': 50000, u'power': u'on', u'light': 4157}}, u'version': 3765, u'metadata': {u'reported': {u'color': {u'timestamp': 1584978911}, u'mem': {u'timestamp': 1584978911}, u'temp': {u'timestamp': 1584978911}, u'power': {u'timestamp': 1584978911}, u'light': {u'timestamp': 1584978911}}}}


