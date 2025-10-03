import random

def is_prime(n, k=5):

    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(d.bit_length() - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=16):

    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1
        if is_prime(p):
            return p

def extended_gcd(a, b):

    if a == 0: return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def mod_inverse(e, phi):

    d, x, y = extended_gcd(e, phi)
    if d != 1: raise Exception('Modular inverse does not exist')
    return x % phi

class Proxy:

    def __init__(self):
        print("Proxy is online.")
        self.node_directory = {}

    def register_node(self, node, public_key):
        print(f"Registering public key for node: {node.node_id}")
        self.node_directory[node.node_id] = {
            "node": node,
            "public_key": public_key
        }

    def get_public_key(self, node_id: str):
        if node_id in self.node_directory:
            return self.node_directory[node_id]["public_key"]
        return None

    def route_message(self, sender_id: str, recipient_id: str, encrypted_message_int: int):
        print(f"\nProxy received an encrypted packet from '{sender_id}' for '{recipient_id}'.")
        print("Routing opaque packet. Content cannot be read.")
        if recipient_id in self.node_directory:
            recipient_node = self.node_directory[recipient_id]["node"]
            print(f"Forwarding packet to '{recipient_id}'.")
            recipient_node.receive_message(sender_id, encrypted_message_int)
        else:
            print(f"Error: Recipient '{recipient_id}' not found in directory.")

class Node:

    def __init__(self, node_id: str, proxy: Proxy):
        self.node_id = node_id
        self.proxy = proxy
        self.inbox = []
        print(f"Node '{self.node_id}' is generating keys. This may take a moment.")
        p, q = generate_prime(bits=256), generate_prime(bits=256)
        while p == q: q = generate_prime(bits=256)
        n, phi = p * q, (p - 1) * (q - 1)
        e = 65537
        d = mod_inverse(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)
        self.proxy.register_node(self, self.public_key)
        print(f"Node '{self.node_id}' is online.")

    def send_message(self, recipient_id: str, message_text: str):
        print(f"\nNode '{self.node_id}' is preparing a message for '{recipient_id}'.")
        print(f"Sending message: '{message_text}'")
        recipient_public_key = self.proxy.get_public_key(recipient_id)
        if not recipient_public_key:
            print(f"Error: Could not retrieve public key for '{recipient_id}'.")
            return
        n, e = recipient_public_key
        message_int = int.from_bytes(message_text.encode('utf-8'), 'big')
        if message_int.bit_length() > n.bit_length():
            print(f"Error: Message is too large for the recipient's key.")
            return
        encrypted_int = pow(message_int, e, n)
        print(f"Message encrypted using '{recipient_id}'s public key.")
        self.proxy.route_message(self.node_id, recipient_id, encrypted_int)

    def receive_message(self, sender_id: str, encrypted_message_int: int):
        print(f"Node '{self.node_id}' received an encrypted packet from '{sender_id}'.")
        n, d = self.private_key
        decrypted_int = pow(encrypted_message_int, d, n)
        message_text = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8', errors='ignore')
        print(f"Decrypted message: '{message_text}'")
        self.inbox.append({"from": sender_id, "message": message_text})

    def read_inbox(self):
        print(f"\nInbox for Node '{self.node_id}':")
        if not self.inbox:
            print("Inbox is empty.")
        for msg in self.inbox:
            print(f"From '{msg['from']}': {msg['message']}")
        print("---------------------------------")

if __name__ == "__main__":

    the_proxy = Proxy()
    print("-" * 20)
    node_a = Node(node_id="alpha", proxy=the_proxy)
    node_b = Node(node_id="beta", proxy=the_proxy)
    node_a.send_message(
        recipient_id="beta", 
        message_text="This is a confidential message for Beta only."
    )
    node_a.read_inbox()
    node_b.read_inbox()
