import logging


# Configure logging
logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Create logger
logger = logging.getLogger()
