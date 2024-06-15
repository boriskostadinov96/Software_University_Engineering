CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
    account_username VARCHAR(30)
) RETURNS INT
AS $$
DECLARE
    v_account_id INT;
    v_photos_count INT;
BEGIN

    SELECT id INTO v_account_id
    FROM accounts
    WHERE username = account_username;

    SELECT COUNT(*)
    INTO v_photos_count
    FROM accounts_photos
    WHERE account_id = v_account_id;

    RETURN v_photos_count;
END;
$$ LANGUAGE plpgsql;
