import smartbchpy
from telegram.ext import Updater, CommandHandler

# Set up smartBCH API endpoint
rpc_url = "https://smartbch.greyh.at"

# Initialize smartBCH API client
client = smartbchpy.client.EthJsonRpc(rpc_url)

# Define function to handle the /tx command
def tx_handler(update, context):
    # Get the transaction hash from the user's message
    tx_hash = context.args[0]

    # Query the smartBCH API for transaction details
    tx = client.get_transaction_by_hash(tx_hash)

    # Send the transaction details back to the user
    update.message.reply_text(f"Transaction details:\n{tx}")

# Define function to handle the /balance command
def balance_handler(update, context):
    # Get the wallet address from the user's message
    address = context.args[0]

    # Query the smartBCH API for the wallet balance
    balance = client.get_balance(address)

    # Send the wallet balance back to the user
    update.message.reply_text(f"Wallet balance:\n{balance}")

# Set up the Telegram bot
updater = Updater("5991247097:AAFrgzPJhNwuTKiS-qvaXsURyp9Y7tb1Ui4", use_context=True)
dispatcher = updater.dispatcher

# Set up message handlers
dispatcher.add_handler(CommandHandler("tx", tx_handler))
dispatcher.add_handler(CommandHandler("balance", balance_handler))

# Start the bot
updater.start_polling()
