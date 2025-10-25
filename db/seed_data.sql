USE fsdu3;

INSERT INTO questions (question_text, category)
VALUES
    ('CD and DVD drives are examples of what?', 'Technology'),
    ('ROM is an example of what type of memory?', 'Technology'),
    ('A permanent memory is called what?', 'Technology'),
    ('Which memory does not store data permanently?', 'Technology'),
    ('Which was the first computer in the world?', 'Technology');

INSERT INTO answers (question_id, answer_text)
VALUES
    (1, 'Storage Devices'),
    (1, 'storage devices'),
    (2, 'Non volatile'),
    (2, 'non volatile'),
    (3, 'ROM'),
    (3, 'rom'),
    (4, 'RAM'),
    (4, 'ram'),
    (5, 'ENIAC computing system'),
    (5, 'eniac computing system');
