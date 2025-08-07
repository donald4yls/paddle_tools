# paddle_tools
Tools based on Paddle paddle platform.



* docker build -t paddle_speech:1.0 .
* docker run -d --name paddle_speech -p 3002:8090 -p 3003:8092 paddle_spech:1.0



docker build -t blip_api_app .

docker run -d --gpus all -p 8002:8070 -v  --name blip_api blip_api_app
