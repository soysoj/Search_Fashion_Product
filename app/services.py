import torch
import clip
import faiss
import numpy as np
from datasets import load_dataset

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# 저장된 임베딩 로드
image_embeddings = np.load('/root/aiffel/image-search/app/data/image_embeddings.npy')
text_embeddings = np.load('/root/aiffel/image-search/app/data/text_embeddings.npy')

# FAISS 인덱스 생성 및 이미지 임베딩 추가
index = faiss.IndexFlatL2(512)
index.add(image_embeddings)

# 검색 함수 정의
def search_images(query, k=5):
    query_embedding = model.encode_text(clip.tokenize([query]).to(device)).cpu().detach().numpy()
    D, I = index.search(query_embedding, k)

    # 결과 이미지 ID 및 거리 반환
    return [{"id": int(I[0][i]), "distance": float(D[0][i])} for i in range(len(I[0]))]

def get_image_by_id(image_id, images):
    return images[image_id]

import base64
from io import BytesIO

def get_image_by_id(image_id, images):
    img = images[image_id]
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str