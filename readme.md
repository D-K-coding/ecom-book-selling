# 📃 Documentation

## ➡ Table of content

- [📃 Documentation](#-documentation)
  - [➡ Table of content](#-table-of-content)
  - [Diagrams](#diagrams)
    - [✔ ER Diagram](#-er-diagram)
    - [👤 Roles](#-roles)

## Diagrams

### ✔ ER Diagram

Related entities and set of users

| Name of the Entity | Contains                                                                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| admin              | id, password, email, name, role                                                                      |
| sellers/authors    | seller_id, password, email, contact_number, address, GST_no, payment_details,   book_id              |
| buyers/customers   | name, address, username, password, email, payment_details, password, contact_number, pincode         |
| book               | book_id, price, discount, name, genre, author, stock,seller_id                                       |
| order              | order_id, payment_status, payment_id, order_date, book_id, seller_id, return_status, review, ratings |

### 👤 Roles

| Role name | Description                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| admin     | manages the whole web application. Can delete, update, add sellers                                            |
| seller    | adds books, create discounts, removes books/discounts, manages stock, sends the notification of ready to ship |
| delivery  | handles the delivery, gets and sends the notification of the shipping status                                  |