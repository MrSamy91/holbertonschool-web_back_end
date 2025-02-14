#!/usr/bin/env python3
"""Module for password encryption using bcrypt."""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with salt.
    
    Args:
        password: String password to be hashed
        
    Returns:
        bytes: Salted and hashed password
    """
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate the salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password.
    
    Args:
        hashed_password: Bytes of the hashed password
        password: String of the password to check
        
    Returns:
        bool: True if password matches, False otherwise
    """
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    
    # Check if the password matches the hash
    return bcrypt.checkpw(password_bytes, hashed_password) 