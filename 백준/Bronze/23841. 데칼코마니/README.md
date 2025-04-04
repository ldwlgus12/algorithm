# [Bronze I] 데칼코마니 - 23841 

[문제 링크](https://www.acmicpc.net/problem/23841) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2025년 4월 4일 19:15:25

### 문제 설명

<p>시험과 과제에 지친 희권이는 취미로 그림을 그리기 시작했다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8064ec54-5f48-4eff-a4d1-910fdaf5ee47/-/preview/" style="height: 100px; width: 237px;"></p>

<p>하지만, 그림이 별로 마음에 들지 않아 데칼코마니로 바꾸려 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2f16e34f-6374-4168-b028-0b5b6a6dddf9/-/preview/" style="width: 701px; height: 100px;"></p>

<p>위에 보이는 것처럼 그림을 좌우 방향으로 반으로 포개어 접으면, 맞닿는 면에 물감이 번지면서 데칼코마니가 완성된다.</p>

<p>접은 그림은 원래대로 되돌릴 수 없기 때문에 희권이는 결과를 미리 알고 싶어 한다.</p>

<p>희권이에게 그림을 데칼코마니 한 결과를 알려주자.</p>

### 입력 

 <p>첫 줄에 그림의 세로 길이 정수 <em>N</em>과 가로 길이 정수 <em>M</em>이 주어진다. (1 ≤ <em>N</em>, <em>M</em> ≤ 50, <em>M</em>은 짝수)</p>

<p><em>N</em>개 줄에 <em>M</em>개씩 그림에 대한 정보가 주어진다.</p>

<p>물감은 26가지가 있고, 각각 알파벳 대문자 하나로 나타낸다.</p>

<p>그림에서 색칠한 곳은 물감에 해당하는 알파벳으로 빈 곳은 <code>'.'</code>으로 표현한다. 그림의 가로 길이는 짝수이고, 그림을 접었을 때 두 물감이 겹치는 경우는 없다.</p>

### 출력 

 <p>데칼코마니 한 그림을 <em>N</em>개의 줄에 걸쳐 출력한다.</p>

