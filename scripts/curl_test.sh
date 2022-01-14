#!/bin/bash

curl "localhost:5000" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: hY9VLNNfCMuQXzHuXsNg" \
-H "X-Naver-Client-Secret: VmtfBzhWuf" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
