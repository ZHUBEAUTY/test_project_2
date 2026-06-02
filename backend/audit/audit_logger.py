import logging

logger = logging.getLogger("audit")

class AuditLogger:
    def log_request(self, headers):
        logger.info(headers)

    def log_event(self, message):
        logger.info(message)
