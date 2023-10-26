DROP TABLE if exists anhkab;
CREATE TABLE anhkab (
 `id` VARCHAR(100)  UNIQUE,
 `data` TEXT  NOT NULL
);
.separator "\t"
.import anhkab_input.txt anhkab
create index datum on anhkab(id);
pragma table_info (anhkab);
select count(*) from anhkab;
.exit
