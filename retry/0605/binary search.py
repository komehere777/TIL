#이진탐색

def get_item(name, what, endpoint, start=1, end=None):
    """
    이진탐색으로 Grab the JSON payload 

    Parameters:
        - name: 찾고 있는 항목
        - what:  `name` 항목이 무엇인지 지정하는 딕셔너리
        - endpoint: 항목을 찾을 위치
        - start: 시작위치, 이 값을 수정할 필요는 없지만 함수는 재귀적으로 이 값을 조정한다.
        - end: 항목의 마지막 위치, 중간점을 찾는데 사용되지만 'start'처럼 신경쓰지 않아도 된다.

    Returns:
        항목을 찾았다면 항목 정보의 딕셔너리, 찾지 못하면 빈 딕셔너리
    """
    # 매번 데이터를 절반으로 자르기 위한 중간점을 찾는다
    mid = (start + (end or 1)) // 2
    
    # lowercase the name so this is not case-sensitive
    name = name.lower()
    
    # define the payload we will send with each request
    payload = {
        'datasetid': 'GHCND',
        'sortfield': 'name',
        'offset': mid, # 매번 offset을 바꾼다.
        'limit': 1 # 1개의 값만 받는다.
    }
    
    # `what`에  추가 필터를 추가하도록 요청한다.
    response = make_request(endpoint, {**payload, **what})
    
    if response.ok:
        payload = response.json()

        # if response is ok, 응답 메타데이터에서 마지막 인덱스를 가져온다.
        end = end or payload['metadata']['resultset']['count']
        
        # grab the lowercase version of the current name
        current_name = payload['results'][0]['name'].lower()
        
        # if what we are searching for is in the current name, we have found our item
        if name in current_name:
            return payload['results'][0] # return the found item
        else:   #name이 없다면
            if start >= end: 
                # 만약 시작 인덱스가 마지막보다 크거나 같이면 항목을 못찾은 거임
                return {}
            elif name < current_name:
                # 이름이 알파벳순으로 현재 이름보다 앞에 있으면 데이터 절반의 왼쪽에서 검색
                return get_item(name, what, endpoint, start, mid - 1)
            elif name > current_name:

                # 이름이 알파벳순으로 현재 이름보다 뒤에 있으면 데이터 절반의 오른쪽에서 검색
                return get_item(name, what, endpoint, mid + 1, end)    
    else:
        # response wasn't ok, use code to determine why
        print(f'Response not OK, status: {response.status_code}')

#이진탐색 일반
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 예시 사용법
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"타겟 값 {target}은(는) 배열의 인덱스 {result}에 있습니다.")
else:
    print(f"타겟 값 {target}을(를) 배열에서 찾을 수 없습니다.")
