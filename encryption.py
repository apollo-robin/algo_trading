# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:58:03 2021

@author: robin
"""


from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


def encrypt_password(password):
    return pwd_context.hash(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)
