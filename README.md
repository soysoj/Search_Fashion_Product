## Coder: 윤소정
# Search_Fashion_Product
### Search_Fashion_Product.ipynb
* Dataset: Fashion product images small (https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small)
* Model: CLIP
* Vector Databases: FAISS
* Fashion Product Image 데이터셋에서 image와 text를 뽑아내 임베딩을 생성하고 유사도를 계산하였습니다. 그리고 FAISS를 이용하여 검색 인덱스를 구축했습니다. <br>
![image](https://github.com/user-attachments/assets/f34bbbbc-0dcf-4c59-8645-854e5ffa0168)<br>

* quesry에 pink t-shir, purple shoes, blue long pants, pink blouse 등을 검색하면 아래와 같은 이미지들이 출력됐습니다.<br>
![image](https://github.com/user-attachments/assets/134e4a56-7735-4323-adba-1a4d8a19b7bf)
![image](https://github.com/user-attachments/assets/6a5db158-26ec-4684-a2c7-1d1ecae308eb)
![image](https://github.com/user-attachments/assets/fe73dff3-c153-4ada-9364-faaff60d6087)
![image](https://github.com/user-attachments/assets/1bde3446-442e-4785-b619-fdb5ec0e0e7f)
<br>

### main.py + app folder + static folder
* 위의 jupyter notebook을 바탕으로 Fast API를 사용하여 웹 프레임 워크를 만들었습니다.
* 위와 마찬가지로 똑같은 방식으로 Fast API와 HTML, CSS를 이용해 패션 아이템 검색창을 만들었습니다.
*  text 창에 pink t-shirt, purple shoes, blue long pants, watch 등을 검색했을때 아래와 같은 결과를 볼 수 있었습니다.<br>
![image](https://github.com/user-attachments/assets/a7674704-f102-4c29-8375-fce974d5ad16)
![image](https://github.com/user-attachments/assets/0eee0f30-a0f7-440b-9b80-2ebd25ebd012)
![image](https://github.com/user-attachments/assets/d9e5e747-5876-4924-9ca9-3abc03295f64)
![image](https://github.com/user-attachments/assets/eca2c1b1-69bb-48e7-b677-91a5212dc0f2)<br>
* 총 5개 아이템씩 보여달라고 했기때문에 만약 아이템이 4개이하일 경우에는 다른 아이템들도 보여주는 것으로 보인다. 이는 차후에 이 부분에 대한 에러를 고쳐보려고합니다.
  * app folder안 data folder에는 image_embedding.npy와 text_embedding.npy 파일들이 있는데 용량이 커서 upload를 시키지 못 했습니다. 따라서 밑의 링크를 들어가시면 image_embedding.npy와 txt_embedding.npy를 다운받아 사용하실 수 있습니다.<br>
    [임베딩 파일 다운받기(Download npy embedding files)](https://drive.google.com/drive/folders/1ouMI7tMUchOapLHx-O_YYgoaTZaeZATd?usp=drive_link)


