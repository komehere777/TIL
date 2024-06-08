# 데이터 프레임에서 컬럼별 inf/-inf 값 찾는 함수

```python
def get_inf_count(df):
    """Find the number of inf/-inf values per column in the dataframe"""
    return {
        col: df[df[col].isin([np.inf, -np.inf])].shape[0] for col in df.columns
    }
