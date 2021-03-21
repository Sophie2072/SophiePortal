drop table trv;
drop table tr;
drop table tr_group;
drop table tr_grouprd;
drop table trsequence;
drop table trvt;

delete from tr where id = 13;

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
catalog_number int
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

create table trsequence
(
release_variant_id int,
recording_id int,
sequence_no int,
group_no int
);

create table trvt
(
release_variant_id int,
included_territory text,
excluded_territory text
);

insert into trsequence
values
(
1,11, 61, 72
);

insert into trsequence
values
(
1,12, 62, 72
);

insert into trsequence
values
(
3,13, 63, 71
);

insert into trsequence
values
(
3,14, 64, 71
);

insert into trvt
values
(
1, 'a,b,c,d,e,f','p'
);

insert into trvt
values
(
3, 'a,b,c,d,e,f,g,h','p'
);

insert into trvt
values
(
5, 'd,i,k,y','p'
);

insert into trvt
values
(
7, 'u,o,l','y'
);


drop view tr_trv; 
drop view trv_grouprd; 
drop view tr_sequence;
drop view tr_territory;
drop view DSP_report;

create view tr_trv as
select 
tr.id as recording_id,
tr.release_variant_id,
trv.title as Product_title,
trv.subtitle as Product_Sub_Title,
trv.label as Label_Name,
trv.upc as Barcode,
trv.pline_year as Pyear,
trv.pline as Pname,
tr.title as Track_Title,
tr.subtitle as Track_Sub_Title,
tr.isrc as Track_ISRC,
tr.catalog_number as Catalogue_No
from tr
left join trv
on trv.id = tr.release_variant_id;


create view trv_grouprd as
select 
trv.id as release_variant_id,
trv.release_group_id,
tr_grouprd.release_date
from trv
left join tr_group
on trv.release_group_id = tr_group.id
left join tr_grouprd 
on tr_group.id = tr_grouprd.release_group_id;


create view tr_sequence as
select 
tr.id as recording_id,
tr.release_variant_id,
trsequence.group_no as Volumn_Number,
trsequence.sequence_no as Track_Number,
trsequence.sequence_no as Track_Index
from tr
left join trsequence
on tr.id = trsequence.recording_id and tr.release_variant_id = trsequence.release_variant_id;


create view tr_territory as
select 
tr.id as recording_id,
tr.release_variant_id ,
trvt.included_territory as Territorial_Availability
from tr
left join trv
on tr.release_variant_id = trv.id
left join trvt
on trv.id = trvt.release_variant_id;


create view DSP_report as
select 
tr_trv.*,
trv_grouprd.*,
tr_sequence.*,
tr_territory.*
from tr_trv
left join trv_grouprd 
on tr_trv.release_variant_id = trv_grouprd.release_variant_id
left join tr_sequence 
on tr_trv.recording_id = tr_sequence.recording_id and tr_trv.release_variant_id = tr_sequence.release_variant_id
left join tr_territory 
on tr_trv.recording_id = tr_territory.recording_id and tr_trv.release_variant_id = tr_territory.release_variant_id;

--
--select * from trv;
--select * from tr;
--select * from tr_group;
--select * from tr_grouprd;
--select * from trsequense;
--select * from trvt;
 
select * from tr_trv;
select * from trv_grouprd;
select * from tr_sequense;
select * from tr_territory;
select * from tr_sequence;
select * from DSP_report;








