select current_time;
select current_date;
select now;
select current_timestamp;
select extract(year from current_date);
select extract (hour from current_time)

select current_date + 10;
select current_date -10;
select current_date + interval '2 months';
select current_date + interval '2 years';
select current_date + interval '2 weeks';
select current_date + interval '2 days';

select age('2026-11-26','2004-08-21');
select to_char(current_date,'dd-mm-yyyy');
select to_char(now(),'dd-mm-yy hh12:mi:ss');