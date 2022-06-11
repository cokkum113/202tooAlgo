-- 없어진 기록 찾기
select a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS a left outer join ANIMAL_INS b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.ANIMAL_ID is NULL
order by a.ANIMAL_ID

-- 있었는데요 없었습니다
select a.ANIMAL_ID, a.NAME
from ANIMAL_INS a join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.DATETIME > b.DATETIME
order by a.DATETIME


-- 오랜 기간 보호한 동물(1)
select a.NAME, a.DATETIME
from ANIMAL_INS a 
left  join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.ANIMAL_ID is null
order by a.DATETIME
limit 3

-- 보호소에서 중성화한 동물
select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS a 
join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_INTAKE != b.SEX_UPON_OUTCOME
order by a.ANIMAL_ID

