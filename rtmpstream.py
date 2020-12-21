import base64

import librtmp

# Create a connection
conn = librtmp.RTMP("rtmp://20.46.44.246:1935/stream/ashustream")
conn.connect()

stream = conn.create_stream()

data = stream.read(1024)

# with open('test.flv', 'wb') as f:
#     stream.write(data)
