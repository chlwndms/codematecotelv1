#✅ 문제
#현재 배열에는 9, 6, 7, 3, 5의 순서로 데이터가 저장되어 있습니다.
#이 때, 선택 정렬 기법을 사용해 자료를 오름차순으로 정렬하면서,
#배열의 위치 교환이 일어날 때 마다 전체 배열을 출력해 주세요.

array = [9, 6, 7, 3, 5]

def selection(arr) :
    for i in range(len(arr)) :
        min = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                n = j
        if (i != n):
            arr[i], arr[n] = arr[n], arr[i]
            print(arr)
    return arr

selection(array)
        