create table book
(
    name        varchar(100) not null,
    url_book    varchar(2048),
    author      varchar(250),
    description text,
    id          serial
        constraint book_pk
            primary key
);

alter table book
    owner to postgres;

insert into book(name,url_book,author,description) values ('Алиса в стране чудес','https://www.100bestbooks.ru/files/Carroll_Alisa_v_strane_chudes.pdf?ysclid=lofx9q34e0335759270','Люис Кэррол','Невероятная, ни на что не похожая сказка Льюиса Кэрролла, английского писателя и математика, «Алиса в Стране Чудес» заслужила любовь читателей всех возрастов и по всему миру. В этой книге непредсказуемый волшебный мир и его обитатели — Белый кролик, Чеширский Кот, Шляпник и Королева Червей — представлены в иллюстрациях известной российской художницы Ирины Петелиной, мастерство которой высоко оценено не только в России, но и во многих зарубежных странах.');

create table "user"
(
    id       serial
        constraint user_pk
            primary key,
    identity varchar(250) not null
);

alter table "user"
    owner to postgres;

create table mark
(
    id      serial
        constraint mark_pk
            primary key,
    user_id integer
        constraint mark_user_id_fk
            references "user"(id),
    book_id integer
        constraint mark_book_id_fk
            references book(id),
    date    date
);

alter table mark
    owner to postgres;

create table rating
(
    id      serial
        constraint rating_pk
            primary key,
    user_id integer
        constraint rating_user_id_fk
            references "user"(id),
    point   integer
);

alter table rating
    owner to postgres;

create table sequence
(
    date_range daterange not null,
    book_id    integer
        constraint sequence_book_id_fk
            references book(id),
    id         serial
        constraint sequence_pk
            primary key
);

alter table sequence
    owner to postgres;

create table sequence_mark
(
    id          serial
        constraint sequence_mark_pk
            primary key,
    mark_id     integer
        constraint sequence_mark_mark_id_fk
            references mark(id),
    sequence_id integer
        constraint sequence_mark_sequence_id_fk
            references sequence(id),
    chat_id     integer
);

alter table sequence_mark
    owner to postgres;

