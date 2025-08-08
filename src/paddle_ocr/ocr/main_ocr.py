from fastapi import FastAPI, UploadFile, File
import codecs
import sys
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from ocr_paddle import ocr

from PIL import Image
import io

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
        allow_origins=["*"],
        # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
        allow_credentials=False,
        # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
        allow_methods=["*"],
        # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
        # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
        allow_headers=["*"],
        # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
        # expose_headers=["*"]
        # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
        # max_age=1000
)

@app.post("/image2text/")
async def image2text(file: UploadFile):
    # print(file.filename)
    try:
        # 检查文件是否上传成功
        if file.content_type.startswith('image'):
            # 指定本地文件保存路径
            with open(f"./uploads/{file.filename}", "wb") as f:
                f.write(file.file.read())
            res=ocr(file.filename)
            
            return JSONResponse(content={"message": res}, status_code=200)
        else:
            return JSONResponse(content={"message": "Invalid file format. Only images are allowed."}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
    
@app.post("/image2text2/")
async def image2text2(image_bytes):
    print(image_bytes)
    status=0
    res=""
    try:
        image_stream = io.BytesIO(image_bytes)
        # print(file.filename)
        # 指定图像文件的本地保存路径
        save_path = "./uploads/image.png"
        image = Image.open(image_stream)

        # 保存图像到本地文件
        image.save(save_path)
        status=200
        res=ocr("image.png")
    except Exception as e:
        status=500
    finally:
        # 关闭图像对象和二进制流
        image.close()
        image_stream.close()
    return JSONResponse(content={"message": res}, status_code=status)
  
# 在最下面加上 这一句 代替命令行启动
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main_ocr:app', host="0.0.0.0", port=8888, reload=True)
