#! /bin/sh

docker kill user-hasher
docker rm user-hasher
docker build -t dexcom-inc/user-hasher . && \
docker run -d -p8000:8000 --name user-hasher -e USER_SALT=TESTSALT dexcom-inc/user-hasher
