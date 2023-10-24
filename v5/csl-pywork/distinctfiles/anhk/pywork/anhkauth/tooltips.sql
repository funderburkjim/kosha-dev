DROP TABLE if exists anhkauthtooltips;
CREATE TABLE anhkauthtooltips (
 `key` VARCHAR(20) NOT NULL,
 `data` VARCHAR(20000) NOT NULL
);
.separator "\t"
.import tooltip.txt anhkauthtooltips
pragma table_info (anhkauthtooltips);
select count(*) from anhkauthtooltips;
.exit
