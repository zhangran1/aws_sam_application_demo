create table employee
(
    id     varchar not null
        constraint employee_pk
            primary key,
    login  varchar,
    name   varchar,
    salary numeric
);

-- alter table employee
--     owner to postgres;

create unique index employee_id_uindex
    on employee (id);

create unique index employee_login_uindex
    on employee (login);

create table employ_create_details
(
    id            serial not null,
    created_at    varchar,
    employee_id   varchar
        constraint employ_create_details_employee_id_fk
            references employee
            on update cascade on delete cascade,
    deleted_at    varchar,
    delete_status boolean default false,
    updated_at    varchar
);

-- alter table employ_create_details
--     owner to postgres;

create table db_lock
(
    lock_status boolean default false,
    lock_id     varchar
);

-- alter table db_lock
--     owner to postgres;

create unique index db_lock_lock_id_uindex
    on db_lock (lock_id);



