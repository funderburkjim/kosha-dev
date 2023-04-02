DROP TABLE if exists harsaab;
CREATE TABLE harsaab (
 `id` VARCHAR(100)  UNIQUE,
 `data` TEXT  NOT NULL
);
.separator "\t"
.import harsaab_input.txt harsaab
create index datum on harsaab(id);
pragma table_info (harsaab);
select count(*) from harsaab;
.exit
