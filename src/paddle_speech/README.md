# Paddle Speech Services

This application provides two main speech processing services using PaddleSpeech:
1. **ASR Stream Service** - Automatic Speech Recognition with WebSocket streaming
2. **TTS API Service** - Text-to-Speech synthesis with RESTful API

## Services Overview

### 1. Paddle Speech ASR Stream Service

#### 1.1 Starting the ASR Stream Server

```bash
paddlespeech_server start --config_file /paddle/speech/conf/ws_conformer_application.yaml
```

#### 1.2 Service Details
- **Protocol**: WebSocket
- **Port**: 8090
- **Endpoint**: `ws://localhost:8090/paddlespeech/asr/streaming`

#### 1.3 Usage Example (JavaScript)

```javascript
const wsUrl = "ws://localhost:3002/paddlespeech/asr/streaming";

let ws = new WebSocket(wsUrl);

ws.onopen = async () => {
  statusEl.textContent = '📡 已连接，开始发送语音数据...';

  // 发送开始指令
  const startMsg = JSON.stringify({
    name: file.name,
    signal: "start",
    nbest: 5
  }, null, 4);
  ws.send(startMsg);

  // 发送 WAV 文件内容
  const arrayBuffer = await file.arrayBuffer();
  ws.send(arrayBuffer);

  // 发送结束指令
  const endMsg = JSON.stringify({
    name: file.name,
    signal: "end",
    nbest: 5
  }, null, 4);
  ws.send(endMsg);
};

ws.onmessage = (event) => {
  console.log("收到识别结果:", event.data);
  resultEl.textContent += event.data + "\n";
  statusEl.textContent = '✅ 识别完成';
  statusEl.style.color = 'green';
};
```

### 2. Paddle Speech TTS API Service

#### 2.1 Starting the TTS Server

```bash
paddlespeech_server start --config_file /paddle/speech/conf/tts_online_application.yaml
```

#### 2.2 Service Details
- **Protocol**: RESTful API
- **Port**: 8092
- **Endpoint**: `http://localhost:8092/paddlespeech/tts/streaming`

#### 2.3 API Usage

##### Request Example

```bash
curl --location 'http://localhost:3003/paddlespeech/tts/streaming' \
--header 'Content-Type: application/json' \
--data '{
    "text": "你好，欢迎使用百度飞桨语音合成服务。",
    "spk_id": 0,
    "speed": 1.0,
    "volume": 1.0,
    "sample_rate": 0,
    "tts_audio_path": "./tts.wav"
}'
```

##### Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | string | 要合成的文本内容 |
| `spk_id` | integer | 说话人ID |
| `speed` | float | 语速 (1.0为正常速度) |
| `volume` | float | 音量 (1.0为正常音量) |
| `sample_rate` | integer | 采样率 (0为默认) |
| `tts_audio_path` | string | 音频文件保存路径 |

##### Response

成功时返回语音PCM的Base64编码数据。

**Response Headers:**
```
date: Thu, 07 Aug 2025 02:43:42 GMT
server: uvicorn
Transfer-Encoding: chunked
```

**Response Body:**
```
QVFEOC8vLy9BQUQ4L3dBQS9.....i8zLy9wLyt2Lw==
```

> **注意**: 返回的Base64数据是PCM格式，需要添加WAV头文件才能正常播放。

## Configuration Files

The service uses the following configuration files located in `/paddle/speech/conf/`:

- `ws_conformer_application.yaml` - ASR stream service configuration
- `tts_online_application.yaml` - TTS API service configuration
- `application.yaml` - General application configuration
- `vector_application.yaml` - Vector service configuration
- `ws_conformer_wenetspeech_application_faster.yaml` - Faster ASR configuration
- `ws_ds2_application.yaml` - DS2 model configuration

## Docker Support

This application includes Docker support. See the `Dockerfile` in this directory for containerization details.

## Version

Current version can be found in the `VERSION` file.

## Requirements

Make sure you have PaddleSpeech server installed and properly configured before running these services.
