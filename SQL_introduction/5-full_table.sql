-- A script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT
	t.table_name AS "Table",
	CONCAT(
		"CREATE TABLE `", t.table_name, "` (\n",
		GROUP_CONCAT(
			CONCAT(
				"  `", c.column_name, "` ",
				c.column_type, ' DEFAULT ',
				IF(c.column_default IS NULL,
					"NULL",
					CONCAT('\'', c.column_default, '\'')
				)
			)
		ORDER BY c.ordinal_position
		SEPARATOR ',\n'
		),
		'\n) ENGINE=', t.engine,
		' DEFAULT CHARSET=', SUBSTRING_INDEX(t.table_collation, '_', 1),
		' COLLATE=', t.table_collation
	) AS "Create Table"
FROM information_schema.tables t
JOIN information_schema.columns c
ON t.table_name = c.table_name AND t.table_schema = c.table_schema
WHERE t.table_schema = 'hbtn_0c_0' AND t.table_name = 'first_table'
GROUP BY t.table_name, t.engine, t.table_collation;

