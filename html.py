# 실행해서 데이타가 잘 나오는지 확인

'''
// 클라이언트단은?
- HTML
- CSS

/ HTML 버전
- 웹페이지의 컨텐츠(이미지, 텍스트, 하이퍼링크, 테이블 ...)의 마크업 언어
- HTML 4
- XHTML
- HTML 5

// 파이참에서 HTML5 문서 만들기
1) 폴더 마우스 우측버튼
2) HTML 문서
3) HTML5

// HTML5 태그 특징
- 대소문자는 상관없다. 소문자 권장
- 구조
 <태그명> ... </태그명> : 짝이 있는 구조
 <태그명/> : 단독태그

- 태그명안에 들어가는 요소
    <태그명 [속성='값']>

    <a href='https://www.google.com/'>구글로 이동하기</a>

// HTML5 태그
주석 <!-- 주석내용 -->

h1 ~ h6(heading) : 글자 진하게, 숫자가 클수록 글자가 작아진다.

p(paragragh) : 문단생성

ul>li : 목록 문단
ol>li : 순서목록 문단
ul(unordered list)
ol(ordered list)
li(list)

dl>dt+dd : 정의문단
dl(definition list)
dt(definition title)
dd(definition data)
----------------------------------------------------
2019-07-19
br(break line) : 줄바꿈
<br> 또는 <br/>

hr(horizontal rule) : 수평선
<hr> 또는 <hr/>

blockquote : 인용문에 사용
            들여쓰기가되어 앞뒤에 여백 생성

em / i => 기울임꼴
strong / b => 진하게
: 인라인 요소

img(image)
<img src = 이미지 경로 alt=대체텍스트>
<img src = 이미지경로 alt = 대체텍스트 />
src(source)
alt(alternate text) : 이미지 대신 나오는 글자
width/height/border

예제 이미지 폴더 생성하기
- images 폴더 명
smile.zip 다운르드후애 images 폴더에 앚축해제

웹페이지 => 웹에서 사용되는
png, jpg, gif
svg(벡터)

a(anchor)
파일(html, 이미지, 웹상주소)과 연결가능
텍스트 하이퍼링크
<a href ='URL'> 글자 </a>
이미지 하이퍼링크
<a href ='URL'> <img src = 이미지경로 atl = 대체 텍스트> </a>

a의 속성들
    href - 연결주소(html, 이미지, 웹상주소(http://~))
    target - _black : 새탭에 주소가 표시된다.
    title - 하이퍼링크 툴팁가능
인라인요소


table
  table>tr>td
  table>tr>th

tr : table row  - 행
td: table data - 셀
th: table head - 제목셀, 글내용이 중앙정렬, 진하게 표시

관련 속성들...
border : 테두리
width / height : 가로 세로 크기
cellpadding : 셀 안쪽여백
cellspacing : 셀과 셀 사이 여백
align : 가로 정렬 center/right/left
valign : 셀의 세로 정렬 top/middle/bottom
bordercolor: 테두리 색상
bgcolor : 배경 색상


셀합치기
colspan : 가로합치기
rowspan : 세로합치기
주의사항: 셀을 합치고 나머지는 삭제하거나 주석처리한다.


form 문서 : 로그인, 회원가입, 게시판, 주문서 ...
폼 구성요소
- 라벨
- 입력상자/ 암호상자/ 여러줄글상자
- 체크박스/ 라디오버튼/ 폼버튼(제출, 리셋)
- 필드셋/ 레전드

form > 폼구성요소




address => 주소

// 파이참에서 html 코딩 기법 - 자동완성
태그입력 후 [tab]


// Emmet 코딩방식으로 HTML 입력하기
태그명1 + 태그명2 ... [tab].
태그명 * 3 [tab] 반복
$ 자동 숫자 증감
{} 내용입력 ... 브레이스,,?
() 그룹핑

'''