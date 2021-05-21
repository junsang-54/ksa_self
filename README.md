#수강생번호 : 012-49391235

# 21.05.20
* 파이썬 내장 함수
  * abs() : 수의 절대값 반환
    * ()안에 숫자 대입
  * all() : 개체 혹은 개체 내에 것들이 전부 True면 True 반환
    * mylist = [0, 1, 1]
      
      x = all(mylist)
  * any() : 개체 혹은 개체 내에 것들이 하나라도 True면 True 반환
  * ascii() : 아스키코드화
    * ()안에 객체 대입
  * bin() : 2진수 변환
  * bool() : boolean 값으로 변환
  * bytearray() : 개체를 byte 배열로 변환, 지정한 크기의 빈 byte 배열 개체로 만듦
    * x = bytearray(4): x를 4byte 배열의 개체로 변환
  * bytes() : bytearray()와 다르게 반환 후 수정할 수 없음
  * callable() : ()안에 함수가 정의된 함수면 True
  * chr() : character 형식으로 바꿈
    * ()안에 숫자 대입
  * classmethod() : 클래드 메소드로 변환
  * complie() : 소스를 개체로 반환하여 실행시킬 준비함
  * complex() : 실수와 허수로 복소수 만듦
  * delattr() : 개체의 특정 속성을 제거
  * dict() : dictionary형 자료로 변환
    * dictionary란 대응 관계를 나타낼 수 있는 자료형
    * x = dict(name = "John", age = 36, country = "Norway")
  * dir() : 개체의 모든 속성 및 메서드 반환
  * divmod() : a 나누기 b의 몫과 나머지
  * enumerate() : 자료형을 입력 받아 인덱스 값을 포함한 개체로 변환
  * eval() : 실행 가능한 문자열을 받아 실행한 결과값 반환
  * exec() : 실행가능한 코드를 받아 실행한 결과값 반환
  * filter() : 제거하고 싶은거 제거
  * float() : 실수로 변환(부동소수점)
  * format() : 포맷을 변환
  * frozenset() : 고정시키는거 *
  * getattr() : 원하는 속성 출력
  * globals() : 
  * hasattr() : 지정한 속성이 있는지 확인
  * hash() :
  * help() :
  * hex() : 16진법으로 변환
  * id() : 개체의 주소값
  * input() :
  * int() : 정수로 변환
  * isinstance() : object의 type 진위여부
  * issubclass() : 상위클래스의 하위클래스가 맞는지 진위여부
  * iter() :
  * len() : 개체의 길이
  * list() : 리스트화
  * locals() : 
  * map() : 함수를 원하는 만큼 반복
  * max() : 최댓값
  * memoryview() : 해당 메모리를 봄 유니코드?
  * min() : 최솟값
  * next() : 자료형에서 다음 인덱스 봄
  * object() : 개체화
  * oct() : 8진법
  * open() : 파일 오픈
  * ord() : 유니코드 변환
  * pow() : 거듭제곱
  * print() : 프린팅
  * property() : 속성 설정
  * range() : 범위 만듦
  * repr() :
  * reversed() : 순서 반대로
  * round() : 원하는 위치에서 반올림
  * set() : 새로운 세트
  * setattr() :
  * slice() :
  * sorted() : 순서대로 배열
  * @staticmethond() :
  * str() : string type 변환
  * sum() : 합
  * super() : 자식클래스가 부모 클래스 가져옴
  * tuple() :
  * type() :
  * vars() :
  * zip() :




# 21.05.20
* 파이썬 키워드
  * and
  * as
  * assert
  * break
  * class
  * continue
  * def
  * del
  * elif
  * else
  * except
  * False
  * finally
  * for
  * from
  * global
  * if
  * import
  * in
  * is
  * lambda
  * None
  * nonlocal
  * not
  * or
  * pass
  * raise
  * return
  * True
  * try
  * while
  * with
  * yield



# 21.05.10

## 1. 개별 프로젝트
* 조장 확인 프로그램
  * 무엇
  * 그림 : pygame (https://digiconfactory.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B2%8C%EC%9E%84%EB%A7%8C%EB%93%A4%EA%B8%B0-8-%EC%9E%A1%EC%84%A4-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%A1%9C%EB%93%9C%EC%99%80-%EC%A1%B0%EC%9E%91%EB%B0%A9%EB%B2%95-PYGAME)
  * 마우스 키보드 : win32api 라이브러리(https://www.youtube.com/watch?v=3izsuZmct80) pygame (https://devnauts.tistory.com/61)
* 출석 퇴실 알람
  * 와이파이가 잡히면 메일받기?
    * 와이파이 모듈(https://eu4ng.tistory.com/36)
  * 프로그램으로 만들어서 컴퓨터 열때 알림가기



# 21.04.29

## 1. 수업
* 프로젝트 발표준비
* 선형대수학, 경사하강법



# 21.04.28

## 1. 수업
* ROC곡선
* 다중분류기

## 2. 자습
* 프로젝트: 테니스 승률 예측 프로그래밍

# 21.04.27

## 1. 수업
* 주피터 노트북
  * 캘리포니아 집값
* 팀 과제(프로젝트)
  * 테니스 승패 
* 모델평가
  * 분류문제


# 21.04.26

## 1. 수업
* 패턴인식 개요
* Jupyter notebook 가상환경 구축 및 예제 실습

## 2. 자습
* 자바 클래스 복습
  * 참조, 객체, 생성자


# 21.04.25

## 과제
* 데이터 콘서트
  * 공공데이터를 활용한 아이디어 : 버스정류장 정보 확대


# 21.04.24

## 자습
### 자바
* 참조타입, 배열, 열거
* Class


# 21.04.23

## 1. 수업
syntax 문법 오류 - 컴파일 안됨
symentic 구조(논리) 오류 - 컴파일은 되는데 실행이 안됨

* 함수
* 문자열
  * string은 "a"는 50, 문자열 추가할때마다 +1
  * mac 경로 : 상단 바 편집에서 option 누르면 경로 복사 나옴
* 자료구조 (!매우 중요!)
  * key, lambda, reverse 검색해보기!


# 21.04.22

## 1. 수업
### 프로젝트
* 삼각함수 : 객체 생성
  * Operation외에 다른 클래스에 메소드 호출

* 파이썬 시작
  * 파이썬, 미니콘다, 아톰 설치
  * 아톰에서 autocomplete-python 오류 -> 아나콘다, 파이참 설치
  

## 2. 자습
### 자바
* 목표 : 3장 ~ 5장 학습
* 실제 : ~ 4-1장

#### 학습내용
+ 타입변환
  + 작은 범위는 큰 범위에 저장 할 때 큰 범위 타입으로 변환
