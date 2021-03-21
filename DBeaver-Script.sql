drop table trv;
drop table tr;
drop table tr_group;
drop table tr_grouprd;

create table trv
(
id int,
release_group_id int,
title text,
subtitle text,
label text,
upc int,
pline_year int,
pline text
);

create table tr 
(
id int,
release_variant_id int,
title text,
subtitle text,
isrc int,
catalog_no int
);

create table tr_group
(
id int
);

create table tr_grouprd
(
release_group_id int,
release_date int
);

insert into trv
values
(
01,51,'last_christmas','','epic',1234,2017,'cd'
);

insert into trv
values
(
03,51,'kuaikuai','','epic',1345,2019,'dvd'
);

insert into trv
values
(
05,52,'pangpang','','fork',3456,2020,'dd'
);

insert into tr
values
(
11,01,'title_1','subtitle_1', 1111, 31
);

insert into tr
values
(
12,01,'title_2','subtitle_2', 2222, 32
);

insert into tr
values
(
13,03,'title_3','subtitle_3', 3333, 33
);

insert into tr_group
values
(
51
);


insert into tr_group
values
(
52
);

insert into tr_group
values
(
53
);

insert into tr_group
values
(
54
);

insert into tr_group
values
(
55
);

insert into tr_grouprd
values
(
51,
41
);

insert into tr_grouprd
values
(
52,
42
);

drop view trv_tr; 
create view trv_tr as
select 
tr.id as recording_id,
tr.release_variant_id,
trv.title as p_titlel,
trv.subtitle as p_subtitle,
trv.label,
trv.upc,
trv.pline_year,
trv.pline,
tr.title as track_title,
tr.subtitle as track_subtitle,
tr.isrc,
tr.catalog_no
from trv 
left join tr
on trv.id = tr.release_variant_id;

drop view trv_grouprd; 
create view trv_grouprd as
select 
trv.id as release_variant_id,
trv.release_group_id,
tr_grouprd.release_group_id,
tr_grouprd.release_date
from trv
left join tr_group
on trv.release_group_id = tr_group.id
left join tr_grouprd 
on tr_group.id = tr_grouprd.release_group_id;

drop view mix; 
create view mix as
select 
trv_grouprd.release_variant_id,
trv_tr.recording_id, 
trv_tr.label,
trv_grouprd.release_date
from trv_tr
left join trv_grouprd 
on trv_tr.release_variant_id = trv_grouprd.release_variant_id;

select * from trv;
select * from tr;
select * from tr_group;
select * from tr_grouprd;

select * from trv_tr ;
select * from trv_grouprd;
select * from mix;





