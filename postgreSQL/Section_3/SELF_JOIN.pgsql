SELECT e.first_name || ' ' || e.last_name AS employees,
        m.first_name || ' ' || m.last_name AS manager
FROM employee
LEFT JOIN employee m ON m.employee_id = e.manager_id
ORDER BY manager;