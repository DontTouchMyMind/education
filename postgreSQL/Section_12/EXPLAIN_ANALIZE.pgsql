CREATE TABLE perf_test(
    id int,
    reason text COLLATE "C",
    annotation text COLLATE "C"
);

INSERT INTO perf_test(id, reason, annotation)
SELECT s.id, md5(random()::text), NULL
FROM generate_series(1, 10000000) AS s(id)
ORDER BY random();

SELECT * FROM perf_test LIMIT 10;

EXPLAIN SELECT * FROM perf_test WHERE id = 3700000;

CREATE INDEX idx_perf_test_id ON perf_test(id);

UPDATE perf_test
SET annotation = UPPER(md5(random()::text));

EXPLAIN SELECT * FROM perf_test
WHERE reason LIKE 'bc%' AND annotation LIKE 'AB%';

CREATE INDEX idx_perf_test_reason_annotation ON perf_test(reason, annotation);
