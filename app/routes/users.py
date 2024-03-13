from fastapi import APIRouter, Response
from typing import List
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from schema.user import userEntity, usersEntity, serializeDict
from models.user import User


user = APIRouter()


@user.post("/users")
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = conn.local.user.insert_one(new_user).inserted_id
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.get("/users/{user_id}")
def find_user(user_id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(user_id)}))


@user.get("/users")
def find_all_users():
    return usersEntity(conn.local.user.find())


@user.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    update_user = dict(user)
    update_user["password"] = sha256_crypt.encrypt(update_user["password"])
    conn.local.user.find_one_and_update(
        {"_id": ObjectId(user_id)}, {"$set": update_user}
    )
    return userEntity(conn.local.user.find_one({"_id": ObjectId(user_id)}))


@user.delete("/users/{user_id}")
def delete_user(user_id: str):
    conn.local.user.find_one_and_delete({"_id": ObjectId(user_id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
