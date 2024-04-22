"""
Token object
"""

from datetime import UTC, datetime
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Token object"""

    created_at: datetime = datetime.now(UTC)
    expires_at: Optional[datetime] = None
    jwt: Optional[str] = None

    def is_token_expired(self) -> bool:
        """Validate the expiration date of the token"""
        return not self.expires_at or self.expires_at <= datetime.now(UTC)

    def is_not_empty(self) -> bool:
        """Validate that the token is not empty"""
        return self.jwt != ""
