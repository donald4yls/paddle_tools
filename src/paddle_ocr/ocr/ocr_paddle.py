from paddleocr import PaddleOCR

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
def ocr(file_name):
    ocr = PaddleOCR(use_textline_orientation=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = './uploads/'+file_name
    result = ocr.predict(img_path)

    # 调试：打印 result 的实际结构
    print("Result type:", type(result))
    print("Result length:", len(result))

    reconigized_texts = {}
    for i, res in enumerate(result):
        if res:  # 如果第一个元素不为空
            print(i, ": Text detected:", res["rec_texts"], "\r\n")  # 打印检测到的文本
            print(i, ": Text detected:", res["rec_scores"], "\r\n")  # 打印检测到的文本
            reconigized_texts[i] = {
                "rec_texts": res["rec_texts"],
                "rec_scores": res["rec_scores"]
            }
    return reconigized_texts  # 返回识别的文本和分数