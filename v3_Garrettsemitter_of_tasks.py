"""
    This program sends a message to a queue on the RabbitMQ server.
    Make tasks harder/longer-running by adding dots at the end of the message.

    Author: Garrett Kopp
    Date: September 16, 2023

"""

import pika
import sys
import webbrowser
# Import the custom logger setup utility (local file named util_logger.py)
from util_logger import setup_logger
import csv
import time
import logging

# Setup custom logging
logger, logname = setup_logger(__file__)

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants
HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
TASKS_FILE_NAME = "tasks.csv"
SHOW_OFFER = False

def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    global SHOW_OFFER
    if SHOW_OFFER:
        webbrowser.open_new("http://localhost:15672/#/queues")

def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """

    try:
        # Define RabbitMQ credentials
        credentials = pika.PlainCredentials(username="guest", password="7hdBx81984")

        # create a blocking connection to the RabbitMQ server with credentials
        conn = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=credentials))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        ch.queue_declare(queue=queue_name, durable=True)
        # use the channel to publish a message to the queue
        # every message passes through an exchange
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)
        # print a message to the console for the user
        print(f" [x] Sent {message}")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":

    # get the message from the command line
    # if no arguments are provided, use the default message
    # use the join method to convert the list of arguments into a string
    # join by the space character inside the quotes
    message = " ".join(sys.argv[1:]) or "twelfth task....."
    # send the message to the queue
    send_message("localhost", "task_queue3", message)