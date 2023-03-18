DROP TABLE if exists harsaauthtooltips;
CREATE TABLE harsaauthtooltips (
 `key` VARCHAR(20) NOT NULL,
 `data` VARCHAR(20000) NOT NULL
);
.separator "\t"
.import tooltip.txt harsaauthtooltips
pragma table_info (harsaauthtooltips);
select count(*) from harsaauthtooltips;
.exit
