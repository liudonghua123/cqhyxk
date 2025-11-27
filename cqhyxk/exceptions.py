"""
Custom exceptions for the cqhyxk SDK
"""


class CqhyxkException(Exception):
    """Base exception class for cqhyxk SDK"""
    pass


class AuthenticationError(CqhyxkException):
    """Raised when there is an authentication error"""
    pass


class APIError(CqhyxkException):
    """Raised when the API returns an error response"""
    def __init__(self, message: str, code: str = None):
        # Ensure the message is properly encoded
        if isinstance(message, bytes):
            message = message.decode('utf-8', errors='ignore')
        elif not isinstance(message, str):
            message = str(message)
        super().__init__(message)
        self.code = code


class RequestError(CqhyxkException):
    """Raised when there is an error making a request"""
    pass