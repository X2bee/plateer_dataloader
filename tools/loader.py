from datasets import load_dataset
from huggingface_hub import login

def plateer_dataset(name:str, token: str = None):
    """
    데이터 셋을 불러오는 함수입니다.
    name: str - 데이터 셋의 이름을 입력합니다.
    
    데이터 셋의 이름은 다음과 같습니다.
    1. 'plateer-ctg' - Plateer 카테고리 분류 데이터 셋
    2. 'ko-wiki' - 한국어 위키백과 데이터 셋
    3. 'ko-namuwiki' - 한국어 나무위키 데이터 셋
    4. 'kcbert-data' - KcBERT 학습 데이터 셋 (뉴스 댓글)
    5. 'ko-nli-class' - 한국어 NLI 데이터 셋 (KAKAO제공 NLI 작업 학습용)
    6. 'ko-nli-score' - 한국어 NLI 데이터 셋을 STS 형태로 변환환 (KAKAO제공 NLI 작업 학습용)
    7. 'ko-sts' - 한국어 STS 데이터 셋 (KAKAO제공 STS 작업 학습용)
    
    token: str - Huggingface의 토큰을 입력합니다.
    x2bee repository에 접근할 수 있어야 합니다.
    """
    
    if name == "plateer-ctg":
        login(token=token)
        dataset = load_dataset("x2bee/plateer_category_data", data_dir="data")
        dataset = dataset['train']
        
        print("""
              카테고리 분류 모델 학습을 위해 제작된 데이터 셋입니다.
              총 17개의 카테고리에 대한 데이터가 구성되어 있습니다.
              생성데이터 및 상품의 일반명/품명이 섞여 있습니다.
              
              데이터의 총 개수는 24,287,817개로 구성되어 있습니다.
              """)
        
        return dataset
    
    elif name == "ko-wiki":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_wiki_corpus_all", data_dir="data")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/lovit/kowikitext
                
                한국어 위키백과 데이터 셋입니다.
                데이터의 총 개수는 14,761,960개로 구성되어 있습니다.
                """)
        
        return dataset
    
    elif name == "ko-namuwiki":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_namuwiki_corpus", data_dir="data")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/lovit/namuwikitext
                
                한국어 나무위키 데이터 셋입니다.
                데이터의 총 개수는 21,366,681개로 구성되어 있습니다.
                """)
        
        return dataset
    
    elif name == "kcbert-data":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_kcbert_corpus_all", data_dir="data")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/Beomi/KcBERT
                
                한국어 뉴스 기사 댓글로 구성된 데이터입니다.
                데이터의 총 개수는 86,246,285개로 구성되어 있습니다. 
                
                KcBERT의 학습시에 사용된 데이터로 알려져 있습니다.
                """)
        
        return dataset
    
    elif name == "ko-nli-class":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_NLI_dataset", data_dir="pair-class")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/kakaobrain/kor-nlu-datasets
                
                KAKAO에서 공개한 한국어 NLI Task를 위한 학습용 데이터셋입니다.
                데이터의 컬럼은 ["hypothesis", "premise", "label"]로 구성되어 있습니다.
                데이터의 총 개수는 392,702개 입니다.

                """)
        
        return dataset
    
    elif name == "ko-nli-score":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_NLI_dataset", data_dir="pair-score")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/kakaobrain/kor-nlu-datasets
                
                KAKAO에서 공개한 한국어 NLI Task를 위한 학습용 데이터셋을 STS의 형태로 가공한 것입니다.
                데이터의 컬럼은 ["sentence1", "sentence2", "score"]로 구성되어 있습니다.
                데이터의 총 개수는 392,702개 입니다.

                """)
        
        return dataset
    
    elif name == "ko-sts":
        login(token=token)
        dataset = load_dataset("x2bee/Korean_STS_all", data_dir="data")
        dataset = dataset['train']
        
        print("""
                Reference: https://github.com/kakaobrain/kor-nlu-datasets
                
                KAKAO에서 공개한 한국어 NLI Task를 위한 학습용 데이터셋입니다.
                데이터의 컬럼은 ["sentence", "pair", "label"]로 구성되어 있습니다.
                데이터의 총 개수는 7,128개 입니다.

                """)
        
        return dataset
    
    else:
        print("해당 데이터 셋은 존재하지 않습니다.")
        print("가능한 데이터 셋은 다음과 같습니다.")
        print("1. 'plateer-ctg'")
        print("2. 'ko-wiki'")
        print("3. 'ko-namuwiki'")
        print("4. 'kcbert-data'")
        print("5. 'ko-nli-class'")
        print("6. 'ko-nli-score'")
        print("7. 'ko-sts'")
        
        return None