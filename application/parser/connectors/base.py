"""
Base classes for external knowledge base connectors.

This module provides minimal abstract base classes that define the essential
interface for external knowledge base connectors.
"""

from abc import ABC, abstractmethod
from typing import Any

from application.parser.schema.base import Document


class BaseConnectorAuth(ABC):
    """
    Abstract base class for connector authentication.
    
    Defines the minimal interface that all connector authentication
    implementations must follow.
    """
    
    @abstractmethod
    def get_authorization_url(self, state: str | None = None) -> str:
        """
        Generate authorization URL for OAuth flows.
        
        Args:
            state: Optional state parameter for CSRF protection
            
        Returns:
            Authorization URL
        """
    
    @abstractmethod
    def exchange_code_for_tokens(self, authorization_code: str) -> dict[str, Any]:
        """
        Exchange authorization code for access tokens.
        
        Args:
            authorization_code: Authorization code from OAuth callback
            
        Returns:
            Dictionary containing token information
        """
    
    @abstractmethod
    def refresh_access_token(self, refresh_token: str) -> dict[str, Any]:
        """
        Refresh an expired access token.
        
        Args:
            refresh_token: Refresh token
            
        Returns:
            Dictionary containing refreshed token information
        """
    
    @abstractmethod
    def is_token_expired(self, token_info: dict[str, Any]) -> bool:
        """
        Check if a token is expired.
        
        Args:
            token_info: Token information dictionary
            
        Returns:
            True if token is expired, False otherwise
        """


class BaseConnectorLoader(ABC):
    """
    Abstract base class for connector loaders.
    
    Defines the minimal interface that all connector loader
    implementations must follow.
    """
    
    @abstractmethod
    def __init__(self, session_token: str):
        """
        Initialize the connector loader.
        
        Args:
            session_token: Authentication session token
        """
    
    @abstractmethod
    def load_data(self, inputs: dict[str, Any]) -> list[Document]:
        """
        Load documents from the external knowledge base.
        
        Args:
            inputs: Configuration dictionary containing:
                - file_ids: Optional list of specific file IDs to load
                - folder_ids: Optional list of folder IDs to browse/download
                - limit: Maximum number of items to return
                - list_only: If True, return metadata without content
                - recursive: Whether to recursively process folders
                
        Returns:
            List of Document objects
        """
    
    @abstractmethod
    def download_to_directory(self, local_dir: str, source_config: dict[str, Any] = None) -> dict[str, Any]:
        """
        Download files/folders to a local directory.
        
        Args:
            local_dir: Local directory path to download files to
            source_config: Configuration for what to download
            
        Returns:
            Dictionary containing download results:
                - files_downloaded: Number of files downloaded
                - directory_path: Path where files were downloaded
                - empty_result: Whether no files were downloaded
                - source_type: Type of connector
                - config_used: Configuration that was used
                - error: Error message if download failed (optional)
        """
