| Parameter | Type   | Description                                                                                      |
|-----------|--------|--------------------------------------------------------------------------------------------------|
| name      | str    | 데이터 셋의 이름을 입력합니다. 가능한 값은 'plateer-ctg', 'ko-wiki', 'ko-namuwiki', 'kcbert-data', 'ko-nli-class', 'ko-nli-score', 'ko-sts'입니다. |
| token     | str    | Huggingface의 토큰을 입력합니다. x2bee repository에 접근할 수 있어야 합니다. (기본값: None)                                      |

### Returns
- dataset: 불러온 데이터 셋을 반환합니다. 데이터 셋의 구성 및 개수는 선택한 데이터 셋에 따라 다릅니다.

### Possible Values for `name`
1. 'plateer-ctg' - Plateer 카테고리 분류 데이터 셋
2. 'ko-wiki' - 한국어 위키백과 데이터 셋
3. 'ko-namuwiki' - 한국어 나무위키 데이터 셋
4. 'kcbert-data' - KcBERT 학습 데이터 셋 (뉴스 댓글)
5. 'ko-nli-class' - 한국어 NLI 데이터 셋 (KAKAO제공 NLI 작업 학습용)
6. 'ko-nli-score' - 한국어 NLI 데이터 셋을 STS 형태로 변환환 (KAKAO제공 NLI 작업 학습용)
7. 'ko-sts' - 한국어 STS 데이터 셋 (KAKAO제공 STS 작업 학습용)

### Dataset Columns and Sizes
| Dataset Name  | Columns                                   | Number of Entries |
|---------------|-------------------------------------------|-------------------|
| plateer-ctg   | goods_nm, category, label                 | 24,287,817        |
| ko-wiki       | text                                      | 14,761,960        |
| ko-namuwiki   | text                                      | 21,366,681        |
| kcbert-data   | text                                      | 86,246,285        |
| ko-nli-class  | hypothesis, premise, label                | 392,702           |
| ko-nli-score  | sentence1, sentence2, score               | 392,702           |
| ko-sts        | sentence, pair, label                     | 7,128             |

### Example Usage
```bash
git clone https://github.com/X2bee/plateer_dataloader.git
```

```python
from tools.loader import plateer_dataset

dataset = plateer_dataset("plateer-ctg")
print(dataset)
```