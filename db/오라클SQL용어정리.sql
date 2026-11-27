
-- ctrl + enter키 : 실행

-- 테이블 생성: create table member();
create table member(
id varchar2(100) primary key,
pw varchar2(100) not null,
name varchar2(100),
phone varchar2(100),
gender varchar2(10) default '남자',
hobby varchar2(100) default '게임'
);

-- 테이블 삭제 : drop table 테이블명;
drop table 테이블명;

-- 테이터 입력: insert into 테이블 명(입력할 컬럼 명) values (입력할 데이터) 
-- 테이블의 모든 컬럼의 데이터를 입력시 : insert into member values() 가능
-- 하지만 일부 컬럼만 입력시 반드시 입력할 데이터의 컬럼 명을 작성해야함.
-- 테이블에 default 가 있으면 4번째 예시처럼 제외하고 데이터를 입력해도 디폴트 값이 들어감
insert into member(id,pw,name,phone,gender,hobby) values(
'aaa','1111','홍길동','010-1111-1111','남자','게임' );
insert into member(id,pw,name,phone,gender,hobby) values(
'bbb','1111','유관순','010-1111-1111','여자','게임' );
insert into member values (
'fff','1111','김유신','010-1111-1111','남자','게임');
insert into member (id,pw,phone) values(
'ggg','1111','010-1111-1111' );

-- 테이블의 전체 데이터 검색
select * from member;

-- 테이블의 일부 컬럼 검색 : 검색할 컬럼명을 작성해야함.
select id,name from member;

-- 테이블의 일부 데이터 검색 : 검색할 컬럼명과 조건을 작성해야함
select id from member where name='홍길동';

-- 테이블의 모든 데이터 수정 : update 테이블명 set 컬럼명= 새 데이터
-- member테이블의 name 컬럼의 모든 데이터를 '홍길동'으로 변경한다.
update member set name= '홍길동';

-- 테이블에서 특정 데이터 수정
-- member테이블에서 name 컬럼에서 '홍길순'인 데이터를 변경한다. gender은 '여자'로, pw는 '2222'로
update member set gender='여자',pw='2222' where name='홍길순';

-- 모든 데이터 삭제
delete from member;

-- 일부 데이터 삭제
-- member테이블에서 gender='여자'인 데이터만 삭제
delete from member where gender='여자'

-- 테이블 컬럼명과 타입 확인 : desc 컬럼명;
desc member;

-- 데이터 되돌리기 : 커밋을 안했다면
rollback;

-- 데이터 최종저장
-- 진짜 주의!! 커밋한 데이터는 롤백으로 못돌림!!
commit;

--------------------------------------------------

-- 타입
-- number() : 숫자, varchar2() : 가변문자열, char():고정문자열, date:날짜, clob: 대용량문자열
-- char() : 무조건 주어진 영역을 차지하고 데이터를 확인 (주로 전화번호나 주민번호와 같이 자리수가 정해져 있는 곳에서 사용)
-- varchar2() : 주어진 영역보다 적은 데이터가 있다면 그 길이만큼 저장, 용량낭비 없이 사용할 수 있음.
create table board(
bno number(7) primary key, -- 1 ~ 9999999 + 음수와 0도 가능!
btitle varchar2(1000),
bcontent clob,
bgroup number(7),
bstep number(4),
bindent number(4),
bdate date,
bfile varchar2(100)
);

-- number : +,-,*,/ 가능
-- date: +,- 가능
-- varchar2 : 사칙연산 안됨.
select '가' || '나' from dual; --가나 : || 가 print('가'+'나') 와 같음
select emp_name+email from employees; -- 안됨

--  임시 컬럼(약칭)
-- salary*1342 라는 컬럼을 k_salary로 약칭 가능.
select emp_name, salary , salary*1342 as k_salary from employees;
select emp_name, salary , salary*1342 k_salary from employees;

-- !!!! null값에는 사칙연산 불가능 ( 쉽게 무한이라고 생각하면 편함)
-- commission_pct가 null 이라면 salary*commission_pct도 null이 나옴, 즉 월급(salary)도 없다고 뜨는것.
select salary, commission_pct,salary*commission_pct from employees; 

-- 하지만 nvi(컬럼,0) : null값이 있을때 0으로 만들어 주면
-- commission_pct가 null이라도 월급(salary)는 나옴
select salary, commission_pct, salary+nvl(salary*commission_pct,0) from employees;

-- ""안에서는 특수문자, 한글, 띄어쓰기 등 사용할수있음. 다만 띄어쓰기는 자제
select salary, commission_pct, salary+nvl(salary*commission_pct,0)"실제월급" from employees;

--distinct : 중복제거
-- department_id에서 중복되는 데이터 제거 가능
select distinct(department_id) from employees;

--where 조건절 : 비교, <,<=,>,>=
--두개 이상일때는 and, or 가능

-- employees 테이블에서 salary가 5000 초과인 행 중 emp_name,salary 컬럼 데이터만 출력하시오.
select emp_name,salary from employees
where salary>5000;

-- employees 테이블에서 salary가 6000이상, department_id가 50인 데이터 중 employee_id, salary 컬럼데이터만 출력하시오.
select employee_id, salary from employees
where salary >= 6000 and department_id=50;

--급여가 4000 이하의 사원번호 사원이름, 급여를 출력하시오
select employee_id, emp_name, salary from employees
where salary<=4000;

--부서번호가 10이거나 30이거나 100인 사원을 출력하시오
select * from employees
where department_id=10 or department_id=30 or department_id=100;

--날짜비교
select hire_date from employees
where hire_date>'07/01/01';
select hire_date from employees
where hire_date>'2007/01/01';
select hire_date from employees
where hire_date>='2007-01-01' and hire_date<='07/12/31';

--number : 숫자 데이터 들어감(정수, 실수) -> number(4,2):99.99, number(4):9999
--char : 고정길이 문자 데이터 저장. -> char(20)이면 5글자만 저장되어도 20자리무조건 확보, 데이터 낭비대신 빠름
--varchar2 : 가변적인 길이 문자열-> varchar2(20)이면 5글자만 저장있으면 들어가있는 자리만 읽음, 공간낭비없는 대신 느림
--date : 날짜