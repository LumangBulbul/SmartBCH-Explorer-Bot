import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from smartbch.wallet import Wallet

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Set up SmartBCH connection
SMARTBCH_RPC = os.getenv('SMARTBCH_RPC')
wallet = Wallet()
wallet.from_mnemonic(os.getenv('SMARTBCH_MNEMONIC'))
wallet.connect(SMARTBCH_RPC)

# Define commands
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am a SmartBCH Explorer bot. How can I help you?')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('You can use the following commands:\n\n'
                              '/wallet <address> - get information about a SmartBCH wallet\n'
                              '/tx <hash> - get information about a SmartBCH transaction\n'
                              '/price - get the current SmartBCH and Bitcoin Cash prices\n'
                              '/token <address> - get the current price of a token\n'
                              '/donate - donate to the bot developer')

def wallet_command(update: Update, context: CallbackContext) -> None:
    """Send information about a SmartBCH wallet."""
    address = context.args[0]
    balance = wallet.get_balance(address)
    update.message.reply_text(f'Address: {address}\n'
                              f'Balance: {balance}')

def tx_command(update: Update, context: CallbackContext) -> None:
    """Send information about a SmartBCH transaction."""
    tx_hash = context.args[0]
    tx = wallet.get_transaction(tx_hash)
    update.message.reply_text(f'Hash: {tx.hash}\n'
                              f'From: {tx.from_address}\n'
                              f'To: {tx.to_address}\n'
                              f'Value: {tx.value}\n'
                              f'Gas Price: {tx.gas_price}\n'
                              f'Gas Limit: {tx.gas_limit}\n'
                              f'Block Number: {tx.block_number}\n'
                              f'Timestamp: {tx.timestamp}')

def price_command(update: Update, context: CallbackContext) -> None:
    """Send the current SmartBCH and Bitcoin Cash prices."""
    price = wallet.get_price()
    update.message.reply_text(f'SmartBCH Price: {price["smtbch_usd"]} USD\n'
                              f'Bitcoin Cash Price: {price["bch_usd"]} USD')

def token_command(update: Update, context: CallbackContext) -> None:
    """Send the
