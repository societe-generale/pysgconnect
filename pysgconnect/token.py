"""
Token object
"""

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Token object"""

    created_at: datetime = datetime.now(timezone.utc)
    expires_at: Optional[datetime] = None
    jwt: Optional[str] = ""

    def is_token_expired(self) -> bool:
        """Validate the expiration date of the token"""
        if not self.expires_at:
            return True

        return self.expires_at <= datetime.now(timezone.utc)

    def is_not_empty(self) -> bool:
        """Validate that the token is not empty"""
        return self.jwt != ""
