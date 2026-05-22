# Try to connect with redis cache

import redis

def connect__redis():
    try:
        client = redis.Redis(
            host = "localhost",
            port = 6379, 
            password = None,
            decode_responses = True
        )
        # Test Connection
        if client.ping():
             print("redis connect is ok")
        else:
            print("Failed to connect with redis")
        # key with no expirey
        client.set("username", "Tejas_don")
        print(client.get("username"))
    except Exception as e:
        print(f"Error while connecting with redis {e}")

if __name__ == "__main__":
    connect__redis()