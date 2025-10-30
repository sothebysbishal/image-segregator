Go to root of this project :
ssh -i "Amneties.pem" ubuntu@ec2-51-112-244-10.me-central-1.compute.amazonaws.com

this will connect to Ubuntu

go to
/home/ubuntu/image-segregator

git pull

sudo systemctl daemon-reload

sudo systemctl restart fastapi

POST REQUEST

https://img-seg.sothebysrealty.ae/classify/url

{
"accessKey": "9Lx7fV_q2Y6sBvD3G1hK8wZ0aR5mTnUcO4pSjHq",
"url" : "https://d1snrxh3s61e7p.cloudfront.net/media/blog/cover_images/9311f9b7-a1cf-4894-ade5-261b4c3062af/indoor-play-areas-that-have-reopened-in-dubai.jpg"
}
