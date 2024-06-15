CREATE OR REPLACE PROCEDURE udp_modify_account(
    address_street VARCHAR(30),
    address_town VARCHAR(30)
)
AS
$$
DECLARE
    v_account_id INT;
    v_current_job_title VARCHAR(40);
BEGIN

    SELECT a.id, a.job_title
    INTO v_account_id, v_current_job_title
    FROM accounts AS a
    JOIN addresses AS ad ON a.id = ad.account_id
    WHERE ad.street = address_street
      AND ad.town = address_town;

    IF FOUND THEN
        UPDATE accounts
        SET job_title = '(Remote) ' || v_current_job_title
        WHERE id = v_account_id;
    END IF;
END;
$$
LANGUAGE plpgsql;