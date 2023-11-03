import ldk_node

# Docs: https://docs.rs/ldk-node/0.1.0/ldk_node/index.html

builder = ldk_node.Builder()
network = ldk_node.Network.REGTEST
builder.set_network(network)
builder.set_esplora_server("http://localhost:3002")
node = builder.build()

node.start()

funding_address = node.new_onchain_address()
print("Funding address: {}".format(funding_address))

balance = node.spendable_onchain_balance_sats()
print(balance)
print(node.node_id())

node_id = "NODE_ID"
node_addr = "IP_ADDR:PORT"
node.connect_open_channel(node_id, node_addr, 1000000, None, None, False)

event = node.wait_next_event()
print(event)
node.event_handled()

channels = node.list_channels()
for channel in channels:
    print(channel.outbound_capacity_msat)

invoice = "INVOICE_STR"

node.send_payment(invoice)

node.stop()