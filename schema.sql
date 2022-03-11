CREATE TABLE IF NOT EXISTS prize
(
    id
    integer
    PRIMARY
    KEY,
    description
    char
(
    150
) NOT NULL
    );

CREATE TABLE IF NOT EXISTS participant
(
    id
    integer
    PRIMARY
    KEY,
    name
    char
(
    150
) NOT NULL
    );


CREATE TABLE IF NOT EXISTS promo
(
    id
    integer
    PRIMARY
    KEY,
    name
    char
(
    150
) NOT NULL,
    description char
(
    150
),
    prizes text,
    participants text
    );