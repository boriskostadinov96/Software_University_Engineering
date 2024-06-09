CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(emp_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        IF EXISTS (SELECT 1 FROM employees WHERE employee_id = emp_id) THEN
            UPDATE employees
            SET salary = salary * 1.05
            WHERE employee_id = emp_id;
        ELSE
            RAISE NOTICE 'Employee with id % does not exist.', emp_id;
        END IF;
    END;
END;
$$