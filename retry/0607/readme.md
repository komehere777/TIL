#'date' 컬럼을 datetime 형식으로 변환하는 방법

```python
df = df.assign(date=pd.to_datetime(df['date']))

df['date'] = df['date'].apply(pd.to_datetime)

df['date'] = df['date'].astype('datetime64[ns]')

df['date'] = df['date'].map(pd.to_datetime)

